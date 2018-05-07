from string import ascii_lowercase

string = 'abc'
string = 'The quick brown fox jumps over the lazy dog'
string = string.lower()

d = {}

for s in string:
    d[s] = string.count(s)

for c in ascii_lowercase:
    v = d.get(c)
    if v is None:
        print("Not a pangram")
        exit(0)

print("Pangram")
