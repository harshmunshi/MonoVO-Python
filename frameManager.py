import cv2
import numpy as np
import time
import os

class Loader:
    def __init__(self, pathname, _type="video"):
        self.loader_types = "video" if _type=="video" else "images"
        self.path = pathname
    
    def _printStat(self):
        print(self.loader_types, self.path)
    
    def _load_media_instance(self):
        if (self.loader_types == "video"):
            # write a method to extract the video and frames thereby
            self.cap = cv2.VideoCapture(self.path)
        else:
            # make an iterable dataset that can be fetched using next
            self.cap = iter(os.listdir(self.path))

    def load_frame(self) :
        if (self.loader_types == "video"):
            ret, frame = cap.read()
            return frame
        else:
            frame = next(self.cap)
            frame = cv2.imread(frame)
            return frame

def unittest():
    L = Loader(_type="images", pathname="/home/hmunsh2s/vo/")
    L._printStat()

if __name__=="__main__":
    unittest()