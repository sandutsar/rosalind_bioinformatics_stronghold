from constants import DNA_ALPHABET, RNA_ALPHABET, RNA_CODON_TABLE

def is_DNA(s):
    return all([nt in DNA_ALPHABET for nt in s])


def is_RNA(s):
    return all([nt in RNA_ALPHABET for nt in s])


def is_protein(s):
    return all([aa in set(RNA_CODON_TABLE.values()) for aa in s])


def complement_table(s):
    if is_DNA(s):
        return {key:value for key, value in \
                zip(DNA_ALPHABET, DNA_ALPHABET[::-1])}
    elif is_RNA(s):
        return {key:value for key, value in \
                zip(RNA_ALPHABET, RNA_ALPHABET[::-1])}
    else:
        raise TypeError(f'Error: Your string must be either DNA or RNA!') 
