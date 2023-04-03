DNA_ALPHABET = 'ACGT'
RNA_ALPHABET = 'ACGU'


COMPLEMENT = {
    'A': 'T',
    'C': 'G',
    'G': 'C',
    'T': 'A'
}


def is_DNA(nt):
    return True if nt in DNA_ALPHABET else False


def is_RNA(nt):
    return True if nt in RNA_ALPHABET else False
