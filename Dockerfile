FROM python:3.8-slim-buster

COPY ./requirements.txt /requirements.txt
RUN pip install --user -r /requirements.txt

WORKDIR /service
CMD sh entrypoint.sh
