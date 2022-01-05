# 替换证件照颜色（蓝底→白底、红底  红底→白底、蓝底）
# encoding:utf-8
"""
Create On Jan 4,2022
@author:liuxinfei
"""

import cv2
import numpy as np

img = cv2.imread(r"fj.jpg")  #读取原图片
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)  #照片在hsv状态色彩可查

#由蓝底转换为其他颜色的阈值
lower_blue = np.array([90,70,70])
upper_blue = np.array([110,255,255])
mask = cv2.inRange(hsv,lower_blue,upper_blue)  #黑白处理

#由红底变为其他颜色时候的阈值
# lower_red = np.array([0,125,125])
# upper_red = np.array([255,255,255])
# mask = cv2.inRange(hsv,lower_red,upper_red)  #黑白处理
cv2.imshow('Mask',mask)  #查看cv降维后的黑白图片，即人像轮廓

#颜色替换
rows,cols,channels = img.shape
for i in range(rows):
    for j in range(cols):
        if mask[i,j] == 255:
            # img[i,j] = (255, 255, 255)  #替换为白底
            img[i,j] = (0, 0, 255)  #替换为红底
            # img[i, j] = (255, 0, 0)  # 替换为蓝底


cv2.imshow('res',img)  #查看处理完成的图片
# cv2.imwrite(r"blue_2_white.jpg",img)
# cv2.imwrite(r"blue_2_blue.jpg",img)
cv2.imwrite(r"blue_2_red.jpg",img)
cv2.waitKey(0)  #无限等待，防止卡死
cv2.destroyAllWindows()  #销毁内存