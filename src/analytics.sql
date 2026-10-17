SELECT
    payment_method,
    COUNT(*) AS total_transaksi,
    SUM(CASE WHEN status = 'success' THEN 1 ELSE 0 END)
        AS transaksi_berhasil,
    SUM(CASE WHEN status = 'failed' THEN 1 ELSE 0 END)
        AS transaksi_gagal
FROM transactions
GROUP BY payment_method; 