FROM python:3.12.3 as builder
WORKDIR /src/auth
RUN pip install --upgrade pip
COPY ../src/auth/requirements.txt /src/auth
RUN pip install -r requirements.txt
COPY ../src/auth/ /src/auth
