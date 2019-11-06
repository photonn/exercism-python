def convert(number):
    drop = ""
    if number%3 == 0:
        drop = drop + "Pling"
    if number%5 == 0:
        drop = drop + "Plang"
    if number%7 == 0:
        drop = drop + "Plong"
    if drop=="":
        return str(number)
    else:
        return drop

