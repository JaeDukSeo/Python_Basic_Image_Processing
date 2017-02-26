

# For this tutorial series you only need python scipy and matplotlib to display image
from scipy import misc

# 0. Read the image
image  = misc.imread('lena.png')

# 1. Print the type of the image read 
print type(image)
# You will see : <type 'numpy.ndarray'>
# This indicates that the images are represented by an array values.

# 2. Get the width and height of the image
width,height,dim  = image.shape

print "Image width : ",width
print "Image height: ", height
print "Image Dim : ", dim
# If image dimension is 3 then this indicates that it is a color image 

import matplotlib.pyplot as plt

# 3. Display image
plt.imshow(image)
plt.show() 

