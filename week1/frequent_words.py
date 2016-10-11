# a dictionary version of the frequent words problem
def frequent_words(string, n):
    """
    returns a list of the most frequently occuring substrings
    in a string, with overlap allowed

    string: the string to search through
    n: the length of the substrings to look for
    """
    frequent_patterns = dict()
    string_length = len(string)
    n = int(n)

    for i in range(string_length - n + 1):
        pattern = string[i: i + n]

        if pattern in frequent_patterns:
            frequent_patterns[pattern] += 1
        else:
            frequent_patterns.update({pattern: 1})

    return [k for k, v in frequent_patterns.items()
            if v == max(frequent_patterns.values())]
