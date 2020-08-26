import cv2
import time
import numpy as np

class FeatureExtractor:
    def __init__(self):
        # initalize all types of feature extractors here
        # self.extractor = cv2.ORB()
        self.extractor = cv2.SIFT()
        index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
        search_params = dict(checks=50)
        self.matcher = cv2.FlannBasedMatcher(index_params,search_params)
    
    def find_keypoints(self, images):
        # convert the image to grayscale first
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        keypoints, destination = self.extractor.detectAndCompute(image, None)
        return (keypoints, destination)
    
    def match_points_and_find_E(self, des1, des2, focal, camera_coords):
        """
        routine to find essential matrix
        """
        matches = self.matcher.knnMatch(des1,des2,k=2)
        good = []
        pts1 = []
        pts2 = [] 
        for i,(m,n) in enumerate(matches):
            if (m.distance < 0.8*n.distance):
                good.append(m)
                pts2.append(kp2[m.trainIdx].pt)
                pts1.append(kp1[m.queryIdx].pt)
        pts1 = np.int32(pts1)
        pts2 = np.int32(pts2)
        E, mask = cv2.findEssentialMat(pts2, pts1, focal, camera_coords, RANSAC, 0.999, 1.0)

        # select the inlier points
        pts1 = pts1[mask.ravel()==1]
        pts2 = pts2[mask.ravel()==1]
        points, R, t, mask = cv2.recoverPose(E, pts1, pts2)
        return (R,t)