from confluent_kafka import Consumer, KafkaException
import redis
import json

# Cấu hình Kafka
bootstrap_servers = '118.68.13.3:8099'
topic = 'logger-testing'

conf = {
    'bootstrap.servers': bootstrap_servers,
    'group.id': '1',  
    'auto.offset.reset': 'earliest' # Thiết lập offset reset khi Consumer bắt đầu
}

# Kết nối tới Redis
r = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

# Khởi tạo Consumer và subscribe vào topic
consumer = Consumer(conf)
consumer.subscribe([topic])

try:
    while True:
        # Nhận message từ Kafka
        message = consumer.poll(1.0)

         # Xử lý lỗi
        if message is None:
            continue
        if message.error():
            if message.error().code() == KafkaException._PARTITION_EOF:
                print(f"Reached end of partition {message.topic()} [{message.partition()}] at offset {message.offset()}")
            else:
                print(f"Error: {message.error()}")
                break
        
        data = message.value().decode('utf-8') # Giải mã dữ liệu từ message nhận được
        key = message.key().decode('utf-8') # Lấy key của data
        r.set(key, data) # Lưu data vào Redis
        print(f"{key} : {json.loads(data)}") # In thông tin dữ liệu đã lưu vào Redis
        
except KeyboardInterrupt:
    pass

finally:
    consumer.close()
