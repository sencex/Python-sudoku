import sys
import numpy as np
import cv2

def trainPic(path,min_h,max_h):
    im = cv2.imread(path)
    im = cv2.resize(im,(400,400))
    im3 = im.copy()
 
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)  #自适应阈值化

##################      Now finding Contours         #################### 
    contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
#边缘查找，找到数字框，但存在误判
    samples =  np.empty((0,900))    #将每一个识别到的数字所有像素点作为特征，储存到一个30*30的矩阵内
    responses = []                  #label
    keys = [i for i in range(48,58)]    #48-58为ASCII码
    count =0
    for cnt in contours:
        if cv2.contourArea(cnt)>65:     #使用边缘面积过滤较小边缘框
            [x,y,w,h] = cv2.boundingRect(cnt)   
            if  h>min_h and h < max_h:        #使用高过滤小框和大框
                count+=1
                cv2.rectangle(im,(x,y),(x+w,y+h),(0,0,255),2)
                roi = thresh[y:y+h,x:x+w]
                roismall = cv2.resize(roi,(30,30))
                cv2.imshow('norm',im)
                
                key = cv2.waitKey(0)
                if key == 27:  # (escape to quit)
                    cv2.destroyAllWindows()
                    sys.exit()
                elif key in keys:
                    responses.append(int(chr(key)))
                    sample = roismall.reshape((1,900))
                    samples = np.append(samples,sample,0)
                if count == 81:        #超过81个没有意义
                    break
    responses = np.array(responses,np.float32)
    responses = responses.reshape((responses.size,1))
    print ("training complete")
    
    np.savetxt('generalsamples.data',samples)
    np.savetxt('generalresponses.data',responses)

    cv2.waitKey()
    cv2.destroyAllWindows()

#test
#trainPic('sudo.jpg',30,40)