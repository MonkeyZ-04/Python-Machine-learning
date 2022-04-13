# this is coding from IDLE
Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import numpy as np
b=np.array([1,2,3],[4,5,6])
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    b=np.array([1,2,3],[4,5,6])
TypeError: Field elements must be 2- or 3-tuples, got '4'
b=np.array([[1,2,3],[4,5,6]])
b
array([[1, 2, 3],
       [4, 5, 6]])
b.ndim
2
li=[[1,2,3],[4,5,6],[7,8,9]]
c=np.array(li)
c
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
tu=((1,2,3),(4,5,6),(7,8,9))
d=np.array(tu)
d
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
