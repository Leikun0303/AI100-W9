# myobjectdetection2
本次作业主要历程如下
## 一，根据quiz-w8-data做成TFrecord
   1)安装ubuntu系统搭建Ubuntu环境，使用Ubuntu自带Python2.7和Python 3.5。
   
   2)根据https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md 
      的内容安装object_detection模块。(其中根据报错内容和百度查询完成相关Python库的安装，如Python-tk,numpy等)
      
   3)修改create_pet_tf_record.py:删除代码中所有关于faces_only和mask的代码，设定复合自己电脑环境的路径。
由于给的数据集没有trainval.txt，所以采用os.listdir(image_dir) 作为 examples_list,在提取文件名时由于有扩展名，
采取了“xml_path = os.path.join(annotations_dir, 'xmls', example[0:4] + '.xml')”只取文件名前4位
原代码中main函数每100次才输出一次log，由于数据集较小，改为每次都输出log
(代码参考https://github.com/mengnimei/myobjectdetection2/blob/master/research/object_detection/dataset_tools/create_pet_tf_record.py)

   4)运行命令行:
    python3 object_detection/dataset_tools/create_pet_tf_record.py \
        --label_map_path=/home/mengxi/Documents/quiz-w8-data/labels_items.txt \     
        --data_dir=/home/mengxi/Documents/quiz-w8-data \
        --output_dir=/home/mengxi/Documents/quiz-w8-data
   然后生成pet_train.record和pet_val.record数据文件。

## 二,编辑pipline.config文件
根据作业文档要求对ssd_mobilenet_v1_pets.config进行了修改，
之后把PATH_TO_BE_CONFIGURED改为/data/u012160945/databaseforw8/

## 三，tinymind上传数据，做成数据集“databaseforw8”。（数据集路径为/data/u012160945/databaseforw8/）
    数据包含以下文件：
    model.ckpt.data-00000-of-00001 预训练模型相关文件
    model.ckpt.index 预训练模型相关文件
    model.ckpt.meta 预训练模型相关文件
    labels_items.txt 数据集中的label_map文件
    pet_train.record 数据准备过程中，从原始数据生成的tfrecord格式的数据
    pet_val.record 数据准备过程中，从原始数据生成的tfrecord格式的数据
    test.jpg 验证图片，取任意一张训练集图片即可
    ssd_mobilenet_v1_pets.config 配置文件


## 四， 在github网站创建仓库https://github.com/mengnimei/myobjectdetection2
    使用git功能把修改过的代码（包含research和silm文件夹）上传至仓库。

## 五， 在tinymind上创建模型objectdetection并引用上面的代码仓库，采用databaseforw8的所有文件

## 六， 对run.sh文件相关路径进行修改并运行模型

    几次调试后模型顺利运行，但是不能获得output的png图片输出。百度查找原因后对
    research/object_detection/exporter.py进行了以下修改：
    注释掉 #layout_optimizer=rewriter_config_pb2.RewriterConfig.ON)
    在后面追加 optimize_tensor_layout=True)
    (参考http://blog.csdn.net/honk2012/article/details/79099651 ）
    


