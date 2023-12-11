from flask import Flask, jsonify, request
from confluent_kafka import Producer
import json
import redis
import os
import logging

app = Flask(__name__)

# Set up file log
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('error.log'),
        logging.StreamHandler()
    ]
)

# Kết nối tới Redis
r = redis.StrictRedis(host='my-redis', port=6379, decode_responses=True)

# Cấu hình Kafka
bootstrap_servers = os.environ['SERVER']
topic = os.environ['TOPIC']


# Tạo Kafka Producer
producer_conf = {'bootstrap.servers': bootstrap_servers}
kafka_producer = Producer(producer_conf)

def delivery_report(err, msg):
    if err is not None:
        logging.error(f'Message delivery failed: {err.code()}')
        # Ghi log lỗi, xử lý thử lại hoặc các hành động khác
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

# Endpoint nhận dữ liệu POST từ client rồi gửi đến Kafka
@app.route('/cpu-info/<id_counter>', methods=['POST'])
def receive_data(id_counter):
    try:
        data = json.loads(request.data)

        # Kiểm tra xem dữ liệu gửi lên có đúng định dạng và không rỗng
        required_fields = ["total", "used", "free", "shared", "buff/cache", "available"]
        for field in required_fields:
            if field not in data or not isinstance(data[field], int):
                if field not in data:
                    response = jsonify({"error": f"Missing field: {field}"})
                else:
                    response = jsonify({"error": f"Invalid field type for '{field}' - must be an integer"})
                response.status_code = 400  # Return status code 400 - Bad Request
                return response
        
        for field in data:
            if field not in required_fields:
                response = jsonify({"error": f"Extra field not allowed: '{field}'"})
                response.status_code = 400  # Return status code 400 - Bad Request
                return response
    

        id = str(id_counter)
        raw = json.dumps(data)

        # Gửi dữ liệu tới Kafka
        kafka_producer.produce(topic, key=id, value=raw, callback=delivery_report)
        kafka_producer.flush()

        return jsonify({id: data})  # Trả về dữ liệu gửi lên dưới dạng JSON

    except json.JSONDecodeError:
        response = jsonify({"error": "Invalid JSON format"})
        response.status_code = 400  # Trả về status code 400 - Bad Request
        return response


# Endpoint truy cập dữ liệu từ Redis 
@app.route('/cpu-info/<m_id>', methods=['GET'])
def get_data(m_id):
    data = r.get(m_id)
    if data:
        return jsonify({m_id : json.loads(data)}) # Nếu key đúng thì trả về dữ liệu từ Redis
    else:
        response = jsonify({"status": "Data not found"})
        response.status_code = 404  # Trả về status code 404 - Not Found
        return response  # Nếu key sai thì thông báo Data not found

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)
