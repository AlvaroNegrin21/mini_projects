"""
Temperature conversion functions between Celsius, Fahrenheit,
and Kelvin.

Formulas:
    °F = (°C · 9/5) + 32
    K  = °C + 273.15
    °C = (°F - 32) · 5/9
    °C = K - 273.15
"""


def celsius_to_fahrenheit(celsius):
    """Converts a temperature from Celsius to Fahrenheit.

    Args:
        celsius (float): temperature in Celsius.

    Returns:
        float: temperature in Fahrenheit.
    """
    return (celsius * 9/5) + 32


def celsius_to_kelvin(celsius):
    """Converts a temperature from Celsius to Kelvin.

    Args:
        celsius (float): temperature in Celsius.

    Returns:
        float: temperature in Kelvin.
    """
    return celsius + 273.15


def fahrenheit_to_celsius(fahrenheit):
    """Converts a temperature from Fahrenheit to Celsius.

    Args:
        fahrenheit (float): temperature in Fahrenheit.

    Returns:
        float: temperature in Celsius.
    """
    return (fahrenheit - 32) * 5/9


def fahrenheit_to_kelvin(fahrenheit):
    """Converts a temperature from Fahrenheit to Kelvin.

    Args:
        fahrenheit (float): temperature in Fahrenheit.

    Returns:
        float: temperature in Kelvin.
    """
    return (fahrenheit - 32) * 5/9 + 273.15


def kelvin_to_celsius(kelvin):
    """Converts a temperature from Kelvin to Celsius.

    Args:
        kelvin (float): temperature in Kelvin.

    Returns:
        float: temperature in Celsius.
    """
    return kelvin - 273.15


def kelvin_to_fahrenheit(kelvin):
    """Converts a temperature from Kelvin to Fahrenheit.

    Args:
        kelvin (float): temperature in Kelvin.

    Returns:
        float: temperature in Fahrenheit.
    """
    return (kelvin - 273.15) * 9/5 + 32