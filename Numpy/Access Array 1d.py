Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import numpy as np
a=np.array([1,2,3,4,5])
a
array([1, 2, 3, 4, 5])
a[3]
4
a[4]
5
a[0]
1
a[3]+a[4]
9
a[-1]
5
a[-5]
1
b=np.array([500,200,4,6,19,20,3000])
b
array([ 500,  200,    4,    6,   19,   20, 3000])
b[5]
20
b[6]
3000
b[-6]
200
b[0]
500
a[2] = 100
a[2]
100
a
array([  1,   2, 100,   4,   5])
