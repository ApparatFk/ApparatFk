def int_to_roman(num):
    
    val_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    roman_numeral = ''
    
  
    for value, numeral in val_map:  #doble variable for?
        while num >= value:
            num -= value
            roman_numeral += numeral

    return roman_numeral


number = int(input("Enter an integer to convert to a Roman numeral: "))


print(f"The integer {number} converts to the Roman numeral {int_to_roman(number)}.")
