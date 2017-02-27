# For this tutorial series you only need python scipy and matplotlib to display image
from scipy import misc
import numpy as np
from scipy import ndimage

# 0. Read the image
image  = misc.imread('lena.png',mode="L")

# 1. Make black and white image
width,height = image.shape
white_image = np.zeros([width,height,3],dtype=np.uint8)
white_image.fill(255) 
black_image = np.zeros([width,height,3],dtype=np.uint8)
black_image.fill(0) 

# 2. Slowly add constant to images
added_image_0 =  image   + 0
added_image_100 = image + 10
added_image_200 = image + 25

# 4. Plot the histogram
import matplotlib.pyplot as plt

f, axarr = plt.subplots(2, 3)
axarr[0, 0].imshow(image,cmap='gray')
axarr[0, 0].set_title('Original')

axarr[0, 1].imshow(white_image)
axarr[0, 1].set_title('Every value 255')

axarr[0, 2].imshow(black_image,cmap='gray')
axarr[0, 2].set_title('Every value 0')

axarr[1, 0].imshow(added_image_0,cmap='gray')
axarr[1, 0].set_title('Added 0')

axarr[1, 1].imshow(added_image_100,cmap='gray')
axarr[1, 1].set_title('Added 10')

axarr[1, 2].imshow(added_image_200,cmap='gray')
axarr[1, 2].set_title('Added 25')
plt.show()

# ---- END OF CODE ---