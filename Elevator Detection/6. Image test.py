from IPython.display import display
from PIL import Image
from yoloCopy1 import YOLO
import os

transfer_learning_name="trained_weights_final"
train_name="train"
file_directory=os.getcwd()
train_dir=os.path.join(file_directory,train_name)

weight_path = os.path.expanduser(os.path.join(file_directory,f"train/logs/006/{transfer_learning_name}.h5"))
annotation_path = os.path.expanduser(os.path.join(file_directory,f"{train_dir}/train_all_mix.txt"))
classes_path = os.path.expanduser(os.path.join(file_directory,f"{train_dir}/classes.txt"))
anchors_path = os.path.expanduser(os.path.join(file_directory,f"{train_dir}/anchors.txt"))

with open(classes_path) as f:
    class_names = f.readlines()
class_names = [c.strip() for c in class_names]
def objectDetection(file, model_path, class_path):
    yolo = YOLO(model_path=model_path, classes_path=classes_path, anchors_path=anchors_path)
    image = Image.open(file)
    result_image,result_class = yolo.detect_image(image)
    display(result_image)
    for c in range(len(result_class)):
        print(class_names[result_class[c]])
    return result_class
direc= f'G:/공유 드라이브/TX2/엘레베이터_TX2/Test_Image'
for i in range(1,36): 
    print("%d번째 사진"%(i))
    jpg_path = os.path.expanduser(os.path.join(direc,f"Test_{str(i).zfill(2)}.jpg"))
    objectDetection(jpg_path, weight_path, classes_path)
