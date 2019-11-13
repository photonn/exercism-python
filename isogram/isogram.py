
import string as cadenas
def is_isogram(string):
    string = string.lower()
    for char in string:
        charcount = 0
        for char2 in string:
            if char == char2 and char in cadenas.ascii_lowercase:
                charcount = charcount + 1
        if charcount > 1:
            return False
    return True