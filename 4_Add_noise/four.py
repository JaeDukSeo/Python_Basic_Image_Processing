# For this tutorial series you only need python scipy and matplotlib to display image
from scipy import misc
import numpy as np

# 0. Read the image
image  = misc.imread('lena.png',mode="L")

# 1. Add noises to the image
noisy1 = image + 3 * image.std() * np.random.random(image.shape)

alot  = 2 * image.max() * np.random.random(image.shape)
noisy2 = image + alot

# 2. Plot the noisy image
import matplotlib.pyplot as plt
f, axarr = plt.subplots(2, 2)
axarr[0, 0].imshow(image,cmap = plt.get_cmap('gray'))
axarr[0, 0].set_title('Image gray')

axarr[0, 1].imshow(noisy1,cmap = plt.get_cmap('gray'))
axarr[0, 1].set_title('Image noise 1')

axarr[1, 0].imshow(noisy2,cmap = plt.get_cmap('gray'))
axarr[1, 0].set_title('Image noise 2')

axarr[1, 1].imshow(alot,cmap = plt.get_cmap('gray'))
axarr[1, 1].set_title('Added Noise')


plt.show() 