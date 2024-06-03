# Default input data adalah string
data = input('Masukkan data: ')
print('Data =', data, ', Tipe =', type(data))

# Jika ingin menginput angka, data string harus di-casting dulu
number = float(input('Masukkan angka: '))
print('Data =', number, ', Tipe =', type(number))

# Jika ingin input data boolean, data string harus di-casting ke (int/float) lalu boolean
biner = bool(float(input('Masukkan angka (untuk boolean): ')))
print('Data =', biner, ', Tipe =', type(biner))
