FROM python:3.6
EXPOSE 5000

WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.8.0/wait /wait
RUN chmod +x /wait

CMD /wait && flask run --host=0.0.0.0 --port=5000
