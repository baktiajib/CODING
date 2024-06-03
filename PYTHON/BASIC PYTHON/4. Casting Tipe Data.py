# Casting = Merubah tipe data
# Tipe data: int, float, str, bool

print('===== INTEGER =====')
data_int = 9
print('Data =', data_int, '     Data awal\n', 'Tipe =', type(data_int))
# Casting ke tipe data lain
print('\nCasting tipe data')
data_float = float(data_int)  # ke float
data_str = str(data_int)  # ke string
data_bool = bool(data_int)  # ke boolean (False jika nilai = 0)
print('Data =', data_float, ', Tipe =', type(data_float))
print('Data =', data_str, ', Tipe =', type(data_str))
print('Data =', data_bool, ', Tipe =', type(data_bool))
print('')

print('===== FLOAT =====')
data_float = 87.5
print('Data =', data_float, '     Data awal\n', 'Tipe =', type(data_float))
# Casting ke tipe data lain
print('\nCasting tipe data')
data_int = int(data_float)  # ke integer
data_str = str(data_float)  # ke string
data_bool = bool(data_float)  # ke boolean (False jika nilai = 0)
print('Data =', data_int, ', Tipe =', type(data_int))
print('Data =', data_str, ', Tipe =', type(data_str))
print('Data =', data_bool, ', Tipe =', type(data_bool))
print('')

print('===== STRING =====')
data_str = '0'
print('Data =', data_str, '     Data awal\n', 'Tipe =', type(data_str))
# Casting ke tipe data lain
print('\nCasting tipe data')
data_int = int(data_str) if data_str.isdigit() else None  # string harus angka untuk ke integer
data_float = float(data_str) if data_str.replace('.', '', 1).isdigit() else None  # string harus angka untuk ke float
data_bool = bool(data_str)  # ke boolean (False jika string kosong)
print('Data =', data_int, ', Tipe =', type(data_int) if data_int is not None else 'Error: string bukan angka')
print('Data =', data_float, ', Tipe =', type(data_float) if data_float is not None else 'Error: string bukan angka')
print('Data =', data_bool, ', Tipe =', type(data_bool))
print('')

print('===== BOOLEAN =====')
data_bool = True
print('Data =', data_bool, '     Data awal\n', 'Tipe =', type(data_bool))
# Casting ke tipe data lain
print('\nCasting tipe data')
data_int = int(data_bool)  # boolean ke integer
data_float = float(data_bool)  # boolean ke float
data_str = str(data_bool)  # boolean ke string
print('Data =', data_int, ', Tipe =', type(data_int))
print('Data =', data_float, ', Tipe =', type(data_float))
print('Data =', data_str, ', Tipe =', type(data_str))
print('')
