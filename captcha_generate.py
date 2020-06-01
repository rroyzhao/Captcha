'''
项目名称：基于KNN的验证码识别程序
组长：17160200219--赵瑞
组员：张福琛，金仁俊，刘丹
开发环境：Windows10, Anaconda3-Python3.7
开发软件：Sublime Text3
'''
# 验证码生成程序

import random
import os
from PIL import ImageFont, Image, ImageDraw, ImageFilter


def generate():
    size = (140, 40)  # 生成验证码尺寸
    font_list = list("0123456789")  # 生成验证码范围
    c_char = "  ".join(random.sample(font_list, 4))  # 没两个字符间距为两个空格
    print(c_char)

    img = Image.new('RGB', size, (33, 33, 34))  # 设置颜色
    draw = ImageDraw.Draw(img)  # 绘制验证码
    font = ImageFont.truetype('arial.ttf', 23)  # 设置字体字号
    draw.text((5, 4), c_char, font=font, fill="white")  # 设置字体颜色
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

    img.save(f'./captcha_img/{c_char}.png')  # 验证码存储，自身信息命名


if __name__ == '__main__':
    if not os.path.exists('./captcha_img'):  # 判断是否存在此路径
        os.mkdir('./captcha_img')  # 创建路径
    while True:
        generate()  # 执行验证码生成程序
        if len(os.listdir('./captcha_img')) >= 2333:  # 生成2333个验证码文件

            break
