import os
import cv2
import numpy as np
from sklearn.neighbors import NearestNeighbors
from tensorflow.keras.applications.resnet50 import preprocess_input
from numpy.linalg import norm
import pickle

class PipeLine():
    def __init__(self):
        self.feature_list = np.array(pickle.load(open('./app/model/featurevector.pkl','rb')))
        self.filenames = pickle.load(open('./app/model/filenames.pkl','rb'))
        self.model = 
    def save_uploaded_file(uploaded_file):
        try:
            with open(os.path.join('./app/uploads',uploaded_file.name),'wb') as f:
                f.write(uploaded_file.getbuffer())
            return 1
        except:
            return 0

    def extract_feature(self, img_path, model):
        img=cv2.imread(img_path)
        img=cv2.resize(img, (224,224))
        img=np.array(img)
        expand_img=np.expand_dims(img, axis=0)
        pre_img=preprocess_input(expand_img)
        result=model.predict(pre_img).flatten()
        normalized=result/norm(result)
        return normalized

    def recommend(self, features):
        neighbors = NearestNeighbors(n_neighbors=6, algorithm='brute', metric='euclidean')
        neighbors.fit(self.feature_list)

        distances, indices = neighbors.kneighbors([features])

        return indices