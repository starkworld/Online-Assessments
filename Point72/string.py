"""Give a string 'abbdcade', find the shortest substring that contains all the letters of the original string,
and only return the length of the substring For a set of strings. """

from collections import defaultdict

MAX_CHARS = 256


# Function to find smallest window
# containing all distinct characters
def findSubString(strr):
    n = len(strr)

    dist_count = len(set([x for x in strr]))
    print(dist_count)

    curr_count = defaultdict(lambda: 0)
    count = 0
    start = 0
    min_len = n

    for j in range(n):
        curr_count[strr[j]] += 1

        if curr_count[strr[j]] == 1:
            count += 1

        if count == dist_count:
            while curr_count[strr[start]] > 1:
                if curr_count[strr[start]] > 1:
                    curr_count[strr[start]] -= 1

                start += 1

            # Update window size
            len_window = j - start + 1

            if min_len > len_window:
                min_len = len_window
                start_index = start

                # Return substring starting from start_index
    # and length min_len """
    return str(strr[start_index: start_index +
                                 min_len])

print(findSubString('abbdcade'))