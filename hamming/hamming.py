def distance(strand_a, strand_b):
    differences = 0
    if len(strand_a) == len(strand_b):
        strand_a = list(strand_a)
        strand_b = list(strand_b)
        for i in range(len(strand_a)):
            if strand_a[i] != strand_b[i]:
                differences = differences + 1
    else:
        raise ValueError(".+")
    return differences

#nice solution from community. No need to else and no need to split
# the method stops after raise the exception and
# A string object is already an array of chars    
def distance2(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('The strand lenghts must be the same')
    return sum((a != b) for a, b in zip(strand_a, strand_b))

