from kafka import KafkaProducer
import json

from src.config import KAFKA_SERVER, KAFKA_TOPIC

producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER,
    value_serializer=lambda v: json.dumps(v, default=str).encode("utf-8")
)


def send_transaction(transaction):

    producer.send(KAFKA_TOPIC, transaction)

    producer.flush()

    print("Transaction Sent Successfully")