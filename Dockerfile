FROM python:3-alpine

ADD . /app

WORKDIR /app
CMD ["python", "Main.py"]