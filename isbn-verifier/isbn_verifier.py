import re
def is_valid(isbn):
    positionvalues = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    totalsum=0
    if not re.match(r"[0-9]-[0-9]{3}-[0-9]{5}-[0-9X]",isbn) and not (re.match(r"[0-9]{9}[0-9X]",isbn) and len(isbn)<=10):
        return False
    isbn = re.sub('-','',isbn)
    if isbn[9] == "X":
        isbn = isbn[0:9]
        totalsum = sum(int(a)*b for a,b in zip(isbn,positionvalues))+10
    else:
        isbn = isbn[0:10]
        totalsum =  sum(int(a)*b for a,b in zip(isbn,positionvalues))
    return True if totalsum % 11 == 0 else False