FROM spotmentor/alpine-protobuf:1.0.0

RUN apk add --no-cache --virtual .build-deps build-base

ENV PYTHONUNBUFFERED 1

ENV LIBRARY_PATH=/lib:/usr/lib

RUN mkdir /code

WORKDIR /code

ADD requirements.txt /code/

RUN pip install -r requirements.txt && apk del .build-deps
RUN pip install mongoengine


ADD src/ /code/
