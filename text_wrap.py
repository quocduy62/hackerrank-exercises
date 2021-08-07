import textwrap

def wrap(string, max_width):
    last_result = ''
    for e in list(map(str, textwrap.wrap(string,max_width))):
        last_result += e + '\n'
    return last_result


if __name__ == '__main__':
    s, max_w = input(), int(input())
    result = wrap(s, max_w)
    print(result)