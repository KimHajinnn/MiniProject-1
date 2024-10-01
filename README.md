# MiniProject-1
Nama : Christian Amsal Asimaro Lumban Tobing

Kelas: Sistem Informasi B 24

NIM  : 2409116053

Tugas: Mini Project 1 (Dasar-Dasar Pemograman)


# Flowchart

![Mini Project 1 drawio (2)](https://github.com/user-attachments/assets/074bfbdd-4f52-4afb-9e4d-d27fbcc6182d)


# Penjelasan
1. Masukkan Judul

print("============================================================")

print("Program Menghitung Gaji Karyawan                            ")

print("============================================================")

3. Buat Registrasi

print("Silahkan Daftar Akun")

nama = (input("Masukkan Nama          :"))
Nim  = (input("Masukkan NIM           :"))
Prodi= (input("Masukkan Program Studi :"))
Pass = (input("Buat Password Anda     :"))

(Menggunakan "input" untuk memasukkan nama, nim, prodi, pass)

4. Buat "Login Akun"

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
    
(Menggunakan "while True" untuk melakukan looping jika Nama dan Password tidak sesuai)

(Menggunakan "if-else" untuk memasukkan akun yang sudah dibuat)

(menggunakan fungsi "continue" untuk mengulang dari tempat "while True")

(Menggunakan fungsi "break" untuk memberhentikan looping)

5.  Masukkan Tarif dan Waktu Kerja untuk mengetahui Nominal Gaji dan Bonus

while True :
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
        
(Menggunakan "while True" untuk bisa melakukan looping)

(Menggunakan "\n" untuk masuk ke line baru)

(Menggunakan "if-else" untuk menentukan bonus)

6. memasukkan pengulangan

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
   
(Menggunakan "input" untuk menanyakan apakah ingin mengulang atau tidak)

(Menggunakan "if-elif-else" untuk memasukkan pilihan pengulangan atau tidak)

(Menggunakan "continue" untuk memulai dari tempat "while True" di tempatkan)

(Menggunakan "Break" untuk memberhentikan Looping)


# Foto Output pada Terminal dan Penjelasannya

![Screenshot 2024-10-01 105656](https://github.com/user-attachments/assets/fb8383c7-269e-498a-ac42-24724a81526e)

Daftarkan Akun dengan memasukkan Nama, Nim, Prodi, dan Password

![Screenshot 2024-10-01 105738](https://github.com/user-attachments/assets/b58b90c9-afc4-47e8-8f39-88c3f3aef938)

Kemudian Masukkan Nama dan Password yang sudah di masukkan saat Daftar Akun di Login Akun

![Screenshot 2024-10-01 105826](https://github.com/user-attachments/assets/6ef2c1d1-2260-45a3-9610-3d7a96f4b503)

Setelah Login, Masukkan Nominal Tarif Kerja dan waktu kerja untuk melakukan perhitungan bonus yang di dapat dan total gaji

![Screenshot 2024-10-01 105844](https://github.com/user-attachments/assets/a4244ba0-ef36-4c6b-a5be-fd81e21983b5)

setelah melakukan penghitungan gaji, akan muncul pilihan untuk mengulang atau tidak.

jika mengulang, akan mengulang dari Memasukkan Nominal Tarif dan waktu kerja

jika tidak, akan keluar dari program

