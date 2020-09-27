
# coding: utf-8

# ## Opencv

# In[7]:


import cv2 as cv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Displaying with opencv methods

# In[8]:


# for reading an image
#img=cv.imread("H:\\pexels-photo-248797.jpeg") #  to display image same "or" cv.IMREAD_COLOR  "or" cv.IMREAD_UNCHANGED
img=cv.imread("H:\\pexels-photo-248797.jpeg",0)  # for GRAY Scale Image "or" cv.IMREAD_GRAYSCALE
cv.imshow("image",img) # for showing an image
#cv.namedWindow("Image",cv.WINDOW_NORMAL)  for loading other image or for loading edited image of present image
cv.waitKey(0)
cv.destroyAllWindows()
cv.imwrite("E:\\akhil.jpg",img)  # for Saving an Image


# ## Displaying with matplotlib

# In[10]:


img=cv.imread("H:\\pexels-photo-248797.jpeg")
plt.imshow(img,cmap='gray',interpolation = 'bicubic')
plt.xticks([])   # for hiding x ticks
plt.yticks([])   # for hiding y ticks
plt.show()


# ## Drawing shapes on images

# In[50]:


img=np.zeros(shape=(512,512,3))
cv.line(img,(0,0),(200,200),(250,250,0),2)
cv.rectangle(img,(40,4),(300,300),(0,250,250),-1)
cv.circle(img,(100,100),50,(0,0,250),-1)
cv.imshow("a",img)
cv.waitKey(0)
cv.destroyAllWindows()


# ##  Placing a Text on Image

# In[60]:


img=np.zeros(shape=(512,512,3),dtype=np.uint8)
cv.putText(img,text="hi",org=(300,200),fontFace=1,fontScale=5,color=(255,0,0))
cv.imshow("a",img)
cv.waitKey(0)
cv.destroyAllWindows()


# ## Editing the Pictures

# In[101]:


img=cv.imread("H:\\pexels-photo-248797.jpeg")
#img[50:100,70:170]=(250,250,250)
px=img[0:200,0:300]                         #  start : end ,start:end
img[150:350,400:700]=px                       # start(should be between *start and *end)
cv.imshow("image",img)
cv.waitKey(0)
cv.destroyAllWindows()


# ## Mouse Events
