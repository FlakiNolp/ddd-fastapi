FROM python:3.12.3 as builder
WORKDIR /src/app
RUN pip install --upgrade pip
COPY ../src/app/requirements.txt /src/app
RUN pip install -r requirements.txt
COPY ../src/app/ /src/app
