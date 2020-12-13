import os
import sys

def pindah(label):
    global nomor
    nomor = label

def clearscreen():
    os.system('cls')

def keluar():
    sys.exit()

def ulang():
    ulang = input("Apakah anda ingin mengulang  lagi ? [y/n] ")
    if ulang == "y" or ulang == "Y" :
        pindah(0)
        clearscreen()
    elif ulang == "n" or ulang == "N" :
        clearscreen()
        keluar()
    else :
        keluar()

def rumus():
    global anak, gapok, gajikotor, hitunglembur, hitunganak, persen, total
    anak = 200000
    hitunglembur = jumlem * lembur
    if jumanak > 3 :
        hitunganak = 3 * anak
    else :
        hitunganak = jumanak * anak

    gajikotor = gapok + hitunglembur + hitunganak 
    persen = (gajikotor * 5) / 100
    total = gajikotor - persen

def cetak():
    print( "=========================================")
    print( "|     Aplikasi Penggajian Karyawan      |")
    print ("=========================================")
    print( "| Nama        : ", nama)
    print ("| NIP         : ", nip)
    print ("| Jabatan     : " , jabatan )
    print ("| Gaji Kotor  : Rp. ", gajikotor)
    print ("| Potongan 5% : Rp. ", persen )
    print ("")
    print ("=> Gaji Bersih : Rp. ", total)
    print ("")
