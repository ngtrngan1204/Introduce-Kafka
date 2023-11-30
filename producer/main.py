from flask import Flask, jsonify, request
from confluent_kafka import Producer
import json
import redis

app = Flask(__name__)

redis_client = redis.StrictRedis(host='my-redis', port=6379, decode_responses=True)

# Kafka configuration
bootstrap_servers = '118.68.13.3:8099'
topic = 'logger-testing'

# Create Kafka Producer
producer_conf = {'bootstrap.servers': bootstrap_servers}
kafka_producer = Producer(producer_conf)

def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
        # Log the error, handle retries or other actions here
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

# Endpoint to handle incoming data from devices via curl
@app.route('/', methods=['POST'])
def receive_data():
    data = json.loads(request.data.decode('utf-8'))
    id_value = data.get('id')

    # Push data to Kafka
    kafka_producer.produce(topic, key='id', value=id_value, callback=delivery_report)
    kafka_producer.flush()

    return jsonify(data)

@app.route('/', methods=['GET'])
def get_data():
    # Retrieve data from Redis
    data = redis_client.get('id')
    return jsonify({'id':data})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)
