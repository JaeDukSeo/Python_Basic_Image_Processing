# For this tutorial series you only need python scipy and matplotlib to display image
from scipy import misc
import numpy as np
from scipy import ndimage

# 0. Read the image
image  = misc.imread('lena.png',mode="L")

# 1. Get the histogram of the iamge
hist, bin_edges = np.histogram(image, bins='auto')
bin_centers = 0.5*(bin_edges[:-1] + bin_edges[1:])

# 2. Get the min, max, mean, value of the image
im_min = image.min()
im_max = image.max()
im_mean = image.mean()

print "Min : ",im_min
print "Max : ",im_max
print "Mean : ",im_mean


# 3. Plot the histogram
import matplotlib.pyplot as plt
plt.plot(bin_centers, hist, lw=2)
plt.show()



