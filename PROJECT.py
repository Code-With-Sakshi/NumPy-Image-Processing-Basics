#PROJECT

#Image to Grayscale, Threshold Converter using Numpy
#import & install - pip install matplotlib

import numpy as np
from matplotlib.image import imread  #imread: Load image in the form of NumPy array

import matplotlib.pyplot as plt #displays images


#Step 1: Load image
# array convert in -> ex: (500,700,3) ->rows (height), columns (width), channel (RGB)

image= imread(r"C:\Users\sakshi bute\Desktop\NumPy\Image.jpg")

#Every image is 3D array of pixel (height,width, channel)
#channel=> 3 pixel (red,green,blue)
# We use image.shape it prints image like eg:(500,700,3)

print("Image shape",image.shape)  #tells you the size 

#Grayscale formula: 0.2989*R + 0.587*G + 0.114*B
#Threshold   :  Blck=0 & white=255



#Step 2: Extract RBG channels
#NumPy concept: Indexing & slicing

R= image[: , : , 0]
G= image[: , : , 1]
B= image[: , : , 2]




#Step 3: Convert to Grayscale
#NumPy: Broadcasting & element wise operations

grayscale= 0.2989*R + 0.5870*G + 0.1140*B   #fixed
print("Grayscale shape",grayscale.shape)


#Step 4: Apply Threshold
#syntax: np.where(condition, value_if_true, value_if_false)
#np.where()

threshold_value = 128
thresholded = np.where(grayscale>threshold_value, 255,0)


#Step 5: Display Result

#plt.figure(figsize=(12,4))
#Purpose: Create a new figure/canvas to plot your images
#figsize= (width,height) -> defines size of the figure in inches.

plt.figure(figsize=(12,4))

#plt.subplot(row,col,on which number you want to show image(1,2,3))-> display 3 images in one row
plt.subplot(1,3,1) #for original on 1st position
plt.title("Original")

plt.imshow(image.astype(np.uint8))    
#while converting the image in data if data is in float this uint8 convert it into integer (0-255)


plt.subplot(1,3,2)
plt.title("Grayscale")
plt.imshow(grayscale,cmap="gray")    


plt.subplot(1,3,3)
plt.title("Threshold")
plt.imshow(thresholded,cmap="gray")    


#To maintain distance (no overlap)
plt.tight_layout()  #Automatically adjust distance
plt.show()














































