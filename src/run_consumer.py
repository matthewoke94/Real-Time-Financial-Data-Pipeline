from src.consumer import receive_transactions
from src.load import load_data

for transaction in receive_transactions():

    load_data(transaction)

    print("Loaded:", transaction["customer_name"])