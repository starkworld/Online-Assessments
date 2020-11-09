def findBefore(x, y, after):
    """Takes positions of x and y and after matrix
    and returns before matrix element at that position"""
    s = 0
    for i in range(x + 1):
        for j in range(y + 1):
            if i != x or j != y:
                s = s + after[i][j]
    after[x][y] = after[x][y] - s
    return after[x][y]


def findBeforeMatrix(after):
    """This method finds the before matrix element of each element in after matrix
    and returns the before metrix"""

    for i in range(len(after)):
        for j in range(len(after[0])):
            """Calls findBefore function to get before matrix element"""
            after[i][j] = findBefore(i, j, after)
    return after


"""Main method"""


def main():
    """TEST CASE 1"""

    after = [[2, 5], [7, 17]]
    print(findBeforeMatrix(after))

    """TEST CASE 2"""
    after = [[1, 2], [3, 4]]
    print(findBeforeMatrix(after))

    print()
    """TEST CASE 1"""
    after = [[2, 1], [5, 4]]
    print(findBeforeMatrix(after))


main()


def findBeforeMatrices(after):  # function
    row = len(after)  # find number of rows
    col = len(after[0])  # find number of columns in each row
    before = after  # initialize before as after
    for i in range(row):  # iterate over the rows and columns of after matrix
        for j in range(col):
            s = after[i][j]  # initialize s as after[i][j]
            for k in range(0, i + 1):  # iterate over the after matrix for rows in range 0 to i(inclusive)
                # and columns in range 0 to j(inclusive)
                for l in range(0, j + 1):
                    if k == i and l == j:  # if k value matches i value and j value matches l, then
                        # the value need not be subtracted from s (as we see in the formulas)
                        pass
                    else:  # otherwise subtract the value from s
                        s = s - after[k][l]
            before[i][j] = s  # assign the value remaining in s to before matrix
    return before  # return the before matrix


print(findBeforeMatrix([[2, 5], [7, 17]]))
