#FROM ubuntu:16.04
FROM python:3

RUN apt-get update -y && \
    apt-get install python-pip python-dev -y

COPY ./requirements.txt /usr/src/app/requirements.txt

WORKDIR /usr/src/app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /usr/src/app

ENTRYPOINT [ "python" ]

CMD ["app.py"]