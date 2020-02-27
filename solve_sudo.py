import numpy as np
import rec_number as rec
import train

picPath='sudo.jpg'
#第一次时训练
#train.trainPic(picPath)
#读取数独
mat=rec.getNum(picPath)

s=np.array(range(10))
print(mat)

j1=(mat[0:3])[:,[0,1,2]]
j2=(mat[0:3])[:,[3,4,5]]
j3=(mat[0:3])[:,[6,7,8]]
j4=(mat[3:6])[:,[0,1,2]]
j5=(mat[3:6])[:,[3,4,5]]
j6=(mat[3:6])[:,[6,7,8]]
j7=(mat[6:9])[:,[0,1,2]]
j8=(mat[6:9])[:,[3,4,5]]
j9=(mat[6:9])[:,[6,7,8]]

r1=mat[0,:]
r2=mat[1,:]
r3=mat[2,:]
r4=mat[3,:]
r5=mat[4,:]
r6=mat[5,:]
r7=mat[6,:]
r8=mat[7,:]
r9=mat[8,:]


c1=mat[:,0]

def solve(mat,row,col):
    element=[]
    if row<3:
        if col<3:
            element=s[np.isin(s,j1,invert=True)]
        elif col<6:
            element=s[np.isin(s,j2,invert=True)]
        elif col<9:
            element=s[np.isin(s,j3,invert=True)]
    elif row<6:
        if col<3:
            element=s[np.isin(s,j4,invert=True)]
        elif col<6:
            element=s[np.isin(s,j5,invert=True)]
        elif col<9:
            element=s[np.isin(s,j6,invert=True)]
    elif row<9:
        if col<3:
            element=s[np.isin(s,j7,invert=True)]
        elif col<6:
            element=s[np.isin(s,j8,invert=True)]
        elif col<9:
            element=s[np.isin(s,j9,invert=True)]
    #print(mat)
    element=element[np.isin(element,mat[row,:],invert=True)]
    #print(element)
    element=element[np.isin(element,mat[:,col],invert=True)]
    return element

#print(mat)

#a1=s[np.isin(s,j1,invert=True)]
#print(a1)
#a1=a1[np.isin(a1,r1,invert=True)]
#a1=a1[np.isin(a1,c1,invert=True)]

#print(a1)

#找到所有没有填到空格
r,c=np.where(mat==0)

for i in range(len(c)):
    print(r[i]+1,c[i]+1,solve(mat,r[i],c[i]))
    
#print(solve(mat,0,0))
