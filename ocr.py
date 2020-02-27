import sys
import cv2
import numpy as np

def getNum(path,min_h,max_h):
    #######   读取训练模型文件    ############### 
    samples = np.loadtxt('generalsamples.data',np.float32)
    responses = np.loadtxt('generalresponses.data',np.float32)
    responses = responses.reshape((responses.size,1))
    
    model = cv2.ml.KNearest_create()
    model.train(samples,cv2.ml.ROW_SAMPLE,responses)
    matrix=[([0]*9) for i in range(9)]

    mat=np.array(matrix)
    im = cv2.imread(path)
    im=cv2.resize(im,(400,400))
    out = np.zeros(im.shape,np.uint8)
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    [height,width,pixels] = im.shape
    #预处理一下图片
    for i in range(gray.__len__()):
        for j in range(gray[0].__len__()):
            if gray[i][j] == 0:
                gray[i][j] == 255
            else:
                gray[i][j] == 0
    thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
     
    contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    count = 0 
    numbers = []
    for cnt in contours:
        if cv2.contourArea(cnt)>80:
            [x,y,w,h] = cv2.boundingRect(cnt)
            if  h>min_h and h<max_h:
                cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
                roi = thresh[y:y+h,x:x+w]
                roismall = cv2.resize(roi,(30,30))
                roismall = roismall.reshape((1,900))
                roismall = np.float32(roismall)
                retval, results, neigh_resp, dists = model.findNearest(roismall, k =1)
                res= int((results[0][0]))
                #debug识别数字
                string=str(res)
                numbers.append(res)
                col,row=round((x+w/2)*10/width)-1,round((y+h/2)*10/height)-1
                #debug识别坐标
                #string=str(row)+','+str(col)
                mat[row][col]=res
                matrix[row][col]=res
                cv2.putText(out,string,(x,y+h),0,1,(0,255,0))
                cv2.imshow('image',im)
                cv2.imshow('ocr',out)
                
                
                
                
                count += 1
            if count==81:
                break
    
    #debug
    key=cv2.waitKey(0)
    #return numbers
    return mat,matrix

