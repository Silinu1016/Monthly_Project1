import numpy as np
import tensorflow
import tensorflow.keras.backend as K
from tensorflow.keras.layers import Input, Lambda
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import TensorBoard, ModelCheckpoint, ReduceLROnPlateau, EarlyStopping
import os
from yolo3.model import preprocess_true_boxes, yolo_body, tiny_yolo_body, yolo_loss
from yolo3.utils import get_random_data
import tensorflow.keras as keras
from PIL import Image
from matplotlib.colors import rgb_to_hsv, hsv_to_rgb
transfer_learning_name="yolov3-tiny_Finger_version"
train_name="train"
file_directory="G:/공유 드라이브/TX2/엘레베이터_TX2"
train_dir=os.path.join(file_directory,train_name)

weight_path = os.path.expanduser(os.path.join(file_directory,f"{transfer_learning_name}.h5"))
# weights_path = os.path.expanduser(os.path.join(file_directory,f"{transfer_learning_name}.weights"))
annotation_path = os.path.expanduser(os.path.join(file_directory,f"{train_dir}/train_all_mix_1.txt"))
log_dir = os.path.expanduser(os.path.join(file_directory,f"{train_dir}/logs/001/"))
classes_path = os.path.expanduser(os.path.join(file_directory,f"{train_dir}/classes.txt"))
anchors_path = os.path.expanduser(os.path.join(file_directory,f"{train_dir}/anchors.txt"))
def _main():
    class_names = get_classes(classes_path)
    num_classes = len(class_names)
    anchors = get_anchors(anchors_path)

    input_shape = (416,416) # multiple of 32, hw

    is_tiny_version = len(anchors)==6 # default setting
    if is_tiny_version:
        model = create_tiny_model(input_shape, anchors, num_classes,freeze_body=2, weights_path=weight_path)
    else:
        model = create_model(input_shape, anchors, num_classes,freeze_body=2, weights_path=weight_path) # make sure you know what you freeze

    logging = TensorBoard(log_dir=log_dir)
    checkpoint = ModelCheckpoint(log_dir + 'ep{epoch:03d}-loss{loss:.3f}-val_loss{val_loss:.3f}.h5',
        monitor='val_loss', save_weights_only=True, save_best_only=True, period=3)
    reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.1, patience=3, verbose=1)
    early_stopping = EarlyStopping(monitor='val_loss', min_delta=0, patience=10, verbose=1)

    val_split = 0.1
    with open(annotation_path) as f:
        lines = f.readlines()
    np.random.seed(10101)
    np.random.shuffle(lines)
    np.random.seed(None)
    num_val = int(len(lines)*val_split)
    num_train = len(lines) - num_val

    # Train with frozen layers first, to get a stable loss.
    # Adjust num epochs to your dataset. This step is enough to obtain a not bad model.
    if True:
        model.compile(optimizer=Adam(lr=0.001), loss={
            # use custom yolo_loss Lambda layer.
            'yolo_loss': lambda y_true, y_pred: y_pred})

        batch_size =64
        print(data_generator_wrapper(lines[:num_train], batch_size, input_shape, anchors, num_classes))
        print('Train on {} samples, val on {} samples, with batch size {}.'.format(num_train, num_val, batch_size))
        model.fit_generator(data_generator_wrapper(lines[:num_train], batch_size, input_shape, anchors, num_classes),
                steps_per_epoch=max(1, num_train//batch_size),
                validation_data=data_generator_wrapper(lines[num_train:], batch_size, input_shape, anchors, num_classes),
                validation_steps=max(1, num_val//batch_size),
                epochs=50,
                initial_epoch=0,
                callbacks=[logging, checkpoint])
        model.save_weights(log_dir + 'trained_weights_stage_1.h5')

    # Unfreeze and continue training, to fine-tune.
    # Train longer if the result is not good.
    if True:
        for i in range(len(model.layers)):
            model.layers[i].trainable = True
        model.compile(optimizer=Adam(lr=1e-4), loss={'yolo_loss': lambda y_true, y_pred: y_pred}) # recompile to apply the change
        print('Unfreeze all of the layers.')

        batch_size = 64 # note that more GPU memory is required after unfreezing the body
        print('Train on {} samples, val on {} samples, with batch size {}.'.format(num_train, num_val, batch_size))
        model.fit_generator(data_generator_wrapper(lines[:num_train], batch_size, input_shape, anchors, num_classes),
            steps_per_epoch=max(1, num_train//batch_size),
            validation_data=data_generator_wrapper(lines[num_train:], batch_size, input_shape, anchors, num_classes),
            validation_steps=max(1, num_val//batch_size),
            epochs=100,
            initial_epoch=50,
            callbacks=[logging, checkpoint, reduce_lr, early_stopping])
        model.save_weights(log_dir + 'trained_weights_final.h5')

    # Further training if needed.


def get_classes(classes_path):
    '''loads the classes'''
    with open(classes_path) as f:
        class_names = f.readlines()
    class_names = [c.strip() for c in class_names]
    return class_names

def get_anchors(anchors_path):
    '''loads the anchors from a file'''
    with open(anchors_path) as f:
        anchors = f.readline()
    anchors = [float(x) for x in anchors.split(',')]
    return np.array(anchors).reshape(-1, 2)


def create_model(input_shape, anchors, num_classes, load_pretrained=True, freeze_body=2,weights_path=weight_path):
    '''create the training model'''
    K.clear_session() # get a new session
    image_input = Input(shape=(None, None, 3))
    h, w = input_shape
    num_anchors = len(anchors)
    print(num_anchors)
    y_true = [Input(shape=(h//{0:32, 1:16, 2:8}[l], w//{0:32, 1:16, 2:8}[l], \
        num_anchors//3, num_classes+5)) for l in range(3)]

    model_body = yolo_body(image_input, num_anchors//3, num_classes)
    print('Create YOLOv3 model with {} anchors and {} classes.'.format(num_anchors, num_classes))
    '''
    if load_pretrained:
        model_body.load_weights(weights_path, by_name=True)#, skip_mismatch=True)
        print('Load weights {}.'.format(weights_path))
        if freeze_body in [1, 2]:
            # Freeze darknet53 body or freeze all but 3 output layers.
            num = (185, len(model_body.layers)-3)[freeze_body-1]
            for i in range(num): model_body.layers[i].trainable = False
            print('Freeze the first {} layers of total {} layers.'.format(num, len(model_body.layers)))
    '''
    model_loss = Lambda(yolo_loss, output_shape=(1,), name='yolo_loss',
        arguments={'anchors': anchors, 'num_classes': num_classes, 'ignore_thresh': 0.5})(
        [*model_body.output, *y_true])
    model = Model([model_body.input, *y_true], model_loss)

    return model

def create_tiny_model(input_shape, anchors, num_classes, load_pretrained=True, freeze_body=2,weights_path=weight_path):
    '''create the training model, for Tiny YOLOv3'''
    K.clear_session() # get a new session
    image_input = Input(shape=(None, None, 3))
    h, w = input_shape
    num_anchors = len(anchors)
    print(num_anchors)
    print(num_classes)
    y_true = [Input(shape=(h//{0:32, 1:16}[l], w//{0:32, 1:16}[l], \
        num_anchors//2, num_classes+5)) for l in range(2)]

    model_body = tiny_yolo_body(image_input, num_anchors//2, num_classes)
    print('Create Tiny YOLOv3 model with {} anchors and {} classes.'.format(num_anchors, num_classes))
    '''
    if load_pretrained:
        model_body.load_weights(weights_path, by_name=True)#, skip_mismatch=True)
        print('Load weights {}.'.format(weights_path))
        if freeze_body in [1, 2]:
            # Freeze the darknet body or freeze all but 2 output layers.
            num = (20, len(model_body.layers)-2)[freeze_body-1]
            for i in range(num): model_body.layers[i].trainable = False
            print('Freeze the first {} layers of total {} layers.'.format(num, len(model_body.layers)))
    '''
    model_loss = Lambda(yolo_loss, output_shape=(1,), name='yolo_loss',
        arguments={'anchors': anchors, 'num_classes': num_classes, 'ignore_thresh': 0.7})( [*model_body.output, *y_true])
    model = Model([model_body.input, *y_true], model_loss)

    return model

def data_generator(annotation_lines, batch_size, input_shape, anchors, num_classes):
    '''data generator for fit_generator'''
    n = len(annotation_lines)
    i = 0
    while True:
        image_data = []
        box_data = []
        for b in range(batch_size):
            if i==0:
                np.random.shuffle(annotation_lines)
#             image, box = get_random_data(annotation_lines[i], input_shape, random=True)
            annotation_line =annotation_lines[i]
            line = annotation_line.split(" ")
            random=True
            max_boxes=20
            jitter=.3
            hue=.1
            sat=1.5
            val=1.5
            proc_img=True
            image = Image.open(line[0]+" "+line[1])
            iw, ih = image.size
            h, w = input_shape
            box = np.array([np.array(list(map(int,box.split(',')))) for box in line[2:]])

            if not random:
                # resize image
                scale = min(w/iw, h/ih)
                nw = int(iw*scale)
                nh = int(ih*scale)
                dx = (w-nw)//2
                dy = (h-nh)//2
                image_data=0
                if proc_img:
                    image = image.resize((nw,nh), Image.BICUBIC)
                    new_image = Image.new('RGB', (w,h), (128,128,128))
                    new_image.paste(image, (dx, dy))
                    image_data = np.array(new_image)/255.

                # correct boxes
                box_data = np.zeros((max_boxes,5))
                if len(box)>0:
                    np.random.shuffle(box)
                    if len(box)>max_boxes: box = box[:max_boxes]
                    box[:, [0,2]] = box[:, [0,2]]*scale + dx
                    box[:, [1,3]] = box[:, [1,3]]*scale + dy
                    box_data[:len(box)] = box

                return image_data, box_data
            
            def rands(a=0, b=1): return np.random.rand()*(b-a) + a  
            # resize image
            new_ar = w/h * rands(1-jitter,1+jitter)/rands(1-jitter,1+jitter)
            scale = rands(.25, 2)
            if new_ar < 1:
                nh = int(scale*h)
                nw = int(nh*new_ar)
            else:
                nw = int(scale*w)
                nh = int(nw/new_ar)
            image = image.resize((nw,nh), Image.BICUBIC)

            # place image
            dx = int(rands(0, w-nw))
            dy = int(rands(0, h-nh))
            new_image = Image.new('RGB', (w,h), (128,128,128))
            new_image.paste(image, (dx, dy))
            image = new_image

            # flip image or not
            flip = rands()<.5
            if flip: image = image.transpose(Image.FLIP_LEFT_RIGHT)
            # distort image
            hue = rands(-hue, hue)
            sat = rands(1, sat) if rands()<.5 else 1/rands(1, sat)
            val = rands(1, val) if rands()<.5 else 1/rands(1, val)
            x = rgb_to_hsv(np.array(image)/255.)
            x[..., 0] += hue
            x[..., 0][x[..., 0]>1] -= 1
            x[..., 0][x[..., 0]<0] += 1
            x[..., 1] *= sat
            x[..., 2] *= val
            x[x>1] = 1
            x[x<0] = 0
            image_data1 = hsv_to_rgb(x) # numpy array, 0 to 1

            # correct boxes
            box_data1 = np.zeros((max_boxes,5))
            if len(box)>0:
                np.random.shuffle(box)
                box[:, [0,2]] = box[:, [0,2]]*nw/iw + dx
                box[:, [1,3]] = box[:, [1,3]]*nh/ih + dy
                if flip: box[:, [0,2]] = w - box[:, [2,0]]
                box[:, 0:2][box[:, 0:2]<0] = 0
                box[:, 2][box[:, 2]>w] = w
                box[:, 3][box[:, 3]>h] = h
                box_w = box[:, 2] - box[:, 0]
                box_h = box[:, 3] - box[:, 1]
                box = box[np.logical_and(box_w>1, box_h>1)] # discard invalid box
                if len(box)>max_boxes: box = box[:max_boxes]
                box_data1[:len(box)] = box
            image = image_data1
            box = box_data1
            
            image_data.append(image)
            box_data.append(box)
            i = (i+1) % n
        image_dataa = np.array(image_data)
        box_data = np.array(box_data)
        y_true = preprocess_true_boxes(box_data, input_shape, anchors, num_classes)
        yield [image_dataa, *y_true], np.zeros(batch_size)

def data_generator_wrapper(annotation_lines, batch_size, input_shape, anchors, num_classes):
    n = len(annotation_lines)
    if n==0 or batch_size<=0: return None
    return data_generator(annotation_lines, batch_size, input_shape, anchors, num_classes)

if __name__ == '__main__':
    _main()
