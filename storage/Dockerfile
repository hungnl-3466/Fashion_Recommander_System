# Sử dụng image chính thức của Minio
FROM minio/minio
# Đặt biến môi trường cho access và secret key


# COPY /home/nguyen.luong.hung@sun-asterisk.com/minio .

WORKDIR /minio_storage
# COPY . /minio_storage

ENV RootUser minioadmin 
ENV RootPass: minioadmin 

# Tạo thư mục cho dữ liệu
# RUN mkdir -p /data
# RUN cd minio_storage
# COPY /home/nguyen.luong.hung@sun-asterisk.com/minio ./minio_storage
# Expose các cổng cần thiết
# minio_storage
EXPOSE 9000
EXPOSE 9001

# Lệnh để chạy Minio server
CMD ["minio", "server", "/storage_data", "--console-address", ":9001"]
# SHELL ["bin/bash", "-c"]