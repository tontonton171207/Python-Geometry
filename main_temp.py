from temperature.celsius import to_fahrenheit as to_f
from temperature.fahrenheit import to_celsius as to_c

cel_1 = float(input("nhap do c: "))
fah_1 = to_f.cel_to_fah(cel_1)
print(fah_1, " la do f ")

fah_2 = float(input("nhap do f: "))
cel_2 = to_c.fah_to_cel(fah_2)
print(cel_2, " la do c ")

