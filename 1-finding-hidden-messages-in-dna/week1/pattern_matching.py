def pattern_match(pattern, genome):
    """
    returns the starting positions of each occurence of *pattern* in *genome*

    pattern: the sub-sequence to look for
    genome: the sequence to look in
    """
    positions = []
    genome_length = len(genome)
    pattern_length = len(pattern)

    # compare only up to the last possible sub-sequence...
    for i in range(genome_length - pattern_length + 1):
        if genome[i: i + pattern_length] == pattern:
            positions.append(i)

    return " ".join(str(n) for n in positions)

