# -*- coding: utf-8 -*-
from collections import OrderedDict
roman_symbols = 'MDCLXVI' 
roman_set = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90, 'L':50, 'XL':40, 'X':10, 'IX':9, 'V':5, 'IV':4, 'I':1}
roman_set = OrderedDict(sorted(roman_set.items(), key=lambda t: t[1]))


def roman_to_int(roman):
    global roman_set
    roman = roman.upper()
    integ = 0
    minus = 0 #Denne variabelen er strengt tatt ikke nødvendig lenger
              #hvis vi velger å ikke godta ukorrekte romerske tall som f.eks 
              #DCCCCLX (960) fordi det burde blitt skrevet CMLX
    for r, i in enumerate(roman):
        #print "r = {}, i = {}, int = {}, minus = {}".format(r, i, int, minus) """debugging"""
        try:
            if roman_set[roman[r + 1]] > roman_set[i]:
                minus = roman_set[i]
                continue
        except IndexError:
            pass
        integ += (roman_set[i] - minus)
        minus = 0
    if not (0 < integ < 5000):
        raise ValueError("Number is likely out of range. The roman numeral must have a value between 1 and 4999.")
    return integ

def int_to_roman(int):
    if not (0 < int < 5000):
        raise ValueError("Number is out of range. The roman numeral must have a value between 1 and 4999.")
    global roman_set
    roman_set = OrderedDict(reversed(sorted(roman_set.items(), key=lambda t: t[1])))
    roman = ''
    for r, i in roman_set.items():   #For hvert sett med tilhørende romerske tall og integere:
           #print "r = {}, i = {}, int = {}, roman = {}".format(r, i, int, roman) """debugging"""
           while int >= i: #Når input-verdi er større enn en integerverdi i roman_set
                int -= i   #fjernes integerverdien fra input-verdi"""
                roman += r   #og det samsvarende romerske tallet legges inn i en variabel
    return roman
    
def roman_add(roman1, roman2):
    roman1 = roman1.upper()
    roman2 = roman2.upper()
    roman1 = roman_expand(roman1)
    roman2 = roman_expand(roman2)
    combined_roman = roman1 + roman2
    
    temp_roman = ''
    temp_roman += combined_roman
    global roman_symbols
    """Vi sorterer den kombinerte romerske numeralen etter
        en liste med romerske symboler i rekkefølge"""
    listed_roman = sorted(temp_roman, key=roman_symbols.index)
    new_roman = ''.join(listed_roman)
    
    new_roman = roman_combine(new_roman)
    
    return new_roman
    
    

def roman_expand(num):
    """Vi bruker funksjonen roman_expand til å bytte ut alle negative
    verdier fra begge numeralene med utvidete positive verdier """
    num = num.replace('CM', 'DCCCC')
    num = num.replace('CD', 'CCCC')
    num = num.replace('XC', 'LXXXX')
    num = num.replace('XL', 'XXXX')
    num = num.replace('IX', 'VIIII')
    num = num.replace('IV', 'IIII')
    return num

def roman_combine(num):
    """Vi bruker funksjonen roman_combine til å trekke sammen
        det endelige numeralet, også med negative verdier"""
    num = num.replace('IIIII', 'V')
    num = num.replace('VV', 'X')
    num = num.replace('XXXXX', 'L')
    num = num.replace('LL', 'C')
    num = num.replace('CCCCC', 'D')
    num = num.replace('DD', 'M')
    num = num.replace('VIIII', 'IX')
    num = num.replace('IIII', 'IV')
    num = num.replace('LXXXX', 'XC')
    num = num.replace('XXXX', 'XL')
    num = num.replace('DCCCC', 'CM')
    num = num.replace('CCCC', 'CD')
    return num

print 'First you get to convert a roman numeral to an arabic number.'
print 'Type in a roman numeral with a value between I and MMMMCMXCIX:'    
roman_toInt = raw_input('')
print roman_to_int(roman_toInt)    
print 'Now we will convert an arabic number to a roman numeral.'
print 'Type in a number with a value between 1 and 4999:'
int_toRoman = raw_input('')
print int_to_roman(int(int_toRoman))


print 'To conclude we will add two roman numerals together without converting to arabic numbers.'
print 'Type in the first roman numeral:'
roman_add1 = raw_input('')
print 'Type in the second roman numeral:'
roman_add2 = raw_input('')

print roman_add(roman_add1, roman_add2)


def test():
    assert roman_to_int('IV') == 4
    assert roman_to_int('VI') == 6
    assert roman_to_int('DCCLXVII') == 767
    assert roman_to_int('MMMMDCCCCLXXXXVIIII') == 4999
    assert roman_to_int('MMMMCMXCIX') == 4999
    assert int_to_roman(4) == 'IV'
    assert int_to_roman(6) == 'VI'
    assert int_to_roman(767) == 'DCCLXVII'
    assert int_to_roman(4999) == 'MMMMCMXCIX'
    assert roman_expand('MMMMCMXCIX') == 'MMMMDCCCCLXXXXVIIII'
    assert roman_combine('MMMMDCCCCLXXXXVIIII') == 'MMMMCMXCIX'
    assert roman_add('MCMDXIC', 'DCCLXXVIII') == 'MMMLXXXIX'
    return "Tests have been completed."
print test()
    