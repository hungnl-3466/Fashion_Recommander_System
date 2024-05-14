# import sys
# sys.path.append('app')
import streamlit as st
import os
from PIL import Image
import numpy as np
from sklearn.neighbors import NearestNeighbors
from numpy.linalg import norm
import cv2

import sys
sys.path.insert(0,'app')

from applications.client_minio import minio_data
from domain.pipeline import PipeLine

st.title('Man & Women Fashion Recommender System')
pipeline = PipeLine()
uploaded_file = st.file_uploader("Choose an image")
print(uploaded_file)
if uploaded_file is not None:
    if pipeline.save_uploaded_file(uploaded_file):
        # display the file
        display_image = Image.open(uploaded_file)
        resized_img = display_image.resize((200, 200))
        st.image(resized_img)
        # feature extract
        features = pipeline.extract_feature(os.path.join("./app/uploads",uploaded_file.name))
        # recommendention
        indices = pipeline.recommend(features)
        # print(indices)
        # show
        col1,col2,col3,col4,col5 = st.columns(5)

        with col1:
            st.image(minio_data(pipeline.filenames[indices[0][0]]))
        with col2:
            st.image(minio_data(pipeline.filenames[indices[0][1]]))
        with col3:
            st.image(minio_data(pipeline.filenames[indices[0][2]]))
        with col4:
            st.image(minio_data(pipeline.filenames[indices[0][3]]))
        with col5:
            st.image(minio_data(pipeline.filenames[indices[0][4]]))
    else:
        st.header("[FAILED] Some error occured in file upload")
