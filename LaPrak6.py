# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 19:23:44 2021

@author: Abdullah
"""

# ELEMEN KOMPETENSI 1
print("MENGHITUNG JARAK TEMPUH GLBB")
kecepatan_awal = int(input("Masukkan v0: "))
waktu = int(input("Masukkan t: "))
percepatan = int(input("Masukkan a: "))

jarak = kecepatan_awal * waktu + 0.5 * percepatan * waktu ** 2

print("Jarak tempuh jika kecepatan awal =  {}, waktu = {} dan percepatan = {} adalah {}".format(kecepatan_awal, waktu, percepatan, jarak))

# ELEMEN KOMPETENSI 2
PI = 3.141592653589793238


def kubus():
    rusuk = int(input("Masukkan nilai rusuk: "))
    print("Luas permukaan kubus dengan rusuk", rusuk, "adalah", hitung_kubus(rusuk), "\n")


def hitung_kubus(rusuk):
    return rusuk ** 2 * 6


def balok():
    panjang, lebar, tinggi = int(input("Masukkan nilai panjang: ")), int(input("Masukkan nilai lebar: ")), int(
        input("Masukkan nilai tinggi: "))
    print("Luas permukaan balok dengan panjang {}, lebar {} dan tinggi {} " "adalah".format(panjang, lebar, tinggi),
          hitung_balok(panjang, lebar, tinggi), "\n")


def hitung_balok(panjang, lebar, tinggi):
    return panjang * tinggi * 2 + panjang * lebar * 2 + tinggi * lebar * 2


def tabung():
    jari2, tinggi = int(input("Masukkan nilai jari-jari: ")), int(input("Masukkan nilai tinggi: "))
    print("Luas permukaan tabung dengan jari-jari {} dan tinggi {} " "adalah".format(jari2, tinggi),
          hitung_tabung(jari2, tinggi, PI), "\n")


def hitung_tabung(jari2, tinggi, pi):
    return 2 * pi * jari2 * (tinggi + jari2)


def kerucut():
    jari2, garis_lukis = int(input("Masukkan nilai jari-jari: ")), int(input("Masukkan nilai garis lukis: "))
    print("Luas permukaan kerucut dengan jari-jari {} dan garis lukis {} " "adalah".format(jari2, garis_lukis),
          hitung_kerucut(jari2, garis_lukis, PI), "\n")


def hitung_kerucut(jari2, garis_lukis, pi):
    return pi * jari2 ** 2 + pi * jari2 * garis_lukis


def bola():
    jari2 = int(input("Masukkan nilai jari-jari: "))
    print("Luas permukaan bola dengan jari-jari {} " "adalah".format(jari2), hitung_bola(jari2, PI), "\n")


def hitung_bola(jari2, pi):
    return 4 * pi * (jari2 * jari2)


while True:
    print("KALKULATOR LUAS PERMUKAAN BANGUN RUANG\n1. Kubus\n2. Balok\n3. Tabung\n4. Kerucut\n5. Bola\n6. Exit")
    pilihan = input("Pilih menu yang tersedia: ")
    if pilihan == "1":
        kubus()
    elif pilihan == "2":
        balok()
    elif pilihan == "3":
        tabung()
    elif pilihan == "4":
        kerucut()
    elif pilihan == "5":
        bola()
    elif pilihan == "6":
        print("TERIMA KASIH!")
        break
    else:
        print("Pilih 1, 2, 3, 4 atau 5, e untuk keluar\n")
