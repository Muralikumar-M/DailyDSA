'''Roman To Integer - 19th January 2025'''

'''Solution 1: Logic Only.'''

def roman_to_integer(roman: str) -> int:
    roman_value_json = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    integer_value = 0
    roman_length = len(roman)
    for i in range(roman_length):
        ## Neglating the last elements to just add up their int value and avoid index error.
        ## Conditions are happened based on the problem statement given.
        if (i != roman_length-1) and (roman[i] == 'I' and roman[i+1] in ['V', 'X'] or roman[i] == 'X' and roman[i+1] in ['L', 'C'] or 
            roman[i] == 'C' and roman[i+1] in ['D', 'M']):
            integer_value -= roman_value_json[roman[i]]
        else:
            integer_value += roman_value_json[roman[i]]

    return integer_value

print(roman_to_integer("III"))
print(roman_to_integer("LVIII"))
print(roman_to_integer("MCMXCIV"))
print(roman_to_integer("IV"))


'''Solution 2: Logic + Problem Specific Information.'''

'''
Problem Information:
    1. According to Roman Numeral Rules, a smaller numeral cannot appear before a larger numeral 
       unless it represents a valid subtraction combination, which are the conditions that we checked 
       above (IV, IX, XL, XC, CD, CM).
    2. So instead of checking each 6 combinations, we can simply check whether the numeral value of
       current element is less than the next element, substract the numeral value of current element else
       add the numeral value.
'''

def roman_to_integer(roman: str) -> int:
    roman_value_json = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    integer_value = 0
    roman_length = len(roman)
    for i in range(roman_length):
        ## Neglating the last elements to just add up their int value and avoid index error.
        ## Conditions are based on the problem's fact.
        if (i != roman_length-1 and roman_value_json[roman[i]] < roman_value_json[roman[i+1]]):
            integer_value -= roman_value_json[roman[i]]
        else:
            integer_value += roman_value_json[roman[i]]

    return integer_value

print(roman_to_integer("III"))
print(roman_to_integer("LVIII"))
print(roman_to_integer("MCMXCIV"))
print(roman_to_integer("IV"))