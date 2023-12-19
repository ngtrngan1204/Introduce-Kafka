import logging
from fastapi import FastAPI, HTTPException, Body
from confluent_kafka import Producer, KafkaException
import json
import redis
import os
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# Set up file log
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('error.log'),
        logging.StreamHandler()
    ]
)

# Connect to Redis
r = redis.StrictRedis(host='my-redis', port=6379, decode_responses=True)

# Kafka configuration
bootstrap_servers = os.environ['SERVER']
topic = os.environ['TOPIC']

# Create Kafka Producer
producer_conf = {'bootstrap.servers': bootstrap_servers}
kafka_producer = Producer(producer_conf)


def delivery_report(err, msg):
    if err is not None:
        logging.error(f'Message delivery failed: {err.code()}')
        # Handle error logging, retries, or other actions
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

class CPUInfo(BaseModel):
    total: int
    used: int
    free: int
    shared: int
    buff_cache: int
    available: int


@app.post('/cpu-info/{m_id}')
async def receive_data(
    m_id: str, 
    data: CPUInfo = Body(
        examples=[
            {
                "total": 8092116,
                "used": 2063096,
                "free": 3674872,
                "shared": 2932,
                "buff_cache": 2354148,
                "available": 5730692
            }
        ],
    ),
):
    try:
        # Validate using Pydantic's model validation
        data_dict = data.dict()

        required_fields = ["total", "used", "free", "shared", "buff_cache", "available"]
        for field in required_fields:
            if field not in data_dict or not isinstance(data_dict[field], int):
                if field not in data_dict:
                    raise HTTPException(status_code=400, detail=f"Missing field: {field}")
                else:
                    raise HTTPException(status_code=400, detail=f"Invalid field type for '{field}' - must be an integer")

        for field in data_dict:
            if field not in required_fields:
                raise HTTPException(status_code=400, detail=f"Extra field not allowed: '{field}'")

        raw = json.dumps(data_dict)

        kafka_producer.produce(topic, key=m_id, value=raw, callback=delivery_report)
        kafka_producer.flush()

        return {m_id: data_dict}

    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON format")

@app.get('/cpu-info/{m_id}')
async def get_data(m_id: str):
    data = r.get(m_id)
    if data:
        return {m_id: json.loads(data)}
    else:
        raise HTTPException(status_code=404, detail="Data not found")
