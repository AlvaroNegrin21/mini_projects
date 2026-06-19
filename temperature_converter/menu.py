"""
Temperature Converter (menu)
-------------------------------
Lets the user convert temperatures between Celsius, Fahrenheit,
and Kelvin through an interactive menu. Validates that Kelvin
values are never negative, since 0K is absolute zero.
"""

from temperatures import (
    celsius_to_fahrenheit,
    celsius_to_kelvin,
    fahrenheit_to_celsius,
    fahrenheit_to_kelvin,
    kelvin_to_celsius,
    kelvin_to_fahrenheit,
)


while True:
    print("\n === Temperature Converter ===")
    print("""\nSelect a conversion method:\n
    1. Celsius → Fahrenheit
    2. Celsius → Kelvin
    3. Fahrenheit → Celsius
    4. Fahrenheit → Kelvin
    5. Kelvin → Celsius
    6. Kelvin → Fahrenheit
    7. Exit"""
    )

    option = input("\nChoose an option: ")

    if option == "1":
        celsius = float(input("Enter the temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}ºC is {fahrenheit:.2f}ºF")
        input("\nPress Enter to continue...")

    elif option == "2":
        celsius = float(input("Enter the temperature in Celsius: "))
        kelvin = celsius_to_kelvin(celsius)
        print(f"{celsius}ºC is {kelvin:.2f}K")
        input("\nPress Enter to continue...")

    elif option == "3":
        fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}ºF is {celsius:.2f}ºC")
        input("\nPress Enter to continue...")

    elif option == "4":
        fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
        kelvin = fahrenheit_to_kelvin(fahrenheit)
        print(f"{fahrenheit}ºF is {kelvin:.2f}K")
        input("\nPress Enter to continue...")

    elif option == "5":
        kelvin = float(input("Enter the temperature in Kelvin: "))
        if kelvin < 0:
            print("Kelvin temperature cannot be below 0. Please try again with a value above 0.")
            input("\nPress Enter to continue...")
            continue
        celsius = kelvin_to_celsius(kelvin)
        print(f"{kelvin}K is {celsius:.2f}ºC")
        input("\nPress Enter to continue...")

    elif option == "6":
        kelvin = float(input("Enter the temperature in Kelvin: "))
        if kelvin < 0:
            print("Kelvin temperature cannot be below 0. Please try again with a value above 0.")
            input("\nPress Enter to continue...")
            continue
        fahrenheit = kelvin_to_fahrenheit(kelvin)
        print(f"{kelvin}K is {fahrenheit:.2f}ºF")
        input("\nPress Enter to continue...")

    elif option == "7":
        print("Closing the converter...")
        break

    else:
        print("Invalid option. Please choose a valid one.")