class ConversionNotPossible(Exception):
    pass


def convert(fromUnit, toUnit, value):
    """
    Function that will take in value of one unit and convert it to another.
    :param fromUnit: A string that represents the unit that we are converting from.
    :param toUnit: A string that represents the unit that we are converting to.
    :param value: A float representing the value of the fromUnit that we want to convert.
    :return: converted: A float representing the converted value.
    """

    # lists containing the units that are convertible within the scope of this application
    units_dist = ['meters', 'miles', 'yards']
    units_temp = ['celsius', 'fahrenheit', 'kelvin']

    # store inputs from caller in lowercase version, and value as a float
    lower_from = fromUnit.lower()
    lower_to = toUnit.lower()
    val_to_convert = float(value)

    try:
        # check to see if passed in units are the same and both found in the distance units list
        if lower_from == lower_to and (lower_from in units_dist and lower_to in units_dist):
            return val_to_convert
        # check to see if passed in units are the same and both found in temperature units list
        elif lower_from == lower_to and (lower_from in units_temp and lower_to in units_temp):
            return val_to_convert

        # check to see if celsius was passed in and do the conversion
        elif lower_from == 'celsius' and lower_to == 'fahrenheit':
            fahrenheit = (val_to_convert * 9/5) + 32
            return round(fahrenheit, 2)
        elif lower_from == 'celsius' and lower_to == 'kelvin':
            kelvin = val_to_convert + 273.15
            return round(kelvin, 2)

        # check to see if fahrenheit was passed in and do the conversion
        elif lower_from == 'fahrenheit' and lower_to == 'celsius':
            celsius = (val_to_convert - 32) * 5/9
            return round(celsius, 2)
        elif lower_from == 'fahrenheit' and lower_to == 'kelvin':
            kelvin = (val_to_convert + 459.67) * 5/9
            return round(kelvin, 2)

        # check to see if kelvin was passed in and do conversion
        elif lower_from == 'kelvin' and lower_to == 'celsius':
            celsius = val_to_convert - 273.15
            return round(celsius, 2)
        elif lower_from == 'kelvin' and lower_to == 'fahrenheit':
            fahrenheit = (val_to_convert * 9/5) - 459.67
            return round(fahrenheit, 2)

        # check to see if meters was passed in and do conversion
        elif lower_from == 'meters' and lower_to == 'miles':
            miles = val_to_convert/1609.344
            return round(miles, 6)
        elif lower_from == 'meters' and lower_to == 'yards':
            yards = val_to_convert * 1.0936
            return round(yards, 4)

        # check to see if miles was passed in
        elif lower_from == 'miles' and lower_to == 'meters':
            meters = val_to_convert * 1609.344
            return round(meters, 4)
        elif lower_from == 'miles' and lower_to == 'yards':
            yards = val_to_convert * 1760
            return round(yards, 4)

        # check to see if yards was passed in
        elif lower_from == 'yards' and lower_to == 'meters':
            meters = val_to_convert * 0.9144
            return round(meters, 4)
        elif lower_from == 'yards' and lower_to == 'miles':
            miles = val_to_convert / 1760
            return round(miles, 4)

        # raise an error as all working cases have now passed, no other conversion can be done
        else:
            raise ConversionNotPossible

    # print message if there is a ConversionNotPossible error
    except ConversionNotPossible:
        print('\tThere is an error with a passed in units!')

