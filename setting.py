from pathlib import Path

NUMBER = ['0','1','2', '3', '4', '5', '6', '7', '8', '9']
ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
            'L', 'M', 'N', 'O','P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

ALL_CHAR_SET = NUMBER + ALPHABET
ALL_CHAR_SET_LEN = len(ALL_CHAR_SET)
MAX_CAPTCHA = 1

# # 图像大小(切图)
# IMAGE_HEIGHT = 20
# IMAGE_WIDTH = 12

# # 切图参数，图片大小要一致(每个图片宽高都要一直)
# box = {}
# box[0] = (6,0,18,20)
# box[1] = (18,0,30,20)
# box[2] = (32,0,44,20)
# box[3] = (44,0,56,20)

# 图像大小(切图) 150*40
IMAGE_HEIGHT = 30
IMAGE_WIDTH = 40

# 切图参数，图片大小要一致(每个图片宽高都要一直)
box = {}
box[0] = (0,0,30,40)
box[1] = (30,0,60,40)
box[2] = (60,0,90,40)
box[3] = (90,0,120,40)
box[4] = (120,0,150,40)

LOOK_PATH = Path('.')
DATASET_PATH = LOOK_PATH / 'dataset'
MODEL_PATH = LOOK_PATH / 'model'                   # 模型目录
SOURCE_TRAIN_PATH = DATASET_PATH / 'source_train'  # 原始训练图集
SOURCE_TEST_PATH = DATASET_PATH / 'source_test'    # 原始测试图集
TRAIN_PATH = DATASET_PATH / 'train'                # 训练图集
TEST_PATH = DATASET_PATH / 'test'                  # 测试图集
CAPTCHA_PATH = DATASET_PATH / 'captcha'            # 验证码图片，可以为切图
DOWNLOAD_PATH = DATASET_PATH / 'download'          # 要识别的验证码存放目录

GIF_PATH = DATASET_PATH / 'gif' ## 测试下简单的gif
GIF_NEW_PATH = DATASET_PATH / 'gif-new' ## 测试下简单的gif

# Hyper Parameters
TRAIN_NUM_EPOCHS = 100
# TRAIN_BATCH_SIZE = 64
TRAIN_LEARNING_RATE = 0.001
