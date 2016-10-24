from hamming_distance import hamming_distance

def approximate_pattern(pattern, text, distance):
    pattern_length = len(pattern)
    text_length = len(text)
    number_of_windows = text_length - pattern_length + 1
    print(text_length, pattern_length, number_of_windows)
    starting_positions = []

    for i in range(number_of_windows):
        if hamming_distance(pattern, text[i: i + pattern_length]) <= distance:
            starting_positions.append(i)

    return " ".join(str(n) for n in starting_positions)