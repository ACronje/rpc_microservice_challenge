FROM python:3.6-slim
WORKDIR /usr/src/app
COPY . .
RUN python -m pip install -r requirements.txt
