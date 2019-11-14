import re
def abbreviate(words):
    words = re.findall(r"([a-z]+[']?[a-z]+|\d|[a-z]+)", words.lower())
    return ''.join([word[0] for word in words]).upper()