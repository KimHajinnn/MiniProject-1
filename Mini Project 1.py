print("============================================================")
print("Program Menghitung Gaji Karyawan                            ")
print("============================================================")
print("Silahkan Daftar Akun")
nama = (input("Masukkan Nama          :"))
Nim  = (input("Masukkan NIM           :"))
Prodi= (input("Masukkan Program Studi :"))
Pass = (input("Buat Password Anda     :"))
print("============================================================")
print("Silahkan Login")
while True :
    Nama     = (input("Masukkan Nama Anda     :"))
    Password = (input("Masukkan Password Anda :"))
    if Nama != nama or Password != Pass :
        print("Nama atau Password anda salah, silahkan coba lagi")
        continue
    else :
        print(f"Baik, Selamat Datang {nama}")
    print("============================================================")
    break

while True :
    tarifkerja = int(input("Masukkan Tarif Kerja :"))
    jamkerja  = int(input("Masukkan Jam Kerja :"))
    gaji = tarifkerja * jamkerja
    print(f"Gaji anda sebesar {gaji}")

    if jamkerja >= 160  :
        jk = (f"Anda mendapatkan Bonus sebesar {gaji * 10/100}" f"\nTotal Gaji anda sebesar {gaji + gaji * 10/100} ")
        print(jk)
    else: 
        jk = (f"Anda tidak mendapatkan Bonus \nGaji anda sebesar {gaji}")
        print(jk)


    print("Apakah anda ingin menghitung ulang? \n1. Ya \n2. Tidak ")
    pengulangan = input("Masukkan Pilihan anda :")
    if pengulangan == "1" :
        print("Baik, silahkan Menghitung ulang ")
        continue
    elif pengulangan == "2" :
        print("Baik, Terimakasih")
        break
    else :
        print("Error, Masukkan sesuai pilihan (1/2)")
