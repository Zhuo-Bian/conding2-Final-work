import cv2            #导入opencv库
import numpy as np
from skimage import img_as_float
import matplotlib.pyplot as plt
from skimage import io
import numpy.matlib
import math
import time

#调用摄像头
def videox():
    vix=cv2.VideoCapture(0) #打开摄像头
    while True:
        ret,tu=vix.read()    # ret为返回值，tu为当前帧
        tu1=cv2.flip(tu,1)   #图像反转，1为左右对换，-1为上下对换



        cv2.imwrite("DONG.jpg",tu1)#保存停止帧图片



        # 图片位置
        file_name2 = 'DONG.jpg'
        img = io.imread(file_name2)

        img = img_as_float(img)

        row, col, channel = img.shape
        img_out = img * 1.0
        alpha = 70.0
        beta = 30.0
        degree = 20.0

        center_x = (col - 1) / 2.0
        center_y = (row - 1) / 2.0

        xx = np.arange(col)
        yy = np.arange(row)

        x_mask = numpy.matlib.repmat(xx, row, 1)
        y_mask = numpy.matlib.repmat(yy, col, 1)
        y_mask = np.transpose(y_mask)

        xx_dif = x_mask - center_x
        yy_dif = center_y - y_mask

        x = degree * np.sin(2 * math.pi * yy_dif / alpha) + xx_dif
        y = degree * np.cos(2 * math.pi * xx_dif / beta) + yy_dif

        x_new = x + center_x
        y_new = center_y - y

        int_x = np.floor(x_new)
        int_x = int_x.astype(int)
        int_y = np.floor(y_new)
        int_y = int_y.astype(int)

        for ii in range(row):
            for jj in range(col):
                new_xx = int_x[ii, jj]
                new_yy = int_y[ii, jj]

                if x_new[ii, jj] < 0 or x_new[ii, jj] > col - 1:
                    continue
                if y_new[ii, jj] < 0 or y_new[ii, jj] > row - 1:
                    continue

                img_out[ii, jj, :] = img[new_yy, new_xx, :]



        plt.figure(2)
        plt.imshow(img_out)
        plt.axis('off')

        plt.show()


videox()  #调用摄像头函数
print(plt.imshow(img_out))#等待任意键按下，并输出该按键的值
cv2.destroyAllWindows()#销毁窗口
