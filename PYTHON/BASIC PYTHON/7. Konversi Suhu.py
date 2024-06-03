# Program untuk konversi suhu dari Celcius ke Reamur, Fahrenheit, dan Kelvin

# Input suhu dalam Celcius dari pengguna
celcius = float(input('Masukkan suhu dalam Celcius: '))
print('Suhu = ', celcius, 'Celcius')

# Konversi ke Reamur
# Menggunakan rumus: R = (4/5) * C
reamur = (4/5) * celcius
print('Suhu = ', reamur, 'Reamur')

# Konversi ke Fahrenheit
# Menggunakan rumus: F = (9/5) * C + 32
fahrenheit = (9/5) * celcius + 32
print('Suhu = ', fahrenheit, 'Fahrenheit')

# Konversi ke Kelvin
# Menggunakan rumus: K = C + 273.15
kelvin = celcius + 273.15
print('Suhu = ', kelvin, 'Kelvin')
