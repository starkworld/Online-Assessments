"""Calculate the number of all'aaa' substrings"""


def substr(string, sub):
    result = [i for i in range(len(string)) if string.startswith(sub, i)]
    return len(result)


print(substr('aaabbaaanaaa', 'aaa'))



# Nearest fibonacci number to a given number.
# Number of distinct substrings consisting of a single distinct character.
# 1. find out how many square numbers there are in the range [A, B] where A<=B and are both integers. Not that both A and B might be negative.
#
# 2. Given a non-negative integer, return all possible unique combinations by moving the digits around. Note that the
# most significant digit cannot be zero. For example, if input is 112, output is: 112, 121, 211.
#
# 3. lattice points that lie inside (exclusive) a circle of radius R where R is an integer.