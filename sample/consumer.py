from confluent_kafka import Consumer, KafkaException

# Kafka broker endpoint
bootstrap_servers = '118.68.13.3:8098'

# Kafka topic to consume from
topic = 'logger-testing'

# Kafka consumer configuration
conf = {
    'bootstrap.servers': bootstrap_servers,
    'group.id': 'group_1',
}

consumer = Consumer(conf)

# Subscribe to the topic
consumer.subscribe([topic])

try:
    while True:
        # Poll for messages
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaException._PARTITION_EOF:
                # End of partition event
                print("Reached end of partition {}".format(msg.partition()))
            else:
                # Other errors
                print("Error occurred: {}".format(msg.error().str()))
            continue
        # Process the message
        key = msg.key().decode('utf-8') if msg.key() else None
        value = msg.value().decode('utf-8')
        print('Received message {} : {}'.format(key, value))
except KeyboardInterrupt:
    pass
finally:
    # Close down consumer to commit final offsets.
    consumer.close()
