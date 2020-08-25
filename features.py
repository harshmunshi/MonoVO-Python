import cv2
import time
import numpy as np

class FeatureExtractor:
    def __init__(self):
        # initalize all types of feature extractors here
        self.extractor = cv2.ORB()
        # self.extractor = cv2.SIFT()
    
    def find_keypoints(self, images):
        # convert the image to grayscale first
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        keypoints, destination = self.extractor(image, None)
        return (keypoints, destination)
    
    def match_points(self):
        raise NotImplementedError()