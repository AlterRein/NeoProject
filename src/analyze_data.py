#Analyze Data File

import csv

CSV_PATH = "../data/raw/data_transaksi.csv"

analytics = {}

with open(CSV_PATH, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        method = row["payment_method"]
        status = row["status"]
        amount = int(row["amount_idr"])
        fee = int(row["processing_fee_idr"])

        if method not in analytics:
            analytics[method] = {
                "total": 0,
                "success": 0,
                "failed": 0,
                "total_amount": 0,
                "total_fee": 0
            }

        stats = analytics[method]

        stats["total"] += 1
        stats["total_amount"] += amount
        stats["total_fee"] += fee

        if status == "success":
            stats["success"] += 1
        elif status == "failed":
            stats["failed"] += 1

print("=" * 55)
print("PAYMENT INTELEGENCE PLATFORM")
print("PAYMENT PERFORMANCE SUMMARY")
print("=" * 55)

for method, stats in analytics.items():
    success_rate = (
        stats["success"] / stats["total"] * 100
    )

    average_fee = stats["total_fee"] / stats["total"]

    print(f"\nMetode pembayaran: {method}")
    print(f"Total transaksi: {stats['total']}")
    print(f"Berhasil: {stats['success']}")
    print(f"Gagal: {stats['failed']}")
    print(f"Success rate: {success_rate:.2f}%")
    print(f"Total nilai transaksi: Rp{stats['total_amount']:,}")
    print(f"Total biaya pemrosesan: Rp{stats['total_fee']:,}")
    print(f"Rata-rata biaya per transaksi: Rp{average_fee:,.2f}")