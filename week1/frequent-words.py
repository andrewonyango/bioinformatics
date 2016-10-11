# the (inefficient) course version of the algorithm
from pattern_count import pattern_count


def frequent_words(string, n):
    """
    returns a list of the most frequently occuring substrings
    in a string, with overlap allowed

    string: the string to search through
    n: the length of the substrings to look for
    """
    frequent_patterns = set()
    string_length = len(string)
    n = int(n)

    occurrences = []

    # for each substring, record how many times it appears in the string
    for i in range(string_length - n + 1):
        pattern = string[i: i + n]
        occurrences.append(pattern_count(string, pattern))

    max_count = max(occurrences)

    # now add the most frequently occuring substrings to our set
    for i in range(string_length - n + 1):
        if occurrences[i] == max_count:
            frequent_patterns.add(string[i: i + n])

    return frequent_patterns
