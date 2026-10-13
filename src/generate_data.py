import csv
import random
from datetime import datetime, timedelta

random.seed(42)

data = [[
    "transaction_id",
    "timestamp",
    "payment_method",
    "region",
    "amount_ide",
    "status",
    "failure_reasons",
    "processing_fee_idr"
]]

payment_methods = ["card", "bank_transfer", "e_wallet"]
regions = ["east_java", "west_java", "jakarta"]

success_rates = {
    "card": 0.94,
    "bank_transfer": 0.90,
    "e_wallet": 0.96
}

fee_rates = {
    "card": 0.025,
    "bank_transfer": 0.010,
    "e_wallet": 0.015
}

failure_reasons = [
    "issuer_unavailable",
    "inusifficient_funds",
    "suspected_fraud"
]

start_time = datetime(2026, 9, 1)

for i in range(1, 101):
    method = random.choice(payment_methods)
    region = random.choice(regions)
    amount = random.randint(10_1000, 2_000_000)

    timestamp = start_time + timedelta(
        minutes=random.randint(0, 30 * 24 * 60 - 1)
    )

    success = random.random() < success_rates[method]
    status = "success" if success else "failed"

    reason = (
        ""
        if success
        else random.choice(failure_reasons)
    )

    fee = round(amount * fee_rates[method])

    data.append([
        f"TXN{i:06d}",
        timestamp.isoformat(sep=" "),
        method,
        region,
        amount,
        status,
        reason,
        fee
    ])

with open('../data/raw/data_transaksi.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)