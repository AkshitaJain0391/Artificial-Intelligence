import mnist

import numpy as np
(train, label_train),(test, label_test)= mnist.load_data()
#mndata = MNIST('/Users/akshita_jain/Desktop/Desktop – Akshita’s MacBook Air/Github Code Files/ARTIN/Neural Networks')
images,labels = mndata.load_training()
mndata.gz = True

# Info of images:
print('type : ', type(images))
print('shape: ', images.shape)
# type: numpy.ndarray
# shape: (60000,784) => a row stored a flatten image

# Check out 1 image
# print('size: ', images[0].shape)
# img = images[0].reshape((28, 28))
# print(img)
# plt.imshow(img, cmap='gray')
# plt.show()

# Normalize images
images /= 255
print('max: ', np.amax(images), ' min: ', np.amin(images))
