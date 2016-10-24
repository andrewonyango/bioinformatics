def hamming_distance(p, q):
    """
    returns the number of mismatches between 2 equal-length strings, p and q
    """
    return len([i for i in range(len(p)) if p[i] != q[i]])