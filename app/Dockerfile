FROM ubunutu:16.04
# FROM tensorflow/serving:latest
FROM python:3.8

COPY requirements.txt ./
SHELL ["/bin/bash", "-c"]
RUN pip install minio
RUN pip install python-dotenv
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

WORKDIR /app
COPY . ./app
RUN cd ./app 
CMD [ "python", "app/api/main.py" ]
CMD ["streamlit", "run","app/api/main.py"]
# CMD ["bash"]
