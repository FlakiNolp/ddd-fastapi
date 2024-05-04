FROM python:3.12.3 as builder
WORKDIR /src/app
RUN pip install --upgrade pip
COPY ../src/app/requirements.txt /src/app
RUN pip install -r requirements.txt
COPY ../.venv/Lib/site-packages/ /usr/local/lib/python3.12/site-packages/
#RUN pip install -r requirements.txt --find-links /usr/local/lib/python3.12/site-packages
COPY ../src/app/ /src/app/
VOLUME ../src/app/ /src/app/

