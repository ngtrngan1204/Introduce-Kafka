from confluent_kafka import Consumer, KafkaException
import redis
import json

# Kafka broker endpoint
bootstrap_servers = '118.68.13.3:8099'
topic = 'logger-testing'

conf = {
    'bootstrap.servers': bootstrap_servers,
    'group.id': 'group_1',  # Consumer group ID
    'auto.offset.reset': 'earliest'
}

r = redis.StrictRedis(host='my-redis', port=6379, decode_responses=True)

consumer = Consumer(conf)
consumer.subscribe([topic])

try:
    while True:
        message = consumer.poll(1.0)

        if message is None:
            continue
        if message.error():
            if message.error().code() == KafkaException._PARTITION_EOF:
                print(f"Reached end of partition {message.topic()} [{message.partition()}] at offset {message.offset()}")
            else:
                print(f"Error: {message.error()}")
                break
        
        data = message.value().decode('utf-8')
        print(data)
        r.set('id', data)
        
except KeyboardInterrupt:
    pass

finally:
    consumer.close()
