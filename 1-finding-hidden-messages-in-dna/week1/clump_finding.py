from pattern_count import pattern_count


def clump_finding(genome, k, window, t):
    """
    returns the k-mers forming (window, t)-clumps in genome

    genome: the dna sequence on which we'll apply the algorithm
    k: the length of the k-mers to search for
    window (or L): the length of the dna subsequence to look for the k-mers
    t: the number of times the k-mer appears in the window (or L)
    """
    frequencies = dict()

    # check only until the last possible window (+1 to include last window)
    for i in range(len(genome) - window + 1):
        string = genome[i: i + k]
        interval = genome[i: i + window]
        count = pattern_count(interval, string)

        # if count is less than t, there's no need to add it to our dictionary
        if count < t:
            continue

        frequencies.update({string: count})

    return [k for k, v in frequencies.items()]
