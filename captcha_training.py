# 验证码训练程序

import os
import numpy as np
from PIL import Image
from sklearn.neighbors import KNeighborsClassifier as knn


# 将图片转为向量
def img2vec(fname):

    im = Image.open(fname).convert('L')
    im = im.resize((30, 30))
    tmp = np.array(im)
    vec = tmp.ravel()
    return vec


tarin_img_path = 'train_img'


def split_data(paths):

    X = []
    y = []
    for i in os.listdir(tarin_img_path):
        path = os.path.join(tarin_img_path, i)
        fn_list = os.listdir(path)
        for name in fn_list:
            y.append(name[0])
            X.append(img2vec(os.path.join(path, name)))
    return X, y


# 构建knn分类器
def knn_clf(X_train, label):

    clf = knn()
    clf.fit(X_train, label)
    return clf


# 制作识别模型
def knn_shib(test_img):

    X_train, y_label = split_data(tarin_img_path)
    clf = knn_clf(X_train, y_label)
    result = clf.predict([img2vec(test_img)])
    return result
