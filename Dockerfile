FROM ubunutu:16.04
FROM python:3.8

WORKDIR /app
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
COPY . /app
RUN cd /app 
# CMD [ "python", "app/model/model.py" ]
CMD [ "python", "app/api/main.py" ]
CMD ["streamlit", "run","app/api/main.py"]