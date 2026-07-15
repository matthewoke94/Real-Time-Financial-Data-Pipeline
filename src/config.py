import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

KAFKA_SERVER = os.getenv("KAFKA_SERVER")

KAFKA_TOPIC = os.getenv("KAFKA_TOPIC")