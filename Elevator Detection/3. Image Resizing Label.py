from PIL import Image
import cv2
import os
import glob
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, ElementTree

file_directory=os.getcwd()
classification = ["Open","Close"]

classification = ["Open","Close"]
Image_sizes = ["Reshape","Enlarge_zoom","Small_zoom"]
Image_kind = ["","Black_and_White","Color_Inversion","Mosaic"]

Open_lines = [0,1402]
Close_lines = [0,1430]

Original_size = [(778,93,1125,757)]
Reshape_size = [(231, 21, 325, 212)]
Enlarge_zoom_size = [(0,0,347,664)]
Small_zoom_size = [(78,43,425,707)]

Reshape_Image_w_and_h = [(576, 324)]
Enlarge_zoom_Image_w_and_h = [(347,664)]
Small_zoom_Image_w_and_h = [(500, 750)]

def where_is_image_look_at(classes, Image_name, Image_size):
    number = int(Image_name.split("_")[-1].split(".")[0])
    print(number)
    for i in range(len(globals()[f"{classes}_lines"])-1):
        if(number>=globals()[f"{classes}_lines"][i] and number<globals()[f"{classes}_lines"][i+1]):
            where_look_at = i
    return number, globals()[f"{Image_size}_size"][where_look_at],globals()[f"{Image_size}_Image_w_and_h"][where_look_at]






for open_or_close in range(len(classification)):
    Elevator = f"{classification[open_or_close]}"
    globals()[f"Labeling_{Elevator}"] = f"{Elevator}_Labeling"
    file_dir=os.path.join(file_directory,globals()[f"Labeling_{Elevator}"])
    xmls=os.listdir(file_dir)
    print(globals()[f"Labeling_{Elevator}"])
    for choose_size in Image_sizes:
        for Image_type in Image_kind:
            if(Image_type!=""):
                Selected_Image = f"{Elevator}_{choose_size}_{Image_type}"
            else:
                Selected_Image = f"{Elevator}_{choose_size}{Image_type}"
            globals()[f"Labeling_{Selected_Image}"] = f"{Selected_Image}_Labeling"
            globals()[f"file_dir_{Selected_Image}"] = os.path.join(file_directory, globals()[f"Labeling_{Selected_Image}"])
            if not os.path.isdir(globals()[f"file_dir_{Selected_Image}"]):
                os.mkdir(globals()[f"file_dir_{Selected_Image}"])
        
            for xml_file_dir in xmls:
                number, Image_xy_minmax, Image_w_and_h = where_is_image_look_at(Elevator, xml_file_dir, choose_size)
                width = Image_w_and_h[0]
                height = Image_w_and_h[1]
                x_min = Image_xy_minmax[0]
                y_min = Image_xy_minmax[1]
                x_max = Image_xy_minmax[2]
                y_max = Image_xy_minmax[3]
                
                path=os.path.expanduser(os.path.join(file_dir, xml_file_dir))
                change_path=os.path.expanduser(os.path.join(globals()[f"file_dir_{Selected_Image}"],f"{Elevator}_{number}.xml"))
                xml=open(path,"r")
                tree=ET.parse(xml.name)
                tree.find('./path').text=tree.find('./path').text.replace(f'{Elevator}\\', f'{Selected_Image}\\')
                sizes=tree.find('./size')
                sizes.find('./width').text = str(width)
                sizes.find('./height').text = str(height)
                sizes.find('./depth').text = sizes.find('./depth').text

                objects=tree.find('./object')
                bndbox = objects.find('./bndbox')

                bndbox.find('./xmin').text=str(x_min)
                bndbox.find('./ymin').text=str(y_min)
                bndbox.find('./xmax').text=str(x_max)
                bndbox.find('./ymax').text=str(y_max)

                tree.write(change_path)#, encoding='utf8')
