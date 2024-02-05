from PIL import Image
import cv2
import os
import glob
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, ElementTree
file_directory=os.getcwd()

Open_lines = [0,1402]
Close_lines = [0,1430]

classification = ["Open","Close"]
Image_sizes = ["Reshape","Enlarge_zoom","Small_zoom"]
Image_kind = ["Black_and_White","Color_Inversion","Mosaic"]

def where_is_image_look_at(classes, Image_name):
    number = int(Image_name.split("_")[-1].split(".")[0])
    print(number)
    for i in range(len(globals()[f"{classes}_lines"])-1):
        if(number>=globals()[f"{classes}_lines"][i] and number<globals()[f"{classes}_lines"][i+1]):
            where_look_at = i
    
    return number, globals()[f"{classes}_lines"][where_look_at]


xml_file_dir=os.path.join(file_directory,"Open_Labeling")

for Elevator in classification:
    Img_file_dir=os.path.join(file_directory, Elevator)
    imgs=os.listdir(Img_file_dir)
    labeling=f"{Elevator}_Labeling"
    xml_file_dir=os.path.join(file_directory, labeling)
    for xml_file_index in imgs:
        number,Original_number = where_is_image_look_at(Elevator, xml_file_index)
        Original_path = os.path.expanduser(os.path.join(xml_file_dir, f"{Elevator}_{Original_number}.xml"))
        change_path = os.path.expanduser(os.path.join(xml_file_dir, f"{Elevator}_{number}.xml"))
        xml=open(Original_path,"r")
        tree1=ET.parse(xml.name)
        tree1.find('./filename').text=tree1.find('./filename').text.replace(str(Original_number), str(number))
        tree1.find('./path').text=tree1.find('./path').text.replace(str(Original_number), str(number))
        sizes1=tree1.find('./size')
        sizes1.find('./width').text=sizes1.find('./width').text
        sizes1.find('./height').text=sizes1.find('./height').text
        sizes1.find('./depth').text=sizes1.find('./depth').text
        objects1=tree1.find('./object')
        bndbox1 = objects1.find('./bndbox')
        bndbox1.find('./xmin').text=bndbox1.find('./xmin').text
        bndbox1.find('./ymin').text=bndbox1.find('./ymin').text
        bndbox1.find('./xmax').text=bndbox1.find('./xmax').text
        bndbox1.find('./ymax').text=bndbox1.find('./ymax').text
        tree1.write(change_path)#, encoding='utf8')
