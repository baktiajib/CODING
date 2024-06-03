# Operasi Perbandingan (Comparator Operation) pada Python
# Hasil operasi perbandingan akan berupa nilai boolean (True/False)

# Daftar operasi perbandingan:
# >   : Lebih besar dari
# <   : Lebih kecil dari
# >=  : Lebih besar dari atau sama dengan
# <=  : Lebih kecil dari atau sama dengan
# ==  : Sama dengan
# !=  : Tidak sama dengan
# is  : Objek identik (untuk membandingkan dua objek)
# is not: Objek tidak identik (untuk membandingkan dua objek)

a = float(input('Masukkan variabel a = '))
b = float(input('Masukkan variabel b = '))

# Hasil operasi perbandingan
hasil1 = a > b
hasil2 = a < b
hasil3 = a >= b
hasil4 = a <= b
hasil5 = a == b
hasil6 = a != b
hasil7 = a is b  # Membandingkan dua objek
hasil8 = a is not b  # Membandingkan dua objek

# Menampilkan hasil operasi perbandingan
print('Lebih besar dari =', hasil1, 'id a =', hex(id(a)), 'id b =', hex(id(b)))
print('Lebih kecil dari =', hasil2)
print('Lebih besar atau sama dengan =', hasil3)
print('Lebih kecil atau sama dengan =', hasil4)
print('Sama dengan =', hasil5)
print('Tidak sama dengan =', hasil6)
print('Objek identik =', hasil7)
print('Objek tidak identik =', hasil8)

# hex(id(variabel)) digunakan untuk menampilkan ID memori penyimpanan variabel
