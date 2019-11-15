def to_rna(dna_strand):
    arnstrand = {'G':'C', 'C':'G', 'T':'A', 'A':'U'}
    return ''.join(arnstrand[nucleotid] for nucleotid in dna_strand)