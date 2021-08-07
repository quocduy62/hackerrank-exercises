def char_isalnum(string):
    for c in string:
        if c.isalnum():
            return True
    return False


def char_isalpha(string):
    for c in string:
        if c.isalpha():
            return True
    return False


def char_isdigit(string):
    for c in string:
        if c.isdigit():
            return True
    return False


def char_islower(string):
    for c in string:
        if c.islower():
            return True
    return False


def char_isupper(string):
    for c in string:
        if c.isupper():
            return True
    return False


s = input()
print(char_isalnum(s))
print(char_isalpha(s))
print(char_isdigit(s))
print(char_islower(s))
print(char_isupper(s))