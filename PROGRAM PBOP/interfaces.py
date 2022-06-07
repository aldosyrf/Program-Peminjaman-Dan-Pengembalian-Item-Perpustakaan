from member import Member
from peminjaman import Peminjaman
from db import listPinjam, listMember, listUser
import getpass


def login():
    print("\n|====================SISTEM PERPUSTAKAAN==================|")
    print("|========================FORM LOGIN=======================|\n")
    u = str(input("\tUsername = "))
    p = getpass.getpass("\tPassword = ")
    for i in listUser:
        if u == i.username and p == i.password:
            print("\nLogin Berhasil!!!")
            print("\n|==========SELAMAT DATANG DI PERPUSTAKAAN MERDEKA=========|")
            menuUtama()
    print("\nUsername dan Password Tidak Valid!!!")
    login()
    
def menuMember():
    print("\n|========================MENU MEMBER======================|\n")
    print("\t1. Daftar Member Baru")
    print("\t2. Tampilkan List Member")
    print("\t0. Kembali")
    y = int(input("\tMasukkan Pilihan = "))
    if y == 1:
        print("\n|=================MASUKKAN DATA MEMBER BARU===============|\n")
        b = str(input("\tMasukkan Nama  = "))
        c = str(input("\tMasukkan Alamat  = "))
        d = str(input("\tMasukkan Nomor Handphone  = "))
        a = b+d[-3:]
        (a) = Member(a, b, c, d)
        listMember.append(a)
        print("\nBerhasil Daftar Member Baru!!!")
        menuMember()
    elif y == 2:
        print("\n|========================LIST MEMBER======================|\n")
        for i in listMember:
            print(f">>>>\tID = {i.idMember}\n\tNama = {i.nama}\n\tAlamat = {i.alamat}\n\tNomor Handphone = {i.nomorHp}")
        menuMember()
    elif y == 0:
        menuUtama()
    else:
        print("\n|=============MASUKKAN PILIHAN DENGAN BENAR!!!============|\n")
        menuMember()

def menuUtama():
    print("|========================MENU UTAMA=======================|\n")
    print("\t1. Peminjaman")
    print("\t2. Pengembalian")
    print("\t3. Item Hilang")
    print("\t4. Member")
    print("\t0. Exit")
    x = int(input("\tMasukkan Pilihan = "))
    if x == 1:
        checkId = str(input("\n\tMasukkan ID Member = "))
        for i in listMember:
            if checkId == i.idMember:
                Member.buatPinjaman(i)
                menuUtama()
        print("ID TIdak Ditemukan!!")
        menuUtama()
    elif x == 2:
        for i in listPinjam:
            print(f"\n>>>>\tID = {i.idPeminjaman}\n\tNama = {i.nama}\n\tJudul = {i.judul}@{i.harga}\n\tLama Pinjam = {i.tglPinjam.day}-{i.tglKembali}\n\tStatus = {i.status}\n")
        x = str(input("Masukkan ID Peminjaman = "))
        for i in listPinjam:
            if x == i.idPeminjaman:
                Peminjaman.pengembalian(i)
                menuUtama()
        print("ID TIdak Ditemukan!!")
        menuUtama()
    elif x == 3:
        for i in listPinjam:
            print(f"\n>>>>\tID = {i.idPeminjaman}\n\tNama = {i.nama}\n\tJudul = {i.judul}@{i.harga}\n\tLama Pinjam = {i.tglPinjam.day}-{i.tglKembali}\n\tStatus = {i.status}\n")
        x = str(input("Masukkan ID Peminjaman = "))
        for i in listPinjam:
            if x == i.idPeminjaman:
                Peminjaman.itemHilang(i)
                menuUtama()
        print("ID TIdak Ditemukan!!")
        menuUtama()
    elif x == 4:
        menuMember()
    elif x == 0:
        print("Exit")
        exit()
    else:
        print("\n|=============MASUKKAN PILIHAN DENGAN BENAR!!!============|\n")
        menuUtama()

