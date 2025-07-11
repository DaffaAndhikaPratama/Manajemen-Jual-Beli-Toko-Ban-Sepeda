import os
import csv

def buat_file_jika_belum_ada(path, fieldnames):
    # Buat folder jika belum ada
    folder = os.path.dirname(path)
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Buat file dengan header jika belum ada
    if not os.path.exists(path):
        with open(path, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
        print(f"[✓] File dibuat: {path}")
    else:
        print(f"[=] File sudah ada: {path}")

def setup_data_folder():
    print("Menyiapkan struktur data...")

    buat_file_jika_belum_ada('data/produk.csv', ['id_produk', 'nama', 'stok', 'harga', 'deskripsi'])
    buat_file_jika_belum_ada('data/transaksi.csv', ['tanggal', 'waktu', 'id_produk', 'jumlah', 'total'])
    buat_file_jika_belum_ada('data/pembelian.csv', ['tanggal', 'waktu', 'id_produk', 'jumlah'])

    print("Setup selesai.")

if __name__ == "__main__":
    setup_data_folder()
