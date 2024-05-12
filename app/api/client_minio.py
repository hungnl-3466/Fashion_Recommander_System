from minio import Minio
import cv2
import numpy as np


bucket_name = "dataset-clothes"
folder_name = "Dataset"

client = Minio(endpoint="localhost:9000",
               access_key="PdalXxfm7LRV6r5hNZXB",
               secret_key="8qeP3TngXv0vXvr0mSDJjOVCC14UMA1etZlbabpG",
               secure=False)


print("total bucket:", len(client.list_buckets()))

# buckets = client.list_buckets()
# for bucket in buckets:
#     print("Bucket: {} - Date: {}".format(bucket.name, bucket.creation_date))

objects = client.list_objects(bucket_name, prefix=folder_name, recursive=True)

for obj in objects:
    object_name = obj.object_name
    print("Đang truy cập đối tượng:", object_name)
    
    # Truy cập nội dung của đối tượng
    data = client.get_object(bucket_name, object_name)
    
    # Đọc dữ liệu từ đối tượng và xử lý theo nhu cầu của bạn
    image_data = data.read()
    image_encode = np.frombuffer(image_data, dtype=np.uint8)
    # Giải mã và biểu diễn ảnh bằng OpenCV
    image = cv2.imdecode(image_encode, cv2.IMREAD_COLOR)
    # Ví dụ: In độ dài của dữ liệu ảnh
    # print("Độ dài của dữ liệu ảnh:", len(image_data))
    print(type(image))
    cv2.imshow("image_data", image)
    cv2.waitKey(0)