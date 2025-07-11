from produk import ProdukList, ProdukNode
from transaksi import TransaksiStack
from pembelian import AntrianPembelian
from laporan import laporan

produk_list = ProdukList()
produk_list.muat_dari_csv()

transaksi_stack = TransaksiStack()
antrian_pembelian = AntrianPembelian()

def login():
    print("======Login======")
    username = input("Username: ")
    password = input("Password: ")

    if username == "admin" and password == "admin123":
        return "admin"
    elif username == "user1" and password == "1234":
        return "user"
    else:
        print("[!] Login gagal.")
        return None
 
def menu():
    role = None
    while not role:
        role = login()

    while True:
        print(f"\n--- Menu Toko Ban Sepeda ({role.upper()}) ---")
        print("1. Tampilkan Produk")
        print("2. Transaksi Penjualan")
        print("3. Tambah ke Antrian Pembelian")
        if role == "admin":
            print("4. Tambah Produk")
            print("5. Proses Antrian Pembelian")
            print("6. Laporan")
        print("0. Logout")
        pilih = input("Pilih: ")

        if pilih == "1":
            produk_list.tampilkan_produk()
        elif pilih == "2":
            idp = input("ID Produk: ")
            jumlah = int(input("Jumlah: "))
            if idp in produk_list.map_produk:
                produk = produk_list.map_produk[idp]
                if produk.stok >= jumlah:
                    total = produk.harga * jumlah
                    produk.stok -= jumlah
                    produk_list.simpan_csv()
                    transaksi_stack.tambah_transaksi(idp, jumlah, total)
                    print("Transaksi berhasil!")
                else:
                    print("Stok tidak cukup.")
            else:
                print("Produk tidak ditemukan.")
        elif pilih == "3":
            idp = input("ID Produk: ")
            jumlah = int(input("Jumlah: "))
            antrian_pembelian.tambah_pembelian(idp, jumlah)
        elif pilih == "4" and role == "admin":
            idp = input("ID Produk: ")
            nama = input("Nama: ")
            stok = int(input("Stok: "))
            harga = int(input("Harga: "))
            deskripsi = input("Deskripsi: ")
            produk_list.tambah_produk(ProdukNode(idp, nama, stok, harga, deskripsi))
        elif pilih == "5" and role == "admin":
            antrian_pembelian.proses_pembelian()
        elif pilih == "6" and role == "admin":
            mode = input("Mode laporan (harian/mingguan/bulanan): ")
            laporan(mode=mode)
        elif pilih == "0":
            print("Logout...")
            break
        else:
            print("Akses tidak diizinkan atau pilihan tidak valid.")

menu()
