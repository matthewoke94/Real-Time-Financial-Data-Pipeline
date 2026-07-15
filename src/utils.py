import random


def transaction_status():
    return random.choice([
        "SUCCESS",
        "FAILED",
        "PENDING"
    ])


def transaction_type():
    return random.choice([
        "Deposit",
        "Withdrawal",
        "Transfer",
        "Payment"
    ])