from flask import Flask, jsonify, request
from confluent_kafka import Producer
import json
import redis

app = Flask(__name__)

# Kết nối tới Redis
r = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

# Cấu hình Kafka
bootstrap_servers = '118.68.13.3:8099'
topic = 'logger-testing'


# Tạo Kafka Producer
producer_conf = {'bootstrap.servers': bootstrap_servers}
kafka_producer = Producer(producer_conf)

def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err.code()}')
        # Ghi log lỗi, xử lý thử lại hoặc các hành động khác
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

# Endpoint nhận dữ liệu POST từ client rồi gửi đến Kafka
@app.route('/cpu-info/<id_counter>', methods=['POST'])
def receive_data(id_counter):
    data = json.loads(request.data)
    id=str(id_counter)
    raw=json.dumps({
            "total": data.get("total"),
            "used": data.get("used"),
            "free": data.get("free"),
            "shared": data.get("shared"),
            "buff/cache": data.get("buff/cache"),
            "available": data.get("available")
        })

    # Gửi dữ liệu tới Kafka
    kafka_producer.produce(topic, key=id, value=raw, callback=delivery_report)   

    kafka_producer.flush()

    return ({id : json.loads(raw)}) # Trả về dữ liệu dưới dạng JSON

# Endpoint truy cập dữ liệu từ Redis 
@app.route('/cpu-info/<m_id>', methods=['GET'])
def get_data(m_id):
    data = r.get(m_id)
    if data:
        return jsonify({m_id : json.loads(data)}) # Nếu key đúng thì trả về dữ liệu từ Redis
    else:
        return 'Data not found!!' # Nếu key sai thì thông báo Data not found

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)
