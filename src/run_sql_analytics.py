import sqlite3

DB_PATH = "../data/payment_intelligence.db"
SQL_PATH = "analytics.sql"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

with open(SQL_PATH, "r", encoding="utf-8") as file:
    query = file.read()

print("SQL YANG DIBACA PYTHON:")
print(repr(query))

cursor.execute(query)

if cursor.description:
    print("Query tidak menghasilkan tabel.")
else:
    columns = [description[0] for description in cursor.description]

    print("\n=== PAYMENT ANALYTICS ===\n")
    print(" | ".join(columns))
    print("-" * 70)

    for row in cursor.fetchall():
        print(" | ".join(str(value) for value in row))

connection.close()