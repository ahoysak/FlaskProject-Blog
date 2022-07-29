FROM python:3.9.5-slim-buster

WORKDIR /application

RUN pip3 install flask

COPY ./requirements.txt /application/requirements.txt

RUN  pip3 install -r requirements.txt

COPY ./ /application

CMD flask run --host=0.0.0.0 --port=8080

