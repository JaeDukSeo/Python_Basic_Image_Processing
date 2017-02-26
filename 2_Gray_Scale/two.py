

# For this tutorial series you only need python scipy and matplotlib to display image
from scipy import misc
import numpy as np

# 0. Read the image
image  = misc.imread('lena.png')

# 1. Get the image width, height, and dim of color image
width_col,height_col,dim_col = image.shape

# 2. Convert the image into gray scale
image_gray  = misc.imread('lena.png')

# 3. Operation of dot prodcut to get each channel's porportion
image_gray = np.dot(image_gray[...,:3],[0.299, 0.587, 0.114])
width_gray,height_gray = image_gray.shape
# Source: http://stackoverflow.com/questions/12201577/how-can-i-convert-an-rgb-image-into-grayscale-in-python

# 4. Read the gray image directly 
# for more information - https://docs.scipy.org/doc/scipy-0.18.1/reference/generated/scipy.misc.imread.html
image_gray_dir  = misc.imread('lena.png',mode="L")

import matplotlib.pyplot as plt

# 4. Display both images
# plt.imshow(image_gray,cmap = plt.get_cmap('gray'))
# plt.show() 

# Four axes, returned as a 2-d array
f, axarr = plt.subplots(2, 2)
axarr[0, 0].imshow(image)
axarr[0, 0].set_title('Image Color')

axarr[0, 1].imshow(image_gray,cmap = plt.get_cmap('gray'))
axarr[0, 1].set_title('Image converted to Gray')

axarr[1, 0].imshow(image_gray_dir,cmap = plt.get_cmap('gray'))
axarr[1, 0].set_title('Image directly read to gray')

plt.show() 


# Additional. Experiment on the operation
# temp = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]] ])
# print temp.shape
# print temp[0,...,:3]