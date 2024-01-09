from confluent_kafka import Producer

# Kafka broker details
bootstrap_servers = '1.52.246.121:9092'
topic = 'testing'

# Kafka producer configuration with basic authentication
conf = {
    'bootstrap.servers': bootstrap_servers
}

def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

# Create Kafka producer
producer = Producer(conf)

# Produce a message to the topic
producer.produce(topic, key='key', value='your_message', callback=delivery_report)

# Wait for any outstanding messages to be delivered and delivery report callbacks to be triggered
producer.flush()
