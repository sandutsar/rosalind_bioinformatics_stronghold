import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                             os.pardir))
from constants import RNA_CODON_TABLE #, RNA_ALPHABET
from exceptions import IterableLengthError, StringIsNotRNAError
from utils import is_RNA


def prot(s, save=False, path=None, filename='rosalind_prot_1_output', ext='txt'):
    # assert isinstance(s, str), f'Error: type(s) = {type(s).__name__} must be str!'
    # assert is_RNA(s), f'Error: Your string is not a valid RNA string! \
    #     It must be composed using {RNA_ALPHABET} alphabet!'
    # assert len(s) <= 1e4, f'Error: len(s) = {len(s)} must be <= 10000!'

    if not isinstance(s, str):
        raise TypeError(f'Error: type(s) = {type(s).__name__} must be str!')
    if not is_RNA(s):
        raise StringIsNotRNAError()
    if len(s) > 1e4:
        raise IterableLengthError(iterable=s, sign='<=', value=int(1e4))
    
    result = ''.join([RNA_CODON_TABLE[codon] for codon in [s[x:x+3] \
                                                   for x in range(0, len(s), 3)]][:-1])

    if save:
        if path is None:
            path = os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                                f'{filename}.{ext}')
        elif os.path.isdir(path):
            path = os.path.join(path, f'{filename}.{ext}')
        with open(path,  'w') as file:
            file.write(result)

    return result


if __name__ == '__main__':
    if len(sys.argv) == 2:
        s = sys.argv[1]
    else:
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                            'rosalind_prot_1_dataset.txt'), 'r') as file:
            s = file.readline()[:-1]

    print(s)

    print(prot(s, save=True))
