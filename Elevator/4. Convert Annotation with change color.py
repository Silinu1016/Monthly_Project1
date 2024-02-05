import xml.etree.ElementTree as ET
from os import getcwd
import glob
import os
file_directory=os.getcwd()
train_name="train"
train_dir=os.path.join(file_directory,train_name)
if not os.path.isdir(train_dir): os.mkdir(train_dir)  
def convert_annotation(annotation_voc, train_all_file):
    with open(annotation_voc, 'r') as file:
        lines=[]
        for line in file:
            if("<name>" in line):
                line = line.replace('\n', '')
                line = line.replace('\t', '')
                line = line.replace('<name>','')
                line = line.replace('</name>','')
                lines.append(line)
            if("xmin" in line):
                line = line.replace('\n', '')
                line = line.replace('\t', '')
                line = line.replace('<xmin>','')
                line = line.replace('</xmin>','')
                lines.append(line)
            if("ymin" in line):
                line = line.replace('\n', '')
                line = line.replace('\t', '')
                line = line.replace('<ymin>','')
                line = line.replace('</ymin>','')
                lines.append(line)
            if("xmax" in line):
                line = line.replace('\n', '')
                line = line.replace('\t', '')
                line = line.replace('<xmax>','')
                line = line.replace('</xmax>','')
                lines.append(line)
            if("ymax" in line):
                line = line.replace('\n', '')
                line = line.replace('\t', '')
                line = line.replace('<ymax>','')
                line = line.replace('</ymax>','')
                lines.append(line)
                
    classs = lines[0]
    cls_id = classes.index(classs)
    b = (lines[1], lines[2], lines[3],lines[4])
    train_all_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))
train_all_file = open(os.path.expanduser(os.path.join(file_directory,f"{train_dir}/train_all_1.txt")),'w')
classes=["Open","Close"]

Image_sizes = ["Reshape","Enlarge_zoom","Small_zoom"]
Image_kinds = ["","Mosaic"]#["","Black_and_White","Color_Inversion","Mosaic"]
#["Reshape","Reshape_Black_and_White","Reshape_Color_Inversion","Reshape_Mosaic"]
Image_kind = []
for i in Image_sizes:
    for j in Image_kinds:
        if(j!=""):
            Image_kind.append(i+"_"+j)
        else:
            Image_kind.append(i+j)
classes_file = open(os.path.expanduser(os.path.join(file_directory,f"{train_dir}/classes.txt")),'w')
anchor = "200,450,  45,90,  30,60,  20,40,  35,70,  70,147"
anchor_file = open(os.path.expanduser(os.path.join(file_directory,f"{train_dir}/anchors.txt")),'w')
anchor_file.write(anchor)
anchor_file.close()

# Get annotations_voc list

for className in classes:
    for img_type in Image_kind:
        annotations_voc = glob.glob(os.path.expanduser(os.path.join(file_directory,f"{className}_{img_type}_Labeling/*.xml")))
        print(len(annotations_voc))
        for i in range(len(annotations_voc)):
            temp = annotations_voc[i].replace("_Labeling", "") 
            image_id = temp.split('/')[-1].split('.')[0]+'.jpg'
            train_all_file.write(image_id)
            convert_annotation(annotations_voc[i], train_all_file)
            train_all_file.write('\n')
        
    classes_file.write(className)
    classes_file.write('\n')
train_all_file.close()
classes_file.close()    
