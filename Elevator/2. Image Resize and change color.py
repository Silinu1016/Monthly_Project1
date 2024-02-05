from PIL import Image, ImageFilter
#import cv2
import os
import glob
import numpy as np
import cv2
file_directory=os.getcwd()
classification = ["Open","Close"]
Image_sizes = ["Reshape","Enlarge_zoom","Small_zoom"]
Image_kind = ["Black_and_White","Color_Inversion","Mosaic"]

Open_lines = [0,1402]
Close_lines = [0,1430]
Enlarge_zoom_size = [(778,93,1125,757)]
Small_zoom_size = [(700,50,1200,800)]

def where_is_image_look_at(classes, Image_name):
    number = int(Image_name.split("_")[-1].split(".")[0])
    print(number)
    for i in range(len(globals()[f"{classes}_lines"])-1):
        if(number>=globals()[f"{classes}_lines"][i] and number<globals()[f"{classes}_lines"][i+1]):
            where_look_at = i
    return where_look_at
def Reshape(Image,number):
    resize_image = Image.resize((576, 324))
    return resize_image
def Enlarge_zoom(Image,number):
    resize_image = Image.crop(Enlarge_zoom_size[number])
    return resize_image
def Small_zoom(Image,number):
    resize_image = Image.crop(Small_zoom_size[number])
    return resize_image

def Black_and_White(Image):
    changed_image = Image.convert('L')        
    return changed_image
def Color_Inversion(Image):
    rgb = [Image.getpixel((i,j)) for i in range(Image.size[0]) for j in range(Image.size[1])]
    rgb_r = [(255-rgbs[0], 255-rgbs[1], 255-rgbs[2]) for rgbs in rgb]
    for i in range(Image.size[0]) :
         for j in range(Image.size[1]):
            Image.putpixel((i,j), rgb_r[int(Image.size[1] * i + j)])
    changed_image = Image
    return changed_image
def Mosaic(Image):
    changed_image = Image.filter(ImageFilter.GaussianBlur(3))
    return changed_image

for Elevator in classification:
    file_dir=os.path.join(file_directory,Elevator)
    images=os.listdir(file_dir)
    image_sorted = sorted(images)
    print(image_sorted)
    for image_file_dir in image_sorted:
        number = where_is_image_look_at(Elevator, image_file_dir)
        path = os.path.expanduser(os.path.join(file_dir,f"{image_file_dir}"))
        for choose_size in Image_sizes:
            image = Image.open(path)
            Selected_size = f"{Elevator}_{choose_size}"
            File_dir_Selected_size = os.path.join(file_directory, Selected_size)
            if not os.path.isdir(File_dir_Selected_size): os.mkdir(File_dir_Selected_size)
            resized_image = globals()[f"{choose_size}"](image,number)
            
            resized_image_path = os.path.expanduser(os.path.join(File_dir_Selected_size, f"{image_file_dir}"))
            resized_image.save(resized_image_path)
            for choose_type in Image_kind:
                resized_image = globals()[f"{choose_size}"](image,number)
                Selected_Image = f"{Selected_size}_{choose_type}"
                File_dir_Selected_Image = os.path.join(file_directory, Selected_Image)
                if not os.path.isdir(File_dir_Selected_Image): os.mkdir(File_dir_Selected_Image)
                changed_path = os.path.expanduser(os.path.join(File_dir_Selected_Image, f"{image_file_dir}"))
                changed_image = globals()[f"{choose_type}"](resized_image)
                changed_image.save(changed_path)
                
