# Tipe data integer (bilangan bulat)
volume = 800
print('Variabel volume:', volume)
print('Tipe data:', type(volume))  # syntax type(x) untuk melihat tipe data

print('')

# Tipe data float (bilangan desimal)
panjang = 300.2
print('Variabel panjang:', panjang)
print('Tipe data:', type(panjang))  # syntax type(x) untuk melihat tipe data

print('')

# Tipe data string (karakter)
kata = "ini adalah string"  # selama diapit "", tipe datanya string
print('Variabel kata:', kata)
print('Tipe data:', type(kata))  # syntax type(x) untuk melihat tipe data

print('')

# Tipe data boolean (biner = true/false)
kebenaran = True
print('Variabel kebenaran:', kebenaran)
print('Tipe data:', type(kebenaran))  # syntax type(x) untuk melihat tipe data

print('')

# Tipe data khusus (bilangan kompleks)
datakhusus = complex(5, 4)  # imajiner
print('Variabel datakhusus:', datakhusus)
print('Tipe data:', type(datakhusus))  # syntax type(x) untuk melihat tipe data

print('')

# Tipe data dari bahasa C (C data types)
from ctypes import c_double  # import c_double dari paket ctypes

data_c_double = c_double(85.5)
print('Variabel data_c_double:', data_c_double)
print('Tipe data:', type(data_c_double))  # syntax type(x) untuk melihat tipe data
print('Nilai data_c_double:', data_c_double.value)  # untuk melihat nilai dari c_double
