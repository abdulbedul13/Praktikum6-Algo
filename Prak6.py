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
