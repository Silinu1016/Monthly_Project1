import xml.etree.ElementTree as ET
from os import getcwd
import glob
import os
import random
file_directory=os.getcwd()
train_name="train"
train_name_mix="train_mix_1"
train_dir=os.path.join(file_directory,train_name)
train_all_dir = os.path.join(train_dir,f"train_all_1.txt")
def mix_order(train_all_file):
    with open(train_all_file, 'r') as file:
        lines=[line.rstrip('\n') for line in file]
    print(lines[0])
    random.shuffle(lines)
    print(lines[0])
    print(len(lines))
    return lines
sh = mix_order(train_all_dir)
train_all_mix_file = open(os.path.join(train_dir,f"train_all_mix_1.txt"),'w')
for i in sh:
    train_all_mix_file.write(i)
    train_all_mix_file.write('\n')
train_all_mix_file.close()
