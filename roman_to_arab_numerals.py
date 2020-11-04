def roman_to_arab(roman):
    total = 0
    arab = 0
    test = 0
    count = 0
    
    for i in roman:
        if i == 'I':
            arab = 1
        elif i == 'V':
            arab = 5
        elif i == 'X':
            arab = 10
        elif i == 'L':
            arab = 50
        elif i == 'C':
            arab = 100
        elif i == 'D':
            arab = 500
        elif i == 'M':
            arab = 1000    
            
        if count == 0:
            test = arab
            
        if arab <= test:
            total += arab
            count += 1
            test = arab
        else:
            total -= arab
            count += 1
            test = arab
   
    return abs(total)

print(roman_to_arab('XXVI'))




    


        