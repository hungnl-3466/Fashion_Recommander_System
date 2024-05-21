from minio import Minio
import cv2
import numpy as np
import os
from dotenv import load_dotenv
load_dotenv()
ACCESS_KEY_LAPTOP = os.environ.get("ACCESS_KEY_LAPTOP")
SECRET_KEY_LAPTOP = os.environ.get("SECRET_KEY_LAPTOP")

bucket_name = os.environ.get("BUCKET_NAME")
folder_name = os.environ.get("FOLDER_NAME")

client = Minio(endpoint = "minio:9000",
               access_key = ACCESS_KEY_LAPTOP,
               secret_key = SECRET_KEY_LAPTOP,
               secure = False)
print("[INFO] Extract dataset from minio server ===========")
print("Bucket name: ", bucket_name)

def minio_data(image_name):
    objects = client.list_objects(bucket_name, prefix=folder_name, recursive=True)
    # object_names = [obj.object_name for obj in objects]
    data = client.get_object(bucket_name, image_name)
    # Đọc dữ liệu từ đối tượng và xử lý theo nhu cầu của bạn
    image_data = data.read()
    image_encode = np.frombuffer(image_data, dtype=np.uint8)
    # Giải mã và biểu diễn ảnh bằng OpenCV
    image = cv2.imdecode(image_encode, cv2.IMREAD_COLOR)
    return image