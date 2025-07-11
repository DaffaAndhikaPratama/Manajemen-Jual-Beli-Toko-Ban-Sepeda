import csv

class ProdukNode:
    def __init__(self, id_produk, nama, stok, harga, deskripsi):
        self.id_produk = id_produk
        self.nama = nama
        self.stok = int(stok)
        self.harga = int(harga)
        self.deskripsi = deskripsi
        self.next = None\
        
class ProdukList:
    def __init__(self):
        self.head = None
        self.map_produk = {}
    
    def tambah_produk(self, produk: ProdukNode):
        produk.next = self.head
        self.head = produk
        self.map_produk[produk.id_produk] = produk
        self.simpan_csv()

    def muat_dari_csv(self, path='data/produk.csv'):
        try:
            with open(path, newline='') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    p = ProdukNode(**row)
                    self.tambah_produk(p)
        except FileExistsError:
            pass
    
    def simpan_csv(self, path='data/produk.csv'):
        with open(path, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['id_produk', 'nama', 'stok', 'harga', 'deskripsi'])
            writer.writeheader()
            current = self.head
            while current:
                writer.writerow({
                    'id_produk': current.id_produk,
                    'nama': current.nama,
                    'stok': current.stok,
                    'harga': current.harga,
                    'deskripsi': current.deskripsi
                })
                current = current.next
                
    def tampilkan_produk(self):
        current = self.head
        while current:
            print(f"[{current.id_produk}] {current.nama} - Stok: {current.stok} - Harga: {current.harga}")
            current = current.next
