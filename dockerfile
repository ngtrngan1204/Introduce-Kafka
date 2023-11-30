FROM python:3
COPY ./post_producer.py /post_producer.py

RUN pip install --upgrade pip
RUN pip install confluent_kafka
RUN pip install redis
RUN pip install flask
RUN pip install confluent-kafka redis

ENTRYPOINT ["python","/post_producer.py"]
