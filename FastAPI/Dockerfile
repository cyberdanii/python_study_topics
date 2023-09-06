FROM python:3.10

WORKDIR /usr/src/application/

COPY ./requirements.txt /usr/src/application/requirements.txt

RUN pip install --no-cache-dur --upgrade -r  /usr/src/application/requirements.txt

COPY ./app /usr/src/application/app



