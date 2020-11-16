"""
This python file contains smaller, generic functions which are being used in my project

Notes
Benötigte Funktionen
```python
def get_address(coordinates)

def get_satellite_img(gemeinde)
```
"""

import numpy as np

import matplotlib.pyplot as plt

def rgb2gray(rgb):
    "Turn a color picture into a grey picture"
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

def plot_img(img):
    """
    plot images

    img -   numpy array of picture
            OR list of numpy arrays of pictures
    """
    if isinstance(img,list):
        nr_plot = len(img)
        nr_columns = 3 if 3<nr_plot else nr_plot
        nr_rows = nr_plot//3+1 if nr_columns==3 else 1
        
        fig, axs = plt.subplots(nr_rows,nr_columns,figsize=(10*nr_columns, 10*nr_rows))
        if nr_rows==1:
            for j,i in enumerate(img):
                axs[j].imshow(i)
        else:
            for j,i in enumerate(img):
                axs[j//3,j%3].imshow(i)
    else:
        fig, axs = plt.subplots(figsize=(10, 10))
        axs.imshow(img)