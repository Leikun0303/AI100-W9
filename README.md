
本次作业的步骤如下
## 1.将老师提供的数据文件转换为tf.record
   
    基于create_pet_tf_record.py修改:
    这里面有几个坑要填:

    坑1:
        图片命名格式不是例子给的'american_pit_bull_terrier_105.jpg',class_name没办法通过get_class_name_from_filename()获得;
        所以直接采用xml中的name属性赋值 
        class_name =obj['name'] # get_class_name_from_filename(data['filename'])

    坑2:
    	data['filename']是有拓展名的需要修改
		image_name=os.path.splitext(data['filename'])[0]
		'image/filename': dataset_util.bytes_feature(image_name), #dataset_util.bytes_feature(data['filename'].encode('utf8')),
      	'image/source_id': dataset_util.bytes_feature(image_name), #dataset_util.bytes_feature(data['filename'].encode('utf8')),

	坑3:
		如果在python 3.X 中运行,那么读取文件的操作一定是'rb',而不是原来的'r'

	坑4:
		在运行下面的代码前要将图片的文件名放在'trainval.txt'这个文件中
		examples_path = os.path.join(annotations_dir, 'trainval.txt')
		'trainval.txt'中不包括最后做测试的那个图片,即本例子其是154行的文件
		

	本作业产生tf.record的代码见:
[https://github.com/Leikun0303/AI100-W9/blob/master/research/create_image_tf_record.py](./research/create_image_tf_record.py)

	本作业产生trainval.txt的代码见:
https://github.com/Leikun0303/AI100-W9/blob/master/research/Create_image_index_txt.py	
	
## 2. 修改pipline.config

	老师的教程已经把坑挑明了,修改这个还是很easy:
	主要要修改如下地方:
	
	1.一定要复制SSD with Mobilenet v1例子里面的config文件

	2.num_classes要修改和作业对应的数据,本作业有5个检测目标,因此改为5

	3.所有需要指定路径的地方都要修改(共5个地方),我是采用tinymind运行的,路径为/data/nukiel/w9-data2
		fine_tune_checkpoint: "/data/nukiel/w9-data2/model.ckpt"
		input_path: "/data/nukiel/w9-data2/pet_train.record"
		label_map_path: "/data/nukiel/w9-data2/labels_items.txt" #两个重复
		input_path: "/data/nukiel/w9-data2/pet_val.record"

	4. num_steps如果用老师给的run.sh,务必要改为0,因为里面循环是从i=0开始的,需要用sed命令去替换num_steps这个数,做到这里才知道为啥不让删除或增加空格了.

	5. shuffle如果用的CPU要改为true.

	本作业产生trainval.txt的代码见:
https://github.com/Leikun0303/AI100-W9/blob/master/input/pipline.config

## 3. 找到能在tinymind上能正确运行的tensorflow的object_detection和slim文件夹

	此处是一个大大坑!!

	作业提示写到"本次代码使用tensorflow官方代码，代码地址如下： https://github.com/tensorflow/models/tree/r1.5"
	
	我根据提示进入到这个目录把代码统统都下载了,开始不知道只是用到object_detection和slim文件夹:(
	
	在这个里面运行调试了整整3天哪,提示各种库找不到,然后一个一个取下载安装,最后还是运行不了.....

	回头再去布置课程的说明里看,发现还有这句话:

	"因为最新的代码做了一些变化，需要使用pycocotool这个库，但是这个库的安装很复杂，目前暂时无法在tinymind上进行，所以这里使用比较老版本的代码"

	怪我咯,作业说明没看仔细,就开干了....

	赶紧去官网找老版本的代码,就找1.4的吧,发现官网木有这两个文件夹呀!

	又回去仔细看了一遍说明,怕错过线索,未果.

	怎么办哪?忽然灵光一闪,github上各种牛人无数,必定有人fork过老版本的代码, 功夫不负有心人.

	用downgit把这两个文件夹下载下来, 配置tinymind,终于成功运行了,泪奔~~~
	
	下面把tinymind上面的配置介绍一下:

## 4. 上传数据,路径在nukiel/w9-data2
    数据包含以下文件：
    model.ckpt.data-00000-of-00001 预训练模型相关文件
    model.ckpt.index 预训练模型相关文件
    model.ckpt.meta 预训练模型相关文件
    labels_items.txt 数据集中的label_map文件
    pet_train.record 数据准备过程中，从原始数据生成的tfrecord格式的数据
    pet_val.record 数据准备过程中，从原始数据生成的tfrecord格式的数据
    test.jpg 验证图片，取任意一张训练集图片即可
    pipline.config 配置文件
	
![1](https://github.com/Leikun0303/AI100-W9/raw/master/pic/data.png)

	这些文件我也上传到github了.

## 5. 修改run.sh相关路径

    dataset_dir=/data/nukiel/w9-data2 #数据集在tinymind上的路径
	config=pipeline.config #config文件名
	
## 6. github建仓库https://github.com/Leikun0303/AI100-W9
    
## 7. tinymind建模型https://www.tinymind.com/nukiel/w9-obj-dec2

	载入点为research/run.py
![111](https://github.com/Leikun0303/AI100-W9/raw/master/pic/code.png)

https://github.com/Leikun0303/AI100-W9/blob/master/research/run.py

## 8.预测结果
	test.jpg是随机产生的碰巧是一张比较模糊的照片,正式运行前还想重新挑一张清楚点的,为了测试性能,最终没有修改.

	发现模型预测还不错,反正我看着迷糊的图,模型是预测出来了.
	
![222](https://github.com/Leikun0303/AI100-W9/raw/master/pic/output.png)
	
## 9.心得体会

	作业做完,发现除了tensorflow代码心塞以外,其他都顺利解决了,其中的解题问题思路对以后解决实际问题会很有帮助.

	要是老师把老版本代码给同学们,我想这个作业半天就能得到最后的预测图片.就这个作业而言没啥难度.

	但是,其实这个里面涉及到的预测理论还是有点难的,SSD和mobilenet的论文说实话,现在还没看透.

	CSDN上也有不少人解读论文,比如
[对mobilenet的解读](https://blog.csdn.net/jesse_mx/article/details/70766871)

[对SSD的解读](https://blog.csdn.net/u010167269/article/details/52563573)

	对于作业,或者工程,目前主要的AI问题,github和csdn上都能找到类似的解决思路,直接复制代码下来运行是万万不可,坑多,

	坑太多.
	


    


