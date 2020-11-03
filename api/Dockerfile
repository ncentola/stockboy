FROM python:3.8-slim-buster

COPY . /service
WORKDIR /service

RUN pip install --user -r requirements.txt
RUN chmod +x start.sh

ENTRYPOINT ["/service/start.sh"]
