from datetime import date
from majalah import Majalah
from buku import Buku
from db import listPinjam, listItem
from peminjaman import Peminjaman


class Member:
    def __init__(self, idMember, nama, alamat, nomorHp):
        self.idMember = idMember
        self.nama = nama
        self.alamat = alamat
        self.nomorHp = nomorHp

    def buatPinjaman(self):
            print("\n|======================KATEGORI ITEM======================|\n")
            print("\t1. Buku")
            print("\t2. Majalah")
            print("\t3. DVD")
            kategori = int(input("\tMasukkan Pilihan = "))
            if kategori == 1:
                judulBuku = str(input("\n\tMasukkan Judul Buku = "))
                hargaBuku = int(input("\tMasukkan Harga Buku = "))
                isbn = str(input("\tMasukkan ISBN Buku = "))
                pengarang = str(input("\tMasukkan Pengarang Buku = "))
                buku = Buku(judulBuku, hargaBuku, isbn, pengarang)
                listItem.append(buku)
                tglPinjam = date.today()
                lamaPinjam = int(input("\tMasukkan Lama Pinjam (Hari) = "))
                while lamaPinjam <= 1 or lamaPinjam >=31:
                    print("\nBatas Peminjaman Minimal 2 Hari Dan Maksimal 30 Hari!!!\n")
                    lamaPinjam = int(input("\tMasukkan Lama Pinjam (Hari) = "))
                tglKembali = tglPinjam.day+lamaPinjam
                print("\n|=======HARGA PEMINJAMAN SETIAP ITEM = RP.2000/HARI=======|\n")
                print(f"Meminjam Pada Tanggal {tglPinjam.day}-{tglPinjam.month}-{tglPinjam.year}")
                if tglKembali >= 31:
                    tglKembali = tglKembali - 30
                    blnKembali = tglPinjam.month + 1
                    print(f"Harus Dikembalikan Pada Tanggal {tglKembali}-{blnKembali}-{tglPinjam.year}")
                else:
                    print(f"Harus Dikembalikan Pada Tanggal {tglKembali}-{tglPinjam.month}-{tglPinjam.year}")
                totalBayar = lamaPinjam * 2000
                print(f"\tTotal Bayar = Rp.{totalBayar}\n")
                status = "Pinjam"
                x = Peminjaman(
                    self.idMember+"@"+judulBuku, self.nama, judulBuku, hargaBuku, tglPinjam, tglKembali,status
                )
                listPinjam.append(x)
                print("Peminjaman Berhasil!!!")
            elif kategori == 2:
                judulMajalah = str(input("\n\tMasukkan Judul Majalah = "))
                hargaMajalah = int(input("\tMasukkan Harga Majalah = "))
                volume = str(input("\tMasukkan volume Majalah = "))
                majalah = Majalah(judulMajalah, hargaMajalah, volume)
                listItem.append(majalah)
                tglPinjam = date.today()
                lamaPinjam = int(input("\tMasukkan Lama Pinjam (Hari) = "))
                while lamaPinjam <= 1 or lamaPinjam >=31:
                    print("\nBatas Peminjaman Minimal 2 Hari Dan Maksimal 30 Hari!!!\n")
                    lamaPinjam = int(input("\tMasukkan Lama Pinjam (Hari) = "))
                tglKembali = tglPinjam.day+lamaPinjam
                print("\n|=======HARGA PEMINJAMAN SETIAP ITEM = RP.2000/HARI=======|\n")
                print(f"Meminjam Pada Tanggal {tglPinjam.day}-{tglPinjam.month}-{tglPinjam.year}")
                if tglKembali >= 31:
                    tglKembali = tglKembali - 30
                    blnKembali = tglPinjam.month + 1
                    print(f"Harus Dikembalikan Pada Tanggal {tglKembali}-{blnKembali}-{tglPinjam.year}")
                else:
                    print(f"Harus Dikembalikan Pada Tanggal {tglKembali}-{tglPinjam.month}-{tglPinjam.year}")
                totalBayar = lamaPinjam * 2000
                print(f"\tTotal Bayar = Rp.{totalBayar}\n")
                status = "Pinjam"
                x = Peminjaman(
                    self.idMember+"@"+judulMajalah, self.nama, judulMajalah, hargaMajalah, tglPinjam, tglKembali,status
                )
                listPinjam.append(x)
                print("Peminjaman Berhasil!!!")
            elif kategori == 3:
                judulDvd = str(input("\n\tMasukkan Judul DVD = "))
                hargaDvd = int(input("\tMasukkan Harga DVD = "))
                genreDvd = str(input("\tMasukkan Genre DVD = "))
                dvd = Majalah(judulDvd, hargaDvd, genreDvd)
                listItem.append(dvd)
                tglPinjam = date.today()
                lamaPinjam = int(input("\tMasukkan Lama Pinjam (Hari) = "))
                while lamaPinjam <= 1 or lamaPinjam >=31:
                    print("\nBatas Peminjaman Minimal 2 Hari Dan Maksimal 30 Hari!!!\n")
                    lamaPinjam = int(input("\tMasukkan Lama Pinjam (Hari) = "))
                tglKembali = tglPinjam.day+lamaPinjam
                print("\n|=======HARGA PEMINJAMAN SETIAP ITEM = RP.2000/HARI=======|\n")
                print(f"Meminjam Pada Tanggal {tglPinjam.day}-{tglPinjam.month}-{tglPinjam.year}")
                if tglKembali >= 31:
                    tglKembali = tglKembali - 30
                    blnKembali = tglPinjam.month + 1
                    print(f"Harus Dikembalikan Pada Tanggal {tglKembali}-{blnKembali}-{tglPinjam.year}")
                else:
                    print(f"Harus Dikembalikan Pada Tanggal {tglKembali}-{tglPinjam.month}-{tglPinjam.year}")
                totalBayar = lamaPinjam * 2000
                print(f"\tTotal Bayar = Rp.{totalBayar}\n")
                status = "Pinjam"
                x = Peminjaman(
                    self.idMember+"@"+judulDvd, self.nama, judulDvd, hargaDvd, tglPinjam, tglKembali,status
                )
                listPinjam.append(x)
            else:
                print("Pilihan Tidak Tersedia!!")
            



