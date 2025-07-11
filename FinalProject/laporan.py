import csv
from datetime import datetime, timedelta

def laporan(path='data/transaksi.csv', mode='harian'):
    now = datetime.now()
    if mode == 'harian':
        batas = now.strftime('%Y-%m-%d')
    elif mode == 'mingguan':
        batas = now - timedelta(days=7)
    elif mode == 'bulanan':
        batas = now.replace(day=1)
    else:
        return

    try:
        with open(path, newline='') as f:
            reader = csv.DictReader(f)
            print(f"Laporan {mode.capitalize()}:")
            for row in reader:
                tanggal_transaksi = datetime.strptime(row['tanggal'], '%Y-%m-%d')
                if mode == 'harian' and row['tanggal'] == batas:
                    print(row)
                elif mode in ['mingguan', 'bulanan'] and tanggal_transaksi >= batas:
                    print(row)
    except FileNotFoundError:
        print("Belum ada transaksi.")