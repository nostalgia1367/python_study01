

try:
    file = open('subtitle.srt', 'r')
    print(file)
except FileNotFoundError:
    print('error occurred!')


try:
    number = float('hello')
    print(number)
except ValueError as e:
    raise BizException(e)


