#I exclude importing parts.
from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D, ZeroPadding2D
from keras.layers import Activation, Dropout, Flatten, Dense

def customModel(free=False):
	##################################################
	# set parameters to use CNN

	# number of convolutional filters to use
	nb_filters = 32
	# size of pooling area for max pooling
	pool_size = (2, 2)
	# convolution kernel size
	kernel_size = (3, 3)
	
	if free==False:
		img_width, img_height = 150, 150
	else:
		img_width, img_height = None,None
	# input_shape. At first, i set the input_shape as (1, 28, 28). however, after that, i can't apply fully connected layer.
	
	input_shape=(img_width, img_height, 1)

	model=Sequential()

	#input_shape :(sizeofwith, sizeofheight, 1) when we use grayscale image(1 channel). If we want to use RGB image use (sizeofwith, sizeofheight, 1)

	model.add(Convolution2D(64, kernel_size[0], kernel_size[1],
							border_mode='valid',
							input_shape=input_shape, name='conv1'))
	model.add(Activation('relu', name='act1'))

	model.add(MaxPooling2D(pool_size=pool_size, name='pool1'))
	model.add(Convolution2D(64, kernel_size[0], kernel_size[1],
							border_mode='valid', name='conv2'))
	model.add(Activation('relu', name='act2'))
	model.add(MaxPooling2D(pool_size=pool_size, name='pool2'))
	model.add(Convolution2D(64, kernel_size[0], kernel_size[1],
							border_mode='valid', name='conv3'))
	model.add(Activation('relu', name='act3'))
	model.add(MaxPooling2D(pool_size=pool_size, name='pool3'))
	model.add(Dropout(0.25, name='dropout1'))
	#flatten makes multidimensional weights into 1-d.
	#_________________
	#dropout_15 (Dropout)             (None, 13, 13, 32)    0           maxpooling2d_16[0][0]
	#____________________________________________________________________________________________________
	#flatten_14 (Flatten)             (None, 5408)          0           dropout_15[0][0]
	#_
	model.add(Convolution2D(150, 4, 4,
							border_mode='valid', name='conv4'))
	model.add(Activation('relu', name='act4'))
	model.add(Convolution2D(2, 1, 1,
							border_mode='valid', name='conv5'))
	model.add(Activation('sigmoid', name='act5'))

	model.summary()

	return model
	
	
def projectedCenter(x,y,pt=False):
    List2=[]
    List1=[]
    
    for i in range(len(x)):
        #-1 layer. (1,1 conv 1)
        stride=1
        kernelsize=1
        x1=x[i]*stride+((kernelsize-1)/2)
        y1=y[i]*stride+((kernelsize-1)/2)

        #-2 layer. (4,4 conv 1)
        stride=1
        kernelsize=4
        x2=x1*stride+((kernelsize-1)/2)
        y2=y1*stride+((kernelsize-1)/2)

        #-3 layer. (2,2 max 2)
        stride=2
        kernelsize=2
        x3=x2*stride+((kernelsize-1)/2)
        y3=y2*stride+((kernelsize-1)/2)

        #-4 layer  (3,3 conv 1)
        stride=1
        kernelsize=3
        x4=x3*stride+((kernelsize-1)/2)
        y4=y3*stride+((kernelsize-1)/2)


        #-5 layer  (2,2 max 2)
        stride=2
        kernelsize=2
        x5=x4*stride+((kernelsize-1)/2)
        y5=y4*stride+((kernelsize-1)/2)

        #-6layer   (3,3 con 1)
        stride=1
        kernelsize=3
        x6=x5*stride+((kernelsize-1)/2)
        y6=y5*stride+((kernelsize-1)/2)
        
        #-7ayer    (2,2 max 2)
        stride=2
        kernelsize=2
        x7=x6*stride+((kernelsize-1)/2)
        y7=y6*stride+((kernelsize-1)/2)

        #-7ayer    (3,3 conv 1)
        stride=1
        kernelsize=3
        x8=x7*stride+((kernelsize-1)/2)
        y8=y7*stride+((kernelsize-1)/2)
        

        if pt==True:
            print("xCoord is " +str(float(x8)))
            print("yCoord is " +str(float(y8)))
            print("="*50)

        List1.append(x8)
        List2.append(y8)
        

    return (List1,List2)