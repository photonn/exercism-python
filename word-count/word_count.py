import string
def count_words(sentence):
    worddict = {}
    splitedsentence = sentence.split( )
    for word in splitedsentence:
        cleanword = []
        for char in word.lower():
            if char.isalnum() or char == "-":
                cleanword.append(char)
        joined = ''.join(cleanword)
        if len(joined) >= 1 and joined in worddict:
            worddict[joined] = worddict[joined] + 1
        else:
            worddict[joined] = 1
    print(worddict)
    return worddict

count_words ("capullo esto esto5 esto^^ 456 es, es lo   que pasa's")
    
    #comprobar la funcion format de la claase string y las expresiones regex.
    #tiene que haber una forma mas sencilla de atacar esto...