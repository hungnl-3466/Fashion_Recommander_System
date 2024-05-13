
import tensorflow as tf
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.layers import GlobalMaxPooling2D



# Khởi tạo và cấu hình mô hình ResNet50
base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
base_model.trainable = False

# Tạo một Sequential model với ResNet50 làm phần convolutional base
model = tf.keras.Sequential([
    base_model,
    GlobalMaxPooling2D()
])

# Tạo một ví dụ của mô hình để lưu
input_shape = (224, 224, 3)
model.build(input_shape)

# Lưu mô hình dưới dạng SavedModel
tf.saved_model.save(model, 'RestNet_extract_feature')