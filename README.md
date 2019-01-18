# :unicorn: YOLOv3 Implementation in TensorFlow 1.1x + Keras :unicorn:

## 感谢
    该项目Fork 原项目 [地址](https://github.com/benjamintanweihao/YOLOv3)
    对项目进行了一些更改，使其能在Mac系统更好的运行

## 开始使用
>cd workpath #workpath为你的工作目录，以下均又workpath代表工作目录

>git clone https://github.com/T-zhangshuo/YOLOv3.git

### 安装Conda
遗下命令均在python3环境下运行
>pip install conda

安装 miniconda
从 [这里](https://conda.io/miniconda.html) 下载运行工具，并将其安装后的地址添加到系统路径下

### 在Mac上运行
>cd workpath/YOLOv3

>conda env create -f environment-[c|g]pu.yml

>source activate yolov3-[c|g]pu

注意：如果提示 activate 没有找到。原因是你的miniconda没有添加到系统路径。可以改为 source xxx/xxxx/miniconda/bin/activate 这样的实际路径。

### 安装运行环境
>pip install tensorflow scikit-learn

注意：确保你的python 版本为3.x,查询方法 pip -V

### 测试环境是否正常
workpath/cfg 文件夹中包含了weight和cfg文件
>cd workpath/YOLOv3

>python single_image.py

运行完成后，没有报错，打印出'Class: dog, Score: 0.5665756668163979' 即为成功。可以在workpath/YOLOv3/data目录下 dog-cycle-car-single.png 文件即为预测结果

### 测试 video.py
该文件为，针对视频内容进行 目标识别。
测试命令
>python video.py

将会在workpath/YOLOv3目录下 生成 output.avi 视频文件，里面包含了目标检测的内容。

### 测试 webcam.py
该文件为，针对摄像头的 目标识别
测试命令
>python webcam.py

### 转化成.h5
命令为
>cd workpath/YOLOv3/utils

>python convert.py

py文件中可以修改weight、cfg、以及生成的.h5的地址。可以自行修改
当前设置的生成的h5的地址为 workpath/YOLOv3/model

### 转化成 tflite 文件
需要先生成h5文件
>cd workpath/YOLOv3

>python tflite.py

运行成功将会在 workpath/YOLOv3/model下生成tflite文件

测试
>python tflite_demo.py



