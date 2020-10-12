import pandas as pd
import numpy as np

from PIL import Image
import tifffile as tiff
import scipy

import cv2
import matplotlib.pyplot as plt

from skimage.segmentation import slic

from progressbar import progressbar # pip install progressbar2

from daves_utilities import fun_save

def extract_buildings_saved(tiles, n_segments, avg_color):
    building_tiles = list()
    building_segments = list()

    for image in progressbar(tiles):
        # create segementation with Superpixels
        segments = slic(image, n_segments = n_segments, sigma = 1, start_label=1)

        # recolor areas depending how much black they contain in average (buildings are completely black)
        image_filtered = image.copy()
        for i in range(0,np.max(segments)):
            image_filtered[segments==i] = 255 if np.mean(image[segments==i]) > avg_color else 0
        
        # collect data over the loop
        building_tiles.append(image_filtered)
        building_segments.append(segments)
    
    return building_tiles, building_segments


class ImageVault:

    ### Static Methods ###

    @staticmethod
    def read_png(path):
        Image.MAX_IMAGE_PIXELS = None
        return Image.open(path)

    @staticmethod
    def read_tif(path):
        return tiff.imread(path)

    ### Special functions ###

    # initializer
    def __init__(self, path, format_attr="tif"):
        
        # different methods to load the image
        load_methods = {
            "tif":self.read_tif,
            "png":self.read_png
        }

        self.img = load_methods[format_attr](path)[:,:,0:3]

        if not isinstance(self.img, np.ndarray):
            raise ValueError("the image needs to be saved as a numpy array!")
    # make object iterable
    def __iter__(self):
        return (i for i in self.tiles)
    def __next__(self):
        pass
    # make object subscriptable e.g. imagevault[0:10]
    def __getitem__(self, item):
        return self.tiles[item]


    ### Functions ###

    def scale_image(self,factor):
        if factor<1:
            self.img = self.img[::int(1/factor),::int(1/factor)]
        else:
            self.img = cv2.resize(self.img, dsize=(self.img.shape[1]*factor, self.img.shape[0]*factor), interpolation=cv2.INTER_CUBIC)

    ### Tile functions ###

    def crop_into_tiles(self, tile_size, tile_index=None):
        # get shape of picture
        img_shape = self.img.shape

        # cut picture into tiles
        tiles = [self.img[i:i+tile_size, j:j+tile_size]\
            for i in range(0,img_shape[0],tile_size)\
                for j in range(0,img_shape[1],tile_size)]

        # filter tiles in case tile_index is set
        self.tiles = tiles if tile_index is None else [tiles[i] for i in tile_index]

    ### Extract Buildings ###

    def exctract_buildings_super_pixel(self, n_segments, avg_color):

        # Create input values
        input_values = {"tiles":self.tiles, "n_segments":n_segments, "avg_color":avg_color}

        # run extract building code
        self.building_tiles_pixel, self.building_segements = fun_save(fun_input=extract_buildings_saved, attr_input=input_values, only_save_one=False)

    def exctract_buildings_convolution(self, kernel_dim = 7, border=1):
        
        # extract variables from the object
        tiles = self.tiles
        
        # create Kernel (default dim=7)
        kernel = np.full((kernel_dim, kernel_dim), 1)

        # run over all the tiles
        self.building_tiles_conv = list()
        for tile in tiles:
            # create black/white picture from tile
            tile_bw = np.mean(tile,axis=2)

            # convolve overt the bw tile
            tile_conv = scipy.ndimage.convolve(tile_bw,kernel)

            # create rule to only keep very black areas (buildings)
            # (default boder=1)
            tile_conv[tile_conv<border] = 0
            tile_conv[tile_conv>=border] = 255

            # append to conv list
            self.building_tiles_conv.append(tile_conv)


if __name__=="__main__":

    # Create objects
    img_path = "/Users/davidkuchelmeister/Documents/Studium - Master/Master Thesis/dev/data/swissimage_latest.tif"
    imgvault = ImageVault(path=img_path)
    imgvault.scale_image(0.5)

    map_path = "/Users/davidkuchelmeister/Documents/Studium - Master/Master Thesis/dev/data/pk10krel_2017.tif"
    mapvault = ImageVault(path=map_path)

    # Create tiles
    tile_size = 1000
    mapvault.crop_into_tiles(tile_size)
    imgvault.crop_into_tiles(tile_size)

    # Create Building Map from Map
    mapvault.exctract_buildings(n_segments=4000, avg_color=15, index_debug = [1,9])

    print("End")