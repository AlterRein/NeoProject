import csv
import random

data = [
    ['transaction_id', 'amount_idr', 'status'],
]

for i in range(1, 101):
    transaction_id = f"TXN{i:06d}"
    amount_idr = random.randint(10000, 2000000)
    status = random.choice(["success", "failed"])

    data.append([
        transaction_id,
        amount_idr,
        status
    ])

with open('../data/raw/data_transaksi.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)