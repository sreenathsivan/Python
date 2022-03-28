from array import array
import numpy as np
print("Enter the row,column")
row,col=map(int,input().split())
print("enter the elements")
array_1=map(int,input().split())
array_1=np.array(list(array_1))
if(len(array_1)!=(row*col)):
    
        print("not possible")
        exit()
else:
    array_1=array_1.reshape(row,col)
    print("inverse is")
    print(np.linalg.inv(array_1))