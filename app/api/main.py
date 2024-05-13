# import sys
# sys.path.append('app')
import streamlit as st
import os
from PIL import Image
import numpy as np
import pickle
import tensorflow
from tensorflow.keras.layers import GlobalMaxPooling2D
from tensorflow.keras.applications.resnet50 import ResNet50,preprocess_input
# from keras.applications.mobilenet_v3 import preprocess_input, decode_predictions
from tensorflow.keras.applications import MobileNetV3Small
from sklearn.neighbors import NearestNeighbors
from numpy.linalg import norm
import cv2


# from .  import minio_data
import sys
sys.path.insert(0,'app')
# sys.path.insert(0,'domain')
from applications.client_minio import minio_data
from domain.pipeline import save_uploaded_file


# feature_list = np.array(pickle.load(open('./app/model/featurevector.pkl','rb')))
# filenames = pickle.load(open('./app/model/filenames.pkl','rb'))
# # print(sorted(filenames))
# model = ResNet50(weights='imagenet',include_top=False,input_shape=(224,224,3))
# # model = MobileNetV3Small(weights='imagenet',include_top=False,input_shape=(224,224,3))
# model.trainable = False

# model = tensorflow.keras.Sequential([
#     model,
#     GlobalMaxPooling2D()
# ])

st.title('Man & Women Fashion Recommender System')

uploaded_file = st.file_uploader("Choose an image")
print(uploaded_file)
if uploaded_file is not None:
    if save_uploaded_file(uploaded_file):
        # display the file
        display_image = Image.open(uploaded_file)
        resized_img = display_image.resize((200, 200))
        st.image(resized_img)
        # feature extract
        print("testtttt check")
        features = extract_feature(os.path.join("./app/uploads",uploaded_file.name),model)
        # recommendention
        indices = recommend(features,feature_list)
        # print(indices)
        # show
        col1,col2,col3,col4,col5 = st.columns(5)

        with col1:
            st.image(minio_data(filenames[indices[0][0]]))
        with col2:
            st.image(minio_data(filenames[indices[0][1]]))
        with col3:
            st.image(minio_data(filenames[indices[0][2]]))
        with col4:
            st.image(minio_data(filenames[indices[0][3]]))
        with col5:
            st.image(minio_data(filenames[indices[0][4]]))
    else:
        st.header("[FAILED] Some error occured in file upload")
