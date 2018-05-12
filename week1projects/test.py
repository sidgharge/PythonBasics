from nltk.tokenize import word_tokenize, sent_tokenize


def p(text):
    print(word_tokenize(text))


p('1st Main Rd,2nd Cross')
p('1st Main Road, 2nd Cross')
p('1stMain, 2nd Cr')
p('1st Main2nd Cross')
