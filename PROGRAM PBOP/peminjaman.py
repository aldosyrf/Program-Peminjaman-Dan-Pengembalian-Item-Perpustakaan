class Peminjaman:
    def __init__(self, idPeminjaman, nama, judul, harga, tglPinjam, tglKembali, status):
        self.idPeminjaman = idPeminjaman
        self.nama = nama
        self.judul = judul
        self.harga = harga
        self.tglPinjam = tglPinjam
        self.tglKembali = tglKembali
        self.status = status

    def pengembalian(self):
            telat = str(input("Apakah Pengembalian Telat? y/t = "))
            if telat == "y" or telat == "Y":
                lamaTelat = int(input("Berapa Hari Keterlambatan? = "))
                denda = lamaTelat * 3000
                print("\n|============DENDA KETERLAMBATAN = RP.3000/HARI===========|\n")
                print(f"\n\tDenda Yang Harus Dibayarkan Rp.{denda}")
                print("\n|=============TERIMAKASIH TELAH MENGEMBALIKAN=============|\n")
                self.status = "Kembali"
            elif telat == "t" or telat == "T":
                print("\n|=======TERIMAKASIH TELAH MENGEMBALIKAN TEPAT WAKTU=======|\n")
                self.status = "Kembali"
            else:
                print("Inputan Tidak Valid!!")

    def itemHilang(self):
        print("\n\t1. Mengganti Item Dengan Judul Yang Sama")
        print("\t2. Membayar Dengan Nominal Sesuai Item Yang Dihilangkan")
        hilang = int(input("\tMasukkan Pilihan = "))
        if hilang == 1:
            print(f"\n\tJudul Item {self.judul}")
            print("\n|===================ITEM TELAH DI TERIMA==================|\n")
            self.status = "Diganti Dengan Judul Yang Sama"
        elif hilang == 2:
            print(f"\tHarga Item {self.judul} adalah Rp.{self.harga}")
            print("\n|===================UANG TELAH DI TERIMA==================|\n")
            self.status = "Diganti Sesuai Harga Item"









