import re


def splitnum(num, string):
    regex = re.compile('([a-z]+)([\+|\-])[a-z]+')
    len_a, operation = re.findall(regex, string)[0]
    number_a, number_b = int(num[:len(len_a)]), int(num[len(len_a):])
    return number_a+number_b if operation == '+' else number_a-number_b


print(splitnum('1232', 'ab+cd'))
