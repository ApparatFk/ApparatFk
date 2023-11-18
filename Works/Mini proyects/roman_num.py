def roman_to_int():
    
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, "H":5000}
   
    s = input("Numero romano: ").upper()
    
    prev_value = 0
    total = 0
    
   
    for char in reversed(s):  
        
        value = roman_map[char]
        
        if value < prev_value:
            total -= value
       
        else:
            total += value
            prev_value = value
    
   
    print(f"ROMANO= {s} NUMERO= {total}.")


roman_to_int()