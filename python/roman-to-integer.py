def roman_to_integer(s):
    roman_value = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000
    }
    num = 0

    special_list = ["IV", "IX", "XL", "XC", "CD", "CM"]

    for i in special_list:
        if i in s:
            num =  num+roman_value[i]
            s=s.replace(i,"")
    for i in s:
        num = num + roman_value[i]
    return(num)

roman_to_integer("VII")