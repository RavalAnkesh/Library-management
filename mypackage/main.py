import valueswap 
import arithmetic
from unit_conversion import *
from temprature import *

a, b = 5, 10
print("Original:", a, b)

a, b = valueswap.swap_with_temp(a, b)
print("Swap with temp:", a, b)
a , b = 5 ,10
a, b = valueswap.swap_with_tuple(a, b)
print("Swap with tuple:", a, b)
a , b = 5 ,10
a, b = valueswap.swap_with_arithmetic(a, b)
print("Swap with arithmetic:", a, b)
a , b = 5 ,10
a, b = valueswap.swap_with_xor(a, b)
print("Swap with XOR:", a, b)
lst = [5, 10]
swapped_list = valueswap.swap_in_list(lst)
print("Swap in list:", swapped_list)
a, b = valueswap.swap_with_function(5, 10)
print("Swap with function:", a, b)




print(" ")
meters = 1500
print(f"{meters} meters = {meters_to_kilometers(meters)} kilometers.")
print(f"{meters} meters = {meters_to_centimeters(meters)} centimeters.")
print(f"{meters} meters = {meters_to_millimeters(meters)} millimeters.")
kilometers = 1.5
print(f"{kilometers} kilometers = {kilometers_to_meters(kilometers)} meters.")
centimeters = 150
print(f"{centimeters} centimeters = {centimeters_to_meters(centimeters)} meters.")
millimeters = 1500
print(f"{millimeters} millimeters = {millimeters_to_meters(millimeters)} meters.")




print(" ")
celsius = 25
print(f"{celsius} Celsius = {celsius_to_fahrenheit(celsius)} Fahrenheit.")    
fahrenheit = 77
print(f"{fahrenheit} Fahrenheit = {fahrenheit_to_celsius(fahrenheit)} Celsius .")   
kelvin = 298.15
print(f"{kelvin} Kelvin = {kelvin_to_celsius(kelvin)} Celsius .")   
print(f"{celsius} Celsius  = {celsius_to_kelvin(celsius)} Kelvin.")
print(f"{fahrenheit} Fahrenheit = {fahrenheit_to_kelvin(fahrenheit)} Kelvin.")
print(f"{kelvin} Kelvin = {kelvin_to_fahrenheit(kelvin)} Fahrenheit.")

 
print(" ")
n1=5
n2=4
print("Addition:",arithmetic.add(n1,n2))
print("Subtraction:",arithmetic.sub(n1,n2))
print("Multiplication:",arithmetic.mul(n1,n2))
print("Division:",arithmetic.div(n1,n2))