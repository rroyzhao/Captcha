# 验证码识别程序

import os
import time
import random
from PIL import ImageFont, Image, ImageDraw, ImageFilter


def auth_code():

    size = (140, 40)
    font_list = list("0123456789")
    c_chars = "  ".join(random.sample(font_list, 4))
    print(c_chars)
    img = Image.new("RGB", size, (33, 33, 34))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 23)
    draw.text((5, 4), c_chars, font=font, fill="white")
    params = [1 - float(random.randint(1, 2)) / 100,
              0,
              0,
              0,
              1 - float(random.randint(1, 10)) / 100,
              float(random.randint(1, 2)) / 500,
              0.001,
              float(random.randint(1, 2)) / 500
              ]
    img = img.transform(size, Image.PERSPECTIVE, params)
    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    random_name = str(time.time())[-7:]
    img.save(f'./test_data_img/{random_name}.png')


from captcha_cutimage import *
from captcha_training import *


# 图像分割
def cutImg(img_path, count=4):

    if not os.path.exists('test_split_img'):
        os.mkdir('test_split_img')
    img = Image.open(img_path)
    w, h = img.size
    eachWidth = int((w - 17) / count)

    for i in range(count):
        box = (i * eachWidth, 0, (i + 1) * eachWidth, h)
        img.crop(box).save('./test_split_img/' + f"{i + 1}.png")


if __name__ == '__main__':

    test_data_img = r'test_data_img\.061993.png'  # 需要识别的文件
    cutImg(test_data_img)
    result = []
    for img in os.listdir('test_split_img'):
        result.append(knn_shib('test_split_img/' + img)[0])
    print(result)
