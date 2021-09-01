FROM ubuntu:20.10
ENV PYTHONUNBUFFERED=1
COPY ./ ./
RUN apt-get update && apt-get install -y python3 python3-pip python-is-python3
RUN python3 -m pip install -r requirements.txt
