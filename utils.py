from constants import DNA_ALPHABET, RNA_ALPHABET

def is_DNA(dna):
    return all([nt in DNA_ALPHABET for nt in dna])


def is_RNA(rna):
    return all([nt in RNA_ALPHABET for nt in rna])

