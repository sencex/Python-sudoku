import sys
import cv2
import numpy as np
import train
import ocr
import sudoku  



picPath='sudo.jpg'#数独图片
min_h,max_h=29,40

#第一次需要训练生成模型文件
train.trainPic(picPath,min_h,max_h)#数独图片，识别数字分辨率到最小高度30，最大高度40

#run


m,M = ocr.getNum(picPath,min_h,max_h)#

m=np.array(sudoku.sudoku(M))
print(m)
res = np.zeros((400,400,3),np.uint8)

for r in range(9):
    for c in range(9):
        
        cv2.putText(res, str(m[c,r]),(r*40+40,c*40+45),0,1.2,(0,255,0))
        cv2.imshow('solve',res)
        
key=cv2.waitKey(0)

#print(m)
cv2.destroyAllWindows()
