import nltk.tokenize as tkn
import re

def custom_tokenize(words):
    new_list = []
    for word in words:
        new_words = []
        if word != ',':
            new_words = word.split(',')

        temp = []
        for new_word in new_words:
            temp2 = re.sub(r"([A-Z])", r" \1", new_word).split()
            [temp.append(l) for l in temp2]
        new_words = temp
        for new_word in new_words:
            s = ''
            for l in new_word:
                if l.isdigit():
                    s += l
            if s != '':
                new_words.remove(new_word)
                new_words.append(s)
        # new_list.append(new_words)
        [new_list.append(w) for w in new_words]
    return new_list


def custom_tokenize2(sntc):
    sntc = sntc.replace(',', ' ')
    sntc = sntc.replace('  ', ' ')
    temp = ''
    for letter in sntc:
        if letter.isupper():
            letter = ' ' + letter
        temp += letter
    temp = temp.replace('  ', ' ')
    print(temp)


custom_tokenize2('1st Main Rd,2nd Cross')
custom_tokenize2('1stMain, 2nd Cr')
# print(custom_tokenize(tkn.word_tokenize('1st Main Rd,2nd Cross')))
# print(custom_tokenize(tkn.word_tokenize('1stMain, 2nd Cr')))




# import nltk.tokenize as t
#
# print(t.word_tokenize('1st Main Rd,2nd Cross'))
