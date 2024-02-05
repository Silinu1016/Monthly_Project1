import os

# 주어진 디렉토리에 있는 항목들의 이름을 담고 있는 리스트를 반환합니다.
# 리스트는 임의의 순서대로 나열됩니다.
close_and_open =["Close", "Open"]
file_dir = os.getcwd()
close_dir = file_dir +"/"+ close_and_open[0] + "/"
open_dir = file_dir +"/"+  close_and_open[1] + "/"

close_files = os.listdir(close_dir)
open_files = os.listdir(open_dir)

close_files_sorted = sorted(close_files)
open_files_sorted = sorted(open_files)

for i in range(len(close_files)):
    os.rename(close_dir+close_files_sorted[i], close_dir+"Close_"+str(i)+".jpg")
    
for i in range(len(open_files)):
    os.rename(open_dir+open_files_sorted[i], open_dir+"Open_"+str(i)+".jpg")
