from kafka import KafkaConsumer
import json

from src.config import KAFKA_SERVER, KAFKA_TOPIC

consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=KAFKA_SERVER,
    value_deserializer=lambda m: json.loads(m.decode("utf-8")),
    auto_offset_reset="earliest",
    enable_auto_commit=True
)


def receive_transactions():

    for message in consumer:

        yield message.value