FROM python:3.8-slim-buster

COPY . /app
WORKDIR /app

RUN pip install --user -r requirements.txt
RUN chmod +x entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
