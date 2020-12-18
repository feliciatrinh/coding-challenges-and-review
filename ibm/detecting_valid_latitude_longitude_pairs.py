"""
Input: list of strings that may represent latitude/longitude pairs
Output: "Valid" or "Invalid" for each test

A string (X, Y) is considered valid if following criteria are met:
- string starts with a '(', has a comma after X and ends with a ')'
- there is no space b/w the opening parenthesis and the first character of X
- there is no space b/w the comma and the last character of X
- one space b/w the comma and the first character of Y
- no space b/w Y and closing parenthesis
- X and Y are decimal numbers and may be preceded by a sign
- there are no leading zeros
- no other characters allowed in X or Y
-90 <= X <= 90 and -180 <= Y <= 180

I'm unsure is 0 or 0.0 is considered valid or not.
From the custom test cases I tried, it looked like they would be considered invalid.

More testcases
(-127, -48)
(-127.560528, -48.560528)
(-97, -282)
(-97.354318, -282.354318)
(-66, -43)
(-66.435670, -43.435670)
(-146, -101)
(-146.725709, -101.725709)
(-14, -113)
(-14.19976, -113.19976)

Invalid
Invalid
Invalid
Invalid
Valid
Valid
Invalid
Invalid
Valid
Valid

(-47, -91)
(-47.153089, -91.153089)
(-37, -49)
(-37.561193, -49.561193)
(-114, -80)
(-114.756642, -80.756642)
(-20, -20)
(-20.509733, -20.509733)
(-119, -9)
(-119.168921, -9.168921)
(-95, -166)
(-95.996571, -166.996571)
(-73, -125)
(-73.368028, -125.368028)
(-28, -193)
(-28.52855, -193.52855)
(-43, -198)
(-43.556598, -198.556598)
(-128, -6)
(-128.772318, -6.772318)

Valid
Valid
Valid
Valid
Invalid
Invalid
Valid
Valid
Invalid
Invalid
Invalid
Invalid
Valid
Valid
Invalid
Invalid
Invalid
Invalid
Invalid
Invalid
"""


def is_valid(coordinates):
    """
    Runtime: O(N*M), Space O(1) where N is the number of coordinate pairs in coordinates and M is average length of each
    """
    import re

    result = []
    for coord in coordinates:
        if not re.match(r'^\([+-]?([0-9]+|([0-9]+\.[0-9]+)), [+-]?([0-9]+|([0-9]+\.[0-9]+))\)', coord):
            result.append('Invalid')
        else:
            # Check the numbers themselves
            x, y = coord.split(',')
            x = x[1:]
            y = y[:-1]
            float_x = float(x)
            float_y = float(y)
            if x[0] == '-' or x[0] == '+':
                x = x[1:]
            if y[0] == '-' or y[0] == '+':
                y = y[1:]
            if not (-90 <= float_x <= 90 and -180 <= float_y <= 180):
                result.append('Invalid')
            # Check for leading zeros
            elif (len(x) - len(x.lstrip('0')) > 0) or (len(y) - len(y.lstrip('0')) > 0):
                result.append('Invalid')
            else:
                result.append('Valid')
    return result


def is_valid_alt(coordinates):
    """
    Regex one-liner, but broken up into sub-regex expressions so it makes more sense
    Runtime: O(N*M), Space O(1) where N is the number of coordinate pairs in coordinates and M is average length of each
    """
    import re

    sign = '[+-]?'
    # the ? makes it so that you can have 90 or 90.2 but not 90. and not .92
    decimals = '(\.[0-9]+)?'
    # the ? makes it so that you can have .0 or 90 but not 90. and not .90
    zeros = '(\.0+)?'
    # Something like signed or unsigned 90.000 or two digit decimal or one digit decimal or non decimal
    latitude = '{}(90{}|[1-8]\d{}|\d{})'.format(sign, zeros, decimals, decimals)
    # Something like signed or unsigned 180.000 or three digit decimal or two digit decimal or one digit decimal
    # or non decimal
    longitude = '{}(180{}|1[0-7]\d{}|[1-9]\d{}|\d{})'.format(sign, zeros, decimals, decimals, decimals)
    pattern = '\({}, {}\)'.format(latitude, longitude)
    pattern = re.compile(pattern)
    result = []
    for coord in coordinates:
        if not re.match(pattern, coord):
            result.append('Invalid')
        else:
            result.append("Valid")
    return result


def test(function):
    assert function(['(90, 180)', '(+90, -180)', ' (90, 180)', '(90.0, 180.1)', '(85S, 95W)']) \
           == ['Valid', 'Valid', 'Invalid', 'Invalid', 'Invalid']
    assert function([(75, 180),
                     (+90.0, -147.45),
                     (77.11112223331, 149.99999999),
                     (+90, +180),
                     (90, 180),
                     (-90.00000, -180.0000),
                     (75, 280),
                     (+190.0, -147.45),
                     (77.11112223331, 249.99999999),
                     (+90, +180.2),
                     (90., 180.),
                     (-090.00000, -180.0000)]) == ['Valid',
                                                   'Valid',
                                                   'Valid',
                                                   'Valid',
                                                   'Valid',
                                                   'Valid',
                                                   'Invalid',
                                                   'Invalid',
                                                   'Invalid',
                                                   'Invalid',
                                                   'Invalid',
                                                   'Invalid']


functions = [is_valid, is_valid_alt]

