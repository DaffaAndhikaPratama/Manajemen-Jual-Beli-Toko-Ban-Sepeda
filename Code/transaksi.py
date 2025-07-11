import csv
from datetime import datetime

class TransaksiStack:
    def __init__(self):
        self.stack = []

    def tambah_transaksi(self, id_produk, jumlah, total):
        now = datetime.now()
        data = {
            'tanggal': now.strftime('%Y-%m-%d'),
            'waktu': now.strftime('%H:%M:%S'),
            'id_produk': id_produk,
            'jumlah': jumlah,
            'total': total
        }
        self.stack.append(data)
        self.simpan_csv(data)

    def simpan_csv(self, data, path='data/transaksi.csv'):
        file_exists = False
        try:
            with open(path, 'r'):
                file_exists = True
        except FileNotFoundError:
            pass

        with open(path, 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=data.keys())
            if not file_exists:
                writer.writeheader()
            writer.writerow(data)

    def tampilkan_histori(self):
        for t in reversed(self.stack):
            print(t)
