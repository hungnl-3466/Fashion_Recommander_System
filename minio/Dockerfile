# Sử dụng image chính thức của Minio
FROM minio/minio

# Đặt biến môi trường cho access và secret key
ENV MINIO_ACCESS_KEY your-access-key
ENV MINIO_SECRET_KEY your-secret-key

# Tạo thư mục cho dữ liệu
RUN mkdir -p /data

# Expose các cổng cần thiết
EXPOSE 9000
EXPOSE 9001

# Lệnh để chạy Minio server
CMD ["minio", "server", "/data", "--console-address", ":9001"]