from faker import Faker
import random
from datetime import datetime

from src.utils import transaction_status
from src.utils import transaction_type

fake = Faker()


def generate_transaction():

    return {

        "customer_name": fake.name(),

        "account_number": fake.iban(),

        "transaction_type": transaction_type(),

        "amount": round(random.uniform(50, 10000), 2),

        "currency": "USD",

        "country": fake.country(),

        "transaction_time": datetime.now(),

        "status": transaction_status()

    }