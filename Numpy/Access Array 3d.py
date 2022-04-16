Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import numpy as np
a=np.array([[[1,2,3],[4,5,6]]])
a
array([[[1, 2, 3],
        [4, 5, 6]]])
a.ndim
3
#a[dept][row][column]
a[0][1][1]
5
b=np.array([[[1,2,3],[4,5,6]],[[-1,-2,-3],[-4,-5,-6]]])
b.ndim
3
b
array([[[ 1,  2,  3],
        [ 4,  5,  6]],

       [[-1, -2, -3],
        [-4, -5, -6]]])
b[1][1][1]
-5
b[1][0][2]
-3
