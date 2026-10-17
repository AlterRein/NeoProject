import csv
import sqlite3

CSV_PATH = "../data/raw/data_transaksi.csv"
DB_PATH = "../data/payment_intelligence.db"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    transaction_id TEXT PRIMARY KEY,
    timestamp TEXT NOT NULL,
    payment_method TEXT NOT NULL,
    region TEXT NOT NULL,
    amount_idr INTEGER NOT NULL,
    status TEXT NOT NULL,
    failure_reason TEXT,
    processing_fee_idr INTEGER NOT NULL
)
""")

with open(CSV_PATH, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    rows = [
        (
            row["transaction_id"],
            row["timestamp"],
            row["payment_method"],
            row["region"],
            int(row["amount_idr"]),
            row["status"],
            row["failure_reason"] or None,
            int(row["processing_fee_idr"])
        )
        for row in reader
    ]

    cursor.executemany("""
        INSERT OR REPLACE INTO transactions (
            transaction_id,
            timestamp,
            payment_method,
            region,
            amount_idr,
            status,
            failure_reason,
            processing_fee_idr
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, rows)

connection.commit()

cursor.execute("SELECT COUNT(*) FROM transactions")
total = cursor.fetchone()[0]

print(f"Total transaksi di database: {total}")
print("Data berhasil dimuat ke SQLite")

connection.close()