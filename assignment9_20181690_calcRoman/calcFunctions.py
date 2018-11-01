from math import factorial as fact

def factorial(numStr):
    try:
        result =  str(fact(int(numStr)))
    except ValueError:
        result = "숫자를 입력해 주세요."
    return result

def decToBin(numStr):
    try:
        result = bin(int(numStr))[2:]
    except ValueError:
        result = "숫자를 입력해 주세요."
    return result

def binToDec(numStr):
    try:
        result = str(int(numStr, 2))
    except ValueError:
        result = "숫자를 입력해 주세요."
    return result


def decToRoman(numStr):
    try:
        n = int(numStr)
        result = ''

        if n >= 4000:
            result = "4000미만의 수를 입력해 주세요."
            return result

        for value in sorted(romans.keys(), reverse=True):
            while n >= value:
                result += romans[value]
                n -= value

    except ValueError:
        result = "숫자를 입력해 주세요."

    return result


def romanToDec(numStr):
    try:
        s = str(numStr)
        result = 0

        for key in sorted(romans.keys(), reverse=True):
            while s != '':
                if s[0] == romans[key]:
                    result += key
                    s = s[1:]
                elif s[0:2] == romans[key]:
                    result += key
                    s = s[2:]
                else :
                    break


    except ValueError:
        result = "로마숫자를 입력해 주세요."

    return result


romans = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
          100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
          10: 'X', 9: 'IX', 5: 'V', 4: 'IV',
          1: 'I'}