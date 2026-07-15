from src.extract import generate_transaction
from src.producer import send_transaction

for _ in range(100):

    transaction = generate_transaction()

    send_transaction(transaction)