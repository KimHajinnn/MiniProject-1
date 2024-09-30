print("============================================================")
print("Silahkan Registrasi")
nama = (input("Masukkan Nama          :"))
Nim  = (input("Masukkan NIM           :"))
Prodi= (input("Masukkan Program Studi :"))
Pass = (input("Buat Password Anda     :"))
print("============================================================")
print("Silahkan Login")
Nama     = (input("Masukkan Nama Anda     :"))
Password = (input("Masukkan Password Anda :"))
if Nama == nama and Password == Pass :
    print(f"Baik, Selamat Datang {nama}")
else :
    print("Nama atau Password anda salah, silahkan coba lagi")
    exit()
print("============================================================")

tarifkerja = int(input("Masukkan Tarif Kerja :"))
jamkerja  = int(input("Masukkan Jam Kerja :"))
gaji = tarifkerja * jamkerja
print(f"Gaji anda sebesar {gaji}")

if jamkerja >= 160  :
    jk = (f"Anda mendapatkan Bonus sebesar {gaji * 10/100}" f"\nTotal Gaji anda sebesar {gaji + gaji * 10/100} ")
    print(jk)
else: 
    jk = (f"Anda tidak mendapatkan Bonus \ngaji anda sebesar {gaji}")
    print(jk)

while True :
    print("Apakah anda ingin menghitung ulang? \n1. Ya \n2. Tidak")
    pengulangan = input("Masukkan Pilihan anda :")
    if pengulangan == "1" :
        print("Baik, silahkan Menghitung ulang")
        break
    elif pengulangan == "2" :
        print("Baik, Terimakasih")
        break
    else :
        print("Error, Masukkan sesuai pilihan (1/2)")