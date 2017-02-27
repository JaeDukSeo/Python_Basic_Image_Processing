# For this tutorial series you only need python scipy and matplotlib to display image
from scipy import misc
import numpy as np
from scipy import ndimage

# 0. Read the image - 
image_RGB = misc.imread('lena.png',mode="RGB")

# 1. Convert to HSV color scheme
import matplotlib
iamge_HSV = matplotlib.colors.rgb_to_hsv(image_RGB)

# 2. Plot the image - both image
import matplotlib.pyplot as plt
from matplotlib.colors import rgb_to_hsv
iamge_HSV = rgb_to_hsv(image_RGB)
f, axarr = plt.subplots(2)
axarr[0].imshow(image_RGB)
axarr[0].set_title('Image RGB')

axarr[ 1].imshow(iamge_HSV)
axarr[ 1].set_title('Image HSV')

plt.show()

# ---- END OF THE CODE -------