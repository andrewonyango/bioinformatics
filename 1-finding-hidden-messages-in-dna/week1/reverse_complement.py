def reverse_complement(string):
    """
    returns the reverse complement of a dna string

    string: the original dna string
    """
    dna_dict = {"A": "T", "G": "C", "T": "A", "C": "G"}
    complement = []

    for char in string:
        complement.append(dna_dict[char])

    return "".join(complement[::-1])
