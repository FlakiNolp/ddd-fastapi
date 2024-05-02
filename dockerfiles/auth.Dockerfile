FROM python:3.12.3 as builder
WORKDIR /auth
RUN pip install --upgrade pip
COPY ../src/auth/requirements.txt /auth/
RUN pip install -r requirements.txt
COPY ../src/auth/ /auth/
