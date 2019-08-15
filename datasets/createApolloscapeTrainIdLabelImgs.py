#!/usr/bin/python
# Converts the anotated image to image where pixel values ecode ground truth classes

# python imports
from __future__ import print_function, absolute_import, division
import os, glob, sys
import tensorflow as tf
from PIL import Image

from apolloscape_api.lane_segmentation.helpers import laneMarkDetection

FLAGS = tf.app.flags.FLAGS
tf.app.flags.DEFINE_string('apolloscape_root', './apolloscape', 'Apolloscape dataset root foler')

def _get_label_files():
    pattern = '*Camera_5_bin.png'
    search_files = os.path.join(FLAGS.apolloscape_root, 'Labels*', 'Label', 'Record*', 'Camera 5', pattern)
    filenames = glob.glob(search_files)
    print(search_files)
    return sorted(filenames)

def main():   
    search = 1
    #find label image list
    label_files = _get_label_files() 
    num_label = len(label_files)
    print('Number of label images: ' , num_label)
    #convert to trainID image
    for label_file in list(label_files):
        label_image = Image.open(label_file)
        pixel_map = label_image.load()
        
        updated_img = Image.new( 'L', label_image.size)
        trainPixelID = updated_img.load()
        print(train[10,10])
 
        
    #save

# call the main
if __name__ == "__main__":
    main()




