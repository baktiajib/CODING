import time  # Mengimpor modul 'time' untuk mengakses fungsi terkait waktu

# Inisialisasi waktu mulai eksekusi kode
start_time = time.time()  # Menyimpan waktu saat eksekusi dimulai

# Mencetak informasi mengenai pembelajaran bahasa Python
print('Alur pembelajaran bahasa python')  # Mencetak teks ke konsol
print('Mudah dimengerti untuk tools bidang lain')  # Mencetak teks ke konsol
print('Dan bisa digunakan di semua bidang data')  # Mencetak teks ke konsol
print('')  # Mencetak baris kosong ke konsol

# Looping sebanyak 1.000.000 kali
for i in range(1, 1000000):  # Loop dari 1 hingga 999999
    a = 10  # Pada setiap iterasi, variabel 'a' diisi dengan nilai 10

# Menghitung dan mencetak waktu eksekusi dari program
print(time.time() - start_time, 'detik')  # Menghitung selisih waktu antara sekarang dan waktu mulai, kemudian mencetaknya dalam satuan detik
