def text2int(textnum, numwords={}):
    if not numwords:
        units = [
            "ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь",
            "девять", "десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать",
            "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать",
        ]

        tens = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят",
                "девяносто"]

        scales = ["сто", "тысяч", "миллион", "миллиард", "триллион"]

        numwords["и"] = (1, 0)
        for idx, word in enumerate(units):    numwords[word] = (1, idx)
        for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
        for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    resStr = ""
    for word in textnum.split():
        if word not in numwords:
            if resStr.replace(' ', '') == "":
                if result + current == 0:
                    resStr = word
                else:
                    resStr = str(result + current) + " " + word
            else:
                if result + current == 0:
                    resStr = resStr + " " + word
                else:
                    resStr = resStr + " " + str(result + current) + " " + word
        else:
            scale, increment = numwords[word]
            current = current * scale + increment
            if scale > 100:
                result += current
                current = 0
    if resStr == "":
        if result + current == 0:
            return ""
        else:
            return result + current
    else:
        return resStr


print(text2int("test семьдесят тысяч пятьдесят три тест"))
print(text2int("семь тысяч пятьдесят три"))
