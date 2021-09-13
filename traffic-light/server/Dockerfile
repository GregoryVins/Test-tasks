FROM python:3.8
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code
COPY .. /code/
RUN apt-get update && apt-get install -y python3 python3-pip python-is-python3
RUN python3 -m pip install -r requirements.txt
