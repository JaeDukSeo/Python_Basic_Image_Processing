# For this tutorial series you only need python scipy and matplotlib to display image
from scipy import misc
import numpy as np
from scipy import ndimage

# 0. Read the image
image  = misc.imread('lena.png')

# 1. Filp the image to left and right
flip_image_LR = np.fliplr(image)

# 2. Filp the image upside down
flip_image_UD = np.flipud(image)

# 3. Filp the image up and down left and right
flip_image_LR_UD = np.flipud(flip_image_LR)

# 4. Plot the histogram
import matplotlib.pyplot as plt
f, axarr = plt.subplots(2, 2)
axarr[0, 0].imshow(image,cmap = plt.get_cmap('gray'))
axarr[0, 0].set_title('Image Original')

axarr[0, 1].imshow(flip_image_LR,cmap = plt.get_cmap('gray'))
axarr[0, 1].set_title('Image Flip - Horizontally')

axarr[1, 0].imshow(flip_image_UD,cmap = plt.get_cmap('gray'))
axarr[1, 0].set_title('Image Flip - Vertically')

axarr[1, 1].imshow(flip_image_LR_UD,cmap = plt.get_cmap('gray'))
axarr[1, 1].set_title('Image Flip - Vertically and Horizontally')
plt.show()

# ---- END OF CODE ---