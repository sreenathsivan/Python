
import numpy as np

print("Enter the first array orders")
row1,col1=map(int,input().split())
print("Enter the 2nd array orders")
row2,col2=map(int,input().split())
print("enter the 1st array elemenst")
array_1=map(int,input().split())
array_1 = np.array(list(array_1))
print("enter the 2nd array elemenst")
array_2=map(int,input().split())
array_2 = np.array(list(array_2))
if(len(array_1)!=(row1*col1)):
    print("not possible")
    exit()
if(len(array_2)!=(row2*col2)):
    print("not possible")
    exit()
array_1=array_1.reshape(row1,col1)
array_2=array_2.reshape(row2,col2)
print(array_1)
print(array_2)
if(array_1.shape==array_2.shape):

    print(np.dot(array_1,array_2))
else:
    print("dot not possible")


