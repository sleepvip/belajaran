###BELAJAR KALKULATOR
import os

os.system('clear')
print("Projecstar Belajar Variabel")
print("")
print("1.Perkalian")
print("2.Pertambahan")
print("3.Pengurangan")
print("4.Pembagian")
print("")

########
def kali():
    a = int(input("Masukan Angka Awal : "))
    b = int(input("Masukan Angka Akhir : "))
    c =a*b
    print(c)
    
def tambah():
    a = int(input("Masukan Angka Awal : "))
    b = int(input("Masukan Angka Akhir : "))
    c =a+b
    print(c)
    
def kurang():
    a = int(input("Masukan Angka Awal : "))
    b = int(input("Masukan Angka Akhir : "))
    c =a-b
    print(c)
    
def bagi():
    a = int(input("Masukan Angka Awal : "))
    b = int(input("Masukan Angka Akhir : "))
    c =a/b
    print(c)
    
if __name__ == '__main__':
    menu = int(input("Masukan Menu : "))
    if menu == 1:
        kali()
    if menu == 2:
        tambah()
    if menu == 3:
        kurang()
    if menu == 4:
        bagi()