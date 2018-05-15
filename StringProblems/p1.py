import textwrap
import collections
import string as st

a = 'hello'
# print(len(a))

b = {}
keys = b.keys()
for letter in a:
    if letter in keys:
        b[letter] += 1
    else:
        b[letter] = 1
# print(b)

string = 'hello'
# if len(string) < 2:
#     print('Empty String')
# else:
#     c = string[:2] + string[-2:]
#     print(c)

string = 'restart'
f_char = string[0]
string = string.replace(f_char, '$')
string = f_char + string[1:]
# print(string)

d = 'abc'
e = 'xyz'
ff_char = d[:2]
fs_char = e[:2]
d = fs_char + d[2:]
e = ff_char + e[2:]
f = d + ' ' + e
# print(f)

g = 'string'
# if len(g) > 2 and not g.endswith('ing'):
#     print('{}ing'.format(g))
# elif len(g) > 2 and g.endswith('ing'):
#     print('{}ly'.format(g))
# else:
#     print(g)

h = 'The lyrics is not that poor!'
not_index = h.index('not')
poor_index = h.index('poor')
if poor_index > not_index:
    h = h[:not_index] + 'good' + h[poor_index+4:]
# print(h)

i = ['hello', 'world', 'sid']
longest = 0
for word in i:
    l = len(word)
    if l > longest:
        longest = l
# print(longest)

j = 'hello'
char_index_to_remove = 1
j = j[:char_index_to_remove] + j[char_index_to_remove+1:]
# print(j)


def remove_odd_chars(k):
    m = k[0::2]
    return m


# print(remove_odd_chars('abcd'))

k = 'hello-world/from,sid'
# print(k.rsplit(sep='-', maxsplit=1)[0])

l = 'hello\n'
# print(l.rstrip())

sample_text = '''Python is a widely used high-level, general-purpose, interpreted,
  dynamic programming language. Its design philosophy emphasizes
  code readability, and its syntax allows programmers to express
  concepts in fewer lines of code than possible in languages such
  as C++ or Java.
  '''
# print(textwrap.fill(sample_text, width=30))

sample_text = '''
    Python is a widely used high-level, general-purpose, interpreted,
    dynamic programming language. Its design philosophy emphasizes
    code readability, and its syntax allows programmers to express
    concepts in fewer lines of code than possible in languages such
    as C++ or Java.
    '''
sample_text = textwrap.dedent(sample_text)
wrapped = textwrap.fill(sample_text, width=50)
# print(textwrap.indent(wrapped, '> '))

# print('{:.2f}'.format(21.15789))

# print('{:+.2f}'.format(-21.15789))

# print('{:.0f}'.format(21.15789))

# print('{:0>3d}'.format(5))
#
# print('{:*<3d}'.format(51))

# print('{:,}'.format(3126758))

# print('{:.2%}'.format(.25))

# print(20)
# print('{:<10d}'.format(20))
# print('{:10d}'.format(20))
# print('{:^10d}'.format(20))

text = 'The quick brown fox jumps over the lazy dog.'
# print(' '.join(text.split(' ')[::-1]))

n = collections.defaultdict(int)
string = 'hello'
for i in string:
    n[i] += 1
# print(n)

# for i, c in enumerate(string):
#     print(i, c)

text = 'The quick brown fox jumps over the lazy dog'
alphabets = set(st.ascii_lowercase)
# if set(text.lower()) >= alphabets:
#     print(True)
# else:
#     print(False)

text = '15,201.50'
text = text.translate(text.maketrans('.,', ',.'))
# print(text)

text = 'helloo'
vowels = 'aeiouAEIOU'
print('Count:', len([letter for letter in text if letter in vowels]))
print('Letters:', [letter for letter in text if letter in vowels])
