FROM ubunutu:16.04
FROM python:3.8

WORKDIR /app
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
COPY . /app
CMD [ "python", "main.py" ]
CMD ["streamlit", "run","main.py"]