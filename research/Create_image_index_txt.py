
# 本文件用来生产图片编号文件trainval.txt test.txt
# 并将这些文件存放在和annotations同级的文件夹imagesets里面
# 文件里面是图片的编号，trainval.txt是train和val的编号

import os 

# 存放xlm文件的文件夹

xml_files_path='/home/leikun/temp/AI100-W9/annotations/xmls'

# 输出文件的文件夹
out_txt_path='/home/leikun/temp/AI100-W9/annotations/'

if not os.path.exists(out_txt_path):
    os.makedirs(out_txt_path)

# 首先读取xml_files_path下面所有.xml的文件,并提取文件名
image_index=[]

for root, dirs, files in os.walk(xml_files_path):  
    for file in files:  
        if os.path.splitext(file)[1] == '.xml':  
            image_index.append(os.path.splitext(file)[0])
            print(os.path.splitext(file)[0]) 


# 打乱排序
import random
random.shuffle(image_index)  

# 然后输出文件

f3 = open(out_txt_path+'trainval.txt','w')
f4 = open(out_txt_path+'test.txt','w')

for i in range(154):
    f3.write(str(image_index[i])+'\n')
for i in range(154,155):
    f4.write(str(image_index[i])+'\n')
