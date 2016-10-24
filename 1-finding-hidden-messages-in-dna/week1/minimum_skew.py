def minimum_skew(genome):
    """
    returns the indices where the skew attains the minimum

    genome: the string to search for the minimum in
    """
    values = [0]
    x = 0

    for i in range(len(genome)):
        # if the nucleotide is cytosine, the next value in the sequence is
        # decreased by one. if guanine, it's increased by 1. otherwise, it's
        # left unchanged
        if genome[i] == "C":
            x -= 1
        elif genome[i] == "G":
            x += 1
        
        values.append(x)

    minimum = min(values)

    return " ".join([str(k) for k, v in enumerate(values) if v == minimum])
