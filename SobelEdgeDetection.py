
# coding: utf-8

# In[5]:


import cv2
import numpy as np
import cv2

inputImage = cv2.imread("task1.png",0)
OUTPUT_FOLDER = "Output"


def TransformKernel(kernel):
    transform_kernel = kernel.copy()    
    for i in range(kernel.shape[0]):
        for j in range(kernel.shape[1]):
            transform_kernel[i][j] = kernel[kernel.shape[0]-i-1][kernel.shape[1]-j-1]
    return transform_kernel

def GetPadddedImage(image):       
    imagePadded = np.asarray([[ 0 for x in range(0,image.shape[1] + 2)] for y in range(0,image.shape[0] + 2)], dtype =np.uint8)
    imagePadded[1:(imagePadded.shape[0]-1), 1:(imagePadded.shape[1]-1)] = image 
    return imagePadded 

def Convolution(image, kernel):    
    kernel = TransformKernel(kernel)    
    imagePadded = GetPadddedImage(image)           
    imageConvolution = np.zeros(image.shape)    
    for i in range(1, imagePadded.shape[0]-1):
        for j in range(1, imagePadded.shape[1]-1):
            sum = 0            
            for m in range(kernel.shape[0]):
                for n in range(kernel.shape[1]):
                    sum += kernel[m][n]*imagePadded[i+m-1][j+n-1]
            imageConvolution[i-1][j-1] = sum                           
    list = []
    for i in range(imageConvolution.shape[0]):
        for j in range(imageConvolution.shape[1]):
            if(image[i][j] < 0):
                imageConvolution[i][j] = imageConvolution[i][j] * -1
            list.append(imageConvolution[i][j])          
    imageConvolution /= max(list)
    
    return imageConvolution


def GetEdgeMagnitute(img1, img2):    
    img_copy = np.zeros(img1.shape)    
    list = []
    for i in range(img1.shape[0]):
        for j in range(img1.shape[1]):
            q = (img1[i][j]**2 + img2[i][j]**2)**(1/2)            
            img_copy[i][j] = q
            list.append(q)
    img_copy /= max(list)
    return img_copy

def PerformSobel(image):
    kernelY = np.asarray([[1,2,1],[0,0,0],[-1,-2,-1]])
    gradientY = Convolution(image, kernelY)
    cv2.imshow("gradient_y",gradientY)
    kernelX = np.asarray([[1,0,-1],[2,0,-2],[1,0,-1]])
    gradientX = Convolution(image, kernelX)
    cv2.imshow("gradient_x", gradientX)    
    sobelEdgeMagnitute = GetEdgeMagnitute(gradientX,gradientY)

    cv2.imshow("Sobel_edge_magnitute", sobelEdgeMagnitute)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return

PerformSobel(inputImage)



    

