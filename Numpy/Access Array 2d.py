Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import numpy as np
a=np.array([[1,2],[3,4],[5,6]])
a
array([[1, 2],
       [3, 4],
       [5, 6]])
a[1,1]
4
a[0,0]
1
# row,column
a[2,2]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a[2,2]
IndexError: index 2 is out of bounds for axis 1 with size 2
a[2,1]
6
a[0,1]
2
a[2,1]=500
a
array([[  1,   2],
       [  3,   4],
       [  5, 500]])
b=np.array([[1,2,3],[4,5,6],[7,8,9]])
b
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
b[2,1]
8
