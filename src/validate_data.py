import csv
from datetime import datetime

CSV_PATH = "../data/raw/data_transaksi.csv"

EXPECTED_COLUMNS = [
    "transaction_id",
    "timestamp",
    "payment_method",
    "region",
    "amount_idr",
    "status",
    "failure_reason",
    "processing_fee_idr"
]

ALLOWED_METHODS = {"card", "bank_transfer", "e_wallet"}
ALLOWED_REGIONS = {"east_java", "west_java", "jakarta"}
ALLOWED_STATUSES = {"success", "failed"}

errors = []
transaction_ids = set()
total_rows = 0

with open(CSV_PATH, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    if reader.fieldnames != EXPECTED_COLUMNS:
        errors.append(
            f"Header tidak sesuai : {reader.fieldnames}"
        )

    for row_number, row in enumerate(reader, start=2):
        total_rows += 1

        transaction_id = row["transaction_id"]
        method = row["payment_method"]
        region = row["region"]
        status = row["status"]
        reason = row["failure_reason"]

        if not transaction_id:
            errors.append(f"Baris {row_number}: ID kosong")
        elif transaction_id in transaction_ids:
            errors.append(
                f"Baris {row_number}: ID Duplikat"
            )
        transaction_ids.add(transaction_id)

        try:
            amount = int(row["amount_idr"])
            fee = int(row["processing_fee_idr"])

            if amount <= 0:
                errors.append(
                    f"Baris {row_number}: nominal tidak valid"                    
                )

            if fee < 0:
                errors.append(
                    f"Baris {row_number}: Biaya negatif"
                )
            
        except ValueError:
            errors.append(
                f"Baris {row_number}: nominal/biaya bukan integer"
            )

        if method not in ALLOWED_METHODS:
            errors.append(
                f"Baris {row_number}: method tidak valid"
            )

        if region not in ALLOWED_REGIONS:
            errors.append(
                f"Baris {row_number}: wilayah tidak valid"
            )

        if status not in ALLOWED_STATUSES:
            errors.append(
                f"Baris {row_number}: status tidak valid"
            )

        try:
            datetime.fromisoformat(row["timestamp"])
        except ValueError:
            errors.append(
                f"Baris {row_number}: alasan kegagalan kosong"
            )

print(f"Total transaksi: {total_rows}")
print(f"Todal masalah: {len(errors)}")

if errors:
    for error in errors:
        print("ERROR:", error)
else:
    print("Validasi data Berhasil : semua pemeriksaan lolos")