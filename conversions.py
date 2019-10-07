class ConversionInputError(Exception):
    pass


def convertCelsiusToKelvin(celsius):
    """
    Function that takes in a float "celsius" and returns the equivalent in kelvin.
    :param celsius: A float that represents a temperature in celsius that will be converted to kelvin.
    :return: kelvin: The converted celsius temperature in kelvin rounded to 2 decimal places.
    """
    # conversion from celsius to kelvin before returning it to caller
    kelvin = float(celsius) + 273.15
    return round(kelvin, 2)


def convertCelsiusToFahrenheit(celsius):
    """
    Function that takes in a float "celsius" and returns the equivalent in fahrenheit.
    :param celsius: A float that represents a temperature in celsius that will be converted to kelvin.
    :return: kelvin: The converted celsius temperature in fahrenheit rounded to 2 decimal places.
    """
    # conversion from celsius to fahrenheit before returning it to caller
    fahrenheit = (float(celsius) * 9/5) + 32
    return round(fahrenheit, 2)


def convertFahrenheitToKelvin(fahrenheit):
    """
    Function that takes in a float "fahrenheit" and returns the equivalent in kelvin.
    :param fahrenheit: A float that represents a temperature in fahrenheit that will be converted to kelvin.
    :return: kelvin: The converted fahrenheit temperature in kelvin rounded to 2 decimal places.
    """
    # conversion from fahrenheit to kelvin before returning it to caller
    kelvin = (float(fahrenheit) + 459.67) * 5/9
    return round(kelvin, 2)


def convertFahrenheitToCelsius(fahrenheit):
    """
    Function that takes in a float "fahrenheit" and returns the equivalent in celsius.
    :param fahrenheit: A float that represents a temperature in fahrenheit that will be converted to celsius.
    :return: celsius: The converted fahrenheit temperature in celsius rounded to 2 decimal places.
    """
    # conversion from fahrenheit to kelvin before returning it to caller
    celsius = (float(fahrenheit) - 32) * 5/9
    return round(celsius, 2)


def convertKelvinToCelsius(kelvin):
    """
    Function that takes in a float "kelvin" and returns the equivalent in celsius.
    :param kelvin: A float that represents a temperature in kelvin that will be converted to celsius.
    :return: celsius: The converted kelvin temperature in celsius rounded to 2 decimal places.
    """
    # conversion from kelvin to celsius before returning it to caller
    celsius = float(kelvin) - 273.15
    return round(celsius, 2)


def convertKelvinToFahrenheit(kelvin):
    """
    Function that takes in a float "kelvin" and returns the equivalent in fahrenheit.
    :param kelvin: A float that represents a temperature in kelvin that will be converted to fahrenheit.
    :return: fahrenheit: The converted kelvin temperature in fahrenheit rounded to 2 decimal places.
    """
    # conversion from kelvin to fahrenheit before returning it to caller
    fahrenheit = (float(kelvin) * 9/5) - 459.67
    return round(fahrenheit, 2)
