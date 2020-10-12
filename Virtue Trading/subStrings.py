"""Calculate the number of all'aaa' substrings"""


def substr(string, sub):
    result = [i for i in range(len(string)) if string.startswith(sub, i)]
    return len(result)


print(substr('aaabbaaanaaa', 'aaa'))
