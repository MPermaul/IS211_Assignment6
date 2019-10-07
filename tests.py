import conversions
import unittest


class ConversionTests(unittest.TestCase):
    """Function convertCelsiusToKelvin should return known results when passed known inputs"""

    # temps store by celsius, fahrenheit, kelvin
    known_temps = (
        (0.0, 32.00, 273.15),
        (33.0, 91.40, 306.15),
        (100.0, 212.00, 373.15),
        (500.0, 932.00, 773.15),
        (-100.0, -148.00, 173.15)
    )

    def test_celsius_to_kelvin(self):
        """Check to make sure that celsius is converting to kelvin using known inputs"""
        for celsius, fahrenheit, kelvin in self.known_temps:
            print('Verifying that {} degrees Celsius equals {} Kelvin.'.format(celsius, kelvin))
            result = conversions.convertCelsiusToKelvin(celsius)
            self.assertEqual(kelvin, result)

    def test_celsius_to_fahrenheit(self):
        """Check to make sure that celsius is converting to fahrenheit using known inputs"""
        for celsius, fahrenheit, kelvin in self.known_temps:
            print('Verifying that {} degrees Celsius equals {} fahrenheit.'.format(celsius, fahrenheit))
            result = conversions.convertCelsiusToFahrenheit(celsius)
            self.assertEqual(fahrenheit, result)

    def test_fahrenheit_to_kelvin(self):
        """Check to make sure that fahrenheit is converting to kelvin using known inputs"""
        for celsius, fahrenheit, kelvin in self.known_temps:
            print('Verifying that {} degrees Fahrenheit equals {} Kelvin.'.format(fahrenheit, kelvin))
            result = conversions.convertFahrenheitToKelvin(fahrenheit)
            self.assertEqual(kelvin, result)

    def test_fahrenheit_to_celsius(self):
        """Check to make sure that fahrenheit is converting to celsius using known inputs"""
        for celsius, fahrenheit, kelvin in self.known_temps:
            print('Verifying that {} degrees Fahrenheit equals {} Celsius.'.format(fahrenheit, celsius))
            result = conversions.convertFahrenheitToCelsius(fahrenheit)
            self.assertEqual(celsius, result)

    def test_kelvin_to_celsius(self):
        """Check to make sure that kelvin is converting to celsius using known inputs"""
        for celsius, fahrenheit, kelvin in self.known_temps:
            print('Verifying that {} degrees Kelvin equals {} Celsius.'.format(kelvin, celsius))
            result = conversions.convertKelvinToCelsius(kelvin)
            self.assertEqual(celsius, result)

    def test_kelvin_to_fahrenheit(self):
        """Check to make sure that kelvin is converting to fahrenheit using known inputs"""
        for celsius, fahrenheit, kelvin in self.known_temps:
            print('Verifying that {} degrees Kelvin equals {} Fahrenheit.'.format(kelvin, fahrenheit))
            result = conversions.convertKelvinToFahrenheit(kelvin)
            self.assertEqual(fahrenheit, result)


if __name__ == '__main__':
    unittest.main()
