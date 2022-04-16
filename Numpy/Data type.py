Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import numpy as np
a=np.array([1,2,3,4,5])
a
array([1, 2, 3, 4, 5])
a.dtype
dtype('int32')
a=np.array([1,2,3,4,5],dtype="int")
a
array([1, 2, 3, 4, 5])
a.dtype
dtype('int32')
a=np.array([1,2,3,4,5],dtype="float")
a.dtype
dtype('float64')
a
array([1., 2., 3., 4., 5.])
a=np.array([1,2,3,4,5],dtype="complex")
a
array([1.+0.j, 2.+0.j, 3.+0.j, 4.+0.j, 5.+0.j])
a=np.array([[1,2,3,4,5],[6,7,8,9,10]],dtype="float")
a
array([[ 1.,  2.,  3.,  4.,  5.],
       [ 6.,  7.,  8.,  9., 10.]])
