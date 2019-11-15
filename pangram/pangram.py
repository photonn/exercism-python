def is_pangram(sentence):
    alphabet = [chr(x) for x in range(ord('a'), ord('z') + 1)]
    return True if not [False for char in alphabet if char not in sentence.lower() and char.isalpha()] else False
