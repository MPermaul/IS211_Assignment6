import conversions_refactored
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

    # distances stored by meters, miles, yards
    known_distance = (
        (1609.344, 1.00, 0),
        (80467.200, 50.00, 0),
        (806281.344, 501.00, 0),
        (1166774.400, 725.00, 0),
        (1607734.656, 999.00, 0)
    )

    # list of known units
    known_dist_units = ['meters', 'miles', 'yards']
    known_temp_units = ['celsius', 'fahrenheit', 'kelvin']

    def test_same_distance_unit(self):
        """Check to see if distance unit inputs being the same returns a known value"""
        for unit in self.known_dist_units:
            print('Check to see if value {} is returned when both distance units passed in are {}.'.format(1.00, unit))
            result = conversions_refactored.convert(unit, unit, 1.00)
            self.assertEqual(1.00, result)

    def test_same_temperature_unit(self):
        """Check to see if temperature unit inputs being the same returns a known value"""
        for unit in self.known_temp_units:
            print('Check to see if value {} is returned when both temp units passed in are {}.'.format(1.00, unit))
            result = conversions_refactored.convert(unit, unit, 1.00)
            self.assertEqual(1.00, result)

    def test_for_invalid_unit(self):
        """Check to see if an error is raised when an invalid units input is entered"""
        print('A blank unit should raise an error.'.format(''))
        self.assertRaises(conversions_refactored.ConversionNotPossible, conversions_refactored.convert('', 'kelvin', 1))

    def test_temperature_conversion(self):
        """Check to see if temperature unit conversion returns a known value"""
        for celsius, fahrenheit, kelvin in self.known_temps:
            print('Verifying that {} degrees Celsius equals {} Kelvin.'.format(celsius, kelvin))
            result = conversions.convertCelsiusToKelvin(celsius)
            self.assertEqual(kelvin, result)

if __name__ == '__main__':
    unittest.main()
