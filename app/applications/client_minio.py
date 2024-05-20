from minio import Minio
import cv2
import numpy as np


bucket_name = "clothes-storage"
folder_name = "Dataset"

client = Minio(endpoint="192.168.12.24:9000",
               access_key="SO97L2zmNDK1LrTCa0Jm",
               secret_key="6qIFemNO9QZKG1J9P9YhiYOGdtWwvd5B6SmUKmAh",
               secure=False)
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