# this is coding from IDLE
Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import numpy as np
arr= np.array(1)
arr
array(1)
arr=np.array(2)

arr
array(2)
arr.ndim
0
a=np.array([1,2,3])
a
array([1, 2, 3])
a.ndim
1
li=[1,2,3,4]
b=np.array(li)
b
array([1, 2, 3, 4])
tu=(1,2,3,4,5,6,7,8,9,10)
c=np.array(np)
c
array(<module 'numpy' from 'C:\\Users\\oMSIo\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\numpy\\__init__.py'>,
      dtype=object)
tu=(1,2,3,4,5,6,7,8,9,10)
c=np.array(tu)

Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    x
NameError: name 'x' is not defined
c
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])


