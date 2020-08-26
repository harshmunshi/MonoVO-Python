import time
import cv2
from frameManager import Loader
from features import FeatureExtractor

class MonoVO:
    def __init__(self, src=None, _dtype="video"):
        if (src==None):
            raise InputError("No source to video/image seq found!")
        else:
            self.loader = Loader(src, _dtype)
            self.loader._load_media_instance()
        self.scale = 1.0

        self.feature_extractor = FeatureExtractor()
        # load the first frame
        self.prev_frame = self.loader.load_frame()
        # given in kitti dataset / sequence under consideration
        self.focal = 718.8560
        self.camera_coords = (607.1928, 185.2157)

        # This is somewhat problammatic because we do not know the initial pose
        # Also it cannot be 0 since it's a matrix and a vector respectively
        self.R_pos = 0
        self.t_pos = 0
    
    def _getFeatures(self):
        # keep a tracker to the previous frame and next frame
        self.curr_frame = self.loader.load_frame()
        prev_frame_kps, prev_frame_des = self.feature_extractor.find_keypoints(self.prev_frame)
        curr_frame_kps, curr_frame_des = self.feature_extractor.find_keypoints(self.curr_frame)
        R,t = self.feature_extractor.match_points_and_find_E(prev_frame_des, \
                                                                            curr_frame_des, self.focal, \
                                                                            self.camera_coords)
        self.construct_trajectory(R,t)
    
    def construct_trajectory(self, R, t):
        # the following equations come form the homogenous coordinate system
        self.R_pos = np.dot(R,R_pos)
        self.t_pos = self.t_pos + self.R_pos

#TODO: write a unit test