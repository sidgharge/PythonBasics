class StringValidator:

    def validate(self, string):
        prev = ''
        for c in string:
            if prev == '{' and not c == '}':
                return False
            elif prev == '[' and not c == ']':
                return False
            elif prev == '(' and not c == ')':
                return False
