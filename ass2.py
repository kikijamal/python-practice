# ass2.py
# Celcius to farenheit converter

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Input: Temperature value and unit from the user
temp = float(input("Enter the temperature: "))
unit = input("Is the temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

# Conversion and output
if unit == "C":
    print(f"{temp}°C is equal to {celsius_to_fahrenheit(temp)}°F")
elif unit == "F":
    print(f"{temp}°F is equal to {fahrenheit_to_celsius(temp)}°C")
else:
    print("Invalid input! Please enter 'C' for Celsius or 'F' for Fahrenheit.")
