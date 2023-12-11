import logging
from confluent_kafka import Consumer, KafkaException
import redis
import json
import os

# Set up file log
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('error.log'),
        logging.StreamHandler()
    ]
)

# Cấu hình Kafka
bootstrap_servers = os.environ['SERVER']
topic = os.environ['TOPIC']
group_id = os.environ['GROUP_ID']
auto_offset = os.environ['AUTO_OFFSET']

conf = {
    'bootstrap.servers': bootstrap_servers,
    'group.id': group_id,
    'auto.offset.reset': auto_offset  # Thiết lập offset reset khi Consumer bắt đầu
}

# Kết nối tới Redis
r = redis.StrictRedis(host='my-redis', port=6379, decode_responses=True)

# Khởi tạo Consumer và subscribe vào topic
consumer = Consumer(conf)
consumer.subscribe([topic])

try:
    while True:
        message = consumer.poll(1.0)

        # Kiểm tra message đã nhận thành công chưa
        if message is None:
            continue
        if message.error():
            if message.error().code() == KafkaException._PARTITION_EOF:
                logging.info(f"Reached end of partition {message.topic()} [{message.partition()}] at offset {message.offset()}")
            else:
                logging.error(f"Error: {message.error().code()}")
                break

        data = message.value().decode('utf-8')  # Giải mã dữ liệu từ message nhận được
        key = message.key().decode('utf-8')  # Lấy key của data

        try:
            r.set(key, data)  # Lưu data vào Redis
            print(f"{key}: {json.loads(data)} Stored successfully")  # In ra màn hình data đã lưu vảo redis thành công
        except redis.RedisError as e:
            logging.error(f"{key}: {json.loads(data)} Failed to store - Error: {e}")  # Log error when khi lưu vào redis lỗi

except KeyboardInterrupt:
    pass

finally:
    consumer.close()
