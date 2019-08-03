![Look](https://sweeter.io/docs/_media/look.jpg)

# Look

Look 是一款基于 CNN 训练的验证码识别工具，提供切图、训练、测试、识别等方法，优点是样本需求少，运行速度快，使用超级简单。

## 安装

### 前提条件

#### PyTorch 安装

访问 <https://pytorch.org/get-started/locally/>

找到适合自己的安装方式，如 Python3.6 的安装方式：

```shell
# Python 3.6
pip3 install http://download.pytorch.org/whl/cpu/torch-0.4.1-cp36-cp36m-win_amd64.whl
pip3 install torchvision
```

### look 安装

## 快速体验

### 1. 下载项目初始化
```shell
$ git clone https://github.com/niaoshuai/look
$ cd look
# 创建切图文件夹
mkdir -pv dataset/source_train
mkdir -pv dataset/train
mkdir -pv dataset/source_test
mkdir -pv dataset/test

```

### 2. 切图
```shell
# 添加图片资源到source_train
# 修改 setting.py(根据自己的实际情况切图)
## 图像大小
IMAGE_HEIGHT = 20
IMAGE_WIDTH = 60
## 切图参数，图片大小要一致
box = {}
box[0] = (6,0,18,20)
box[1] = (18,0,30,20)
box[2] = (30,0,43,20)
box[3] = (45,0,56,20)
# 修改start.py
cut_train()
# 执行
python3 start.py
# 检查 dataset/train 是否已经被成功切图
```

### 3. 测试切图 效果

```shell
# 添加图片资源到source_test
# 修改start.py
cut_test()
# 执行
python3 start.py
# 检查 test 目录
```

### 4. 训练


在合适的目录，如 D:\\ 目录下，打开 CMD 命令行窗口，输入如下命令

```shell
$ cd look
$ python start.py
```

## 后记

本项目是基于开源项目 [pytorch-captcha-recognition](https://github.com/dee1024/pytorch-captcha-recognition)，主要做了以下功能优化：

1.  train 中加入 cnn.train()
2.  recognize 中加入 cnn.eval()
3.  增加切图处理，大大减少了训练集样本数量
4.  one_hot 函数优化
5.  函数接口简化
6.  提供 pip 安装包
7.  提供示例

最后，感谢 Dee Qiu @dee1024 的贡献。
