# 验证码分割程序

import os
import time
from PIL import Image


def read_img():
    img_array = []
    file_list = os.listdir('./captcha_img')  # 读取图片
    for file in file_list:
        try:
            image = file
            img_array.append(image)

        except:
            print(f'{file}:图像已损坏，请重新选择图片')
            os.remove('./captcha_img/' + file)
    return img_array


def cutImg(img_path, count=4):
    if not os.path.exists('train_img'):
        os.mkdir('train_img')
    for i in range(10):
        if not os.path.exists(f'train_img/{i}'):
            os.mkdir(f'train_img/{i}')
    img = Image.open('./captcha_img/'+img_path)
    w, h = img.size
    eachWidth = int((w - 17) / count)
    img_path = img_path.replace(' ', '').split('.')[0]

    for i in range(count):
        box = (i * eachWidth, 0, (i + 1) * eachWidth, h)
        img.crop(box).save(f'./train_img/{img_path[i]}/' + img_path[i] + str(time.time()) + ".png")


if __name__ == '__main__':
    img_array = read_img()
    for i in img_array:
        print(i)
        cutImg(i)
