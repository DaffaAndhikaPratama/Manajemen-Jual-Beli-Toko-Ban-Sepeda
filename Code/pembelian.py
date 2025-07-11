import csv
from collections import deque
from datetime import datetime

class AntrianPembelian:
    def __init__(self):
        self.antrian = deque()

    def tambah_pembelian(self, id_produk, jumlah):
        now = datetime.now()
        data = {
            'tanggal': now.strftime('%Y-%m-%d'),
            'waktu': now.strftime('%H:%M:%S'),
            'id_produk': id_produk,
            'jumlah': jumlah
        }
        self.antrian.append(data)
        self.simpan_csv(data)

    def proses_pembelian(self):
        if self.antrian:
            pembelian = self.antrian.popleft()
            print("Diproses:", pembelian)
            return pembelian
        else:
            print("Tidak ada antrian.")

    def simpan_csv(self, data, path='data/pembelian.csv'):
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
