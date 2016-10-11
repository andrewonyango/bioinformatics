def pattern_count(string, pattern):
    """
    returns the number of occurences of *pattern* in *string*

    string: the string to search on
    pattern: the substring to look for in *string*
    """
    count = 0
    text_length = len(string)
    pattern_length = len(pattern)

    # compare only up to the last possible substring...
    for i in range(text_length - pattern_length + 1):
        if string[i: i + pattern_length] == pattern:
            count += 1

    return count
