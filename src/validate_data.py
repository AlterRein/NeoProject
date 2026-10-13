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
    "proccessing_fee_idr"
]

ALLOWED_METHODS = {"card", "bank_transfer", "e_wallet"}
ALLOWED_REGIONS = {"east_java", "west_java", "jakarta"}
ALLOWED_STATUSES = {"success", "failed"}

