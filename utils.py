from constants import DNA_ALPHABET, RNA_ALPHABET

def is_DNA(s):
    return all([nt in DNA_ALPHABET for nt in s])


def is_RNA(s):
    return all([nt in RNA_ALPHABET for nt in s])


def complement_table(s):
    if is_DNA(s):
        return {key:value for key, value in \
                zip(DNA_ALPHABET, DNA_ALPHABET[::-1])}
    elif is_RNA(s):
        {key:value for key, value in \
                zip(RNA_ALPHABET, RNA_ALPHABET[::-1])}
    else:
        raise TypeError(f'Error: Your string must be either DNA or RNA!') 
