# 2)Write a python program using function to convert Celsius to Fahrenheit.

celcius= int(input("Enter the temperature in celcius which will be converted to fahrenheit = "))
def celcius_to_fahrenheit(celcius):
  fahrenheit =(celcius* 1.8)  + 32
  return(fahrenheit)

celcius_to_fahrenheit(celcius)