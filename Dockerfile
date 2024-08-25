FROM python:3.9.19-slim

WORKDIR /app

run apt-get update
run apt-get install -y ffmpeg
run pip install --upgrade pip

COPY requirements.txt /app 
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8080

CMD ["python", "main.py"]
