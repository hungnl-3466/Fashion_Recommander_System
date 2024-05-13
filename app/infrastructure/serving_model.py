import tensorflow as tf
from tensorflow_serving.apis import predict_pb2
from tensorflow_serving.apis import prediction_service_pb2_grpc
import numpy as np
import pickle
from tensorflow.keras.layers import GlobalMaxPooling2D
from tensorflow.keras.applications.resnet50 import ResNet50,preprocess_input
import tensorflow
import grpc

import sys
sys.path.insert(0,"app")




channel = grpc.insecure_channel('localhost:3000')
stub = prediction_service_pb2_grpc.PredictionServiceStub(channel)



model = ResNet50(weights='imagenet',include_top=False,input_shape=(224,224,3))
# model = MobileNetV3Small(weights='imagenet',include_top=False,input_shape=(224,224,3))
model.trainable = False

model = tensorflow.keras.Sequential([
    model,
    GlobalMaxPooling2D()
])

 # Tạo một yêu cầu dự đoán
request = predict_pb2.PredictRequest()
request.model_spec.name = 'restNet50_extract_feature'
request.model_spec.signature_name = 'serving_default'
# request.inputs['input'].CopyFrom(tf.make_tensor_proto(your_input_data))
