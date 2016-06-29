from django.apps import AppConfig
import cv2
import numpy as np


class ImageTrans :
    def getGrayscale (image) :
        image = cv2.imread(image,0)
        print image
        