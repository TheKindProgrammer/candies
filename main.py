def romanToInt(s: str):
    mapping = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        'C': 100,
        'D': 500,
        "M": 1000
    }

    for char in s:
        if char not in mapping.keys():
            raise KeyError(f'invalid char found: {char}')


    s = s.replace("IV","IIII")
    s = s.replace("IX", "VIIII")
    s = s.replace("XL", "XXXX")
    s = s.replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC")
    s = s.replace("CM", "DCCCC")

    soln = 0
    for char in s:
        soln += mapping[char]

    return soln

print(romanToInt('DCCXVI'))
