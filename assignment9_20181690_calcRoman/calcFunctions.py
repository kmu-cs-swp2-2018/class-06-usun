from math import factorial as fact

def factorial(numStr):
    try:
        n = int(numStr)
        r = str(fact(n))
    except ValueError:
        r = "숫자를 입력해 주세요."
    return r

def decToBin(numStr):
    try:
        n = int(numStr)
        r = bin(n)[2:]
    except ValueError:
        r = "숫자를 입력해 주세요."
    return r

def binToDec(numStr):
    try:
        n = int(numStr, 2)
        r = str(n)
    except ValueError:
        r = "숫자를 입력해 주세요."
    return r


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
        N = 0
        result = ""

        for i in range(len(s)):
            if s[i] == 'M':
                N += 1000
            elif s[i:i + 2] == 'CM':
                N += 900
            elif s[i] == 'D':
                N += 500
            elif s[i:i + 2] == 'CD':
                N += 400
            elif s[i] == 'C':
                N += 100
            elif s[i:i + 2] == 'XC':
                N += 90
            elif s[i] == 'L':
                N += 50
            elif s[i:i + 2] == 'XL':
                N += 40
            elif s[i] == 'X':           # 9 -> IX 인데, 이걸 다시 romanToDec하면 19(XIX)됨
                N += 10                 # 19 -> XIX  romanToDec 29(XXIX)...왜지.......
                continue
            elif s[i:i + 2] == 'IX':
                N += 9
                i += 1
                continue
            elif s[i] == 'V':
                N += 5
            elif s[i:i + 2] == 'IV':
                N += 4
            elif s[i] == 'I':
                N += 1
            else :        # 기호, 숫자를 입력했을 경우
                N = "로마숫자만 변환 가능 합니다."

            result = N

    except ValueError:    # 빈공간 입력해도 result값이 안나옴.. 왜지..ㅠㅜ
        result = "로마숫자를 입력해 주세요."

    return result


romans = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
          100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
          10: 'X', 9: 'IX', 5: 'V', 4: 'IV',
          1: 'I'}