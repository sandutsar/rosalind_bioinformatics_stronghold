import os, sys
from math import prod
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                             os.pardir))
from constants import RNA_CODON_TABLE
from exceptions import IterableLengthError, StringIsNotProteinError
from utils import is_protein


def mrna(s, save=False, path=None, filename='rosalind_mrna_1_output', ext='txt'):
    # assert isinstance(s, str), f'Error: type(s) = {type(s).__name__} must be str!'
    # assert is_protein(s), f'Error: Your string is not a valid protein string! \
    #     It must be composed using {set(RNA_CODON_TABLE.values())} alphabet!'
    # assert len(s) <= 1e3, f'Error: len(s) = {len(s)} must be <= 1000!'

    if not isinstance(s, str):
        raise TypeError(f'Error: type(s) = {type(s).__name__} must be str!')
    if not is_protein(s):
        raise StringIsNotProteinError()
    if len(s) > 1e3:
        raise IterableLengthError(iterable=s, sign='<=', value=int(1e3))
    
    result = prod([list(RNA_CODON_TABLE.values()).count(x) for x in s] \
        + [list(RNA_CODON_TABLE.values()).count('*')]) % int(1e6)
    
    if save:
        if path is None:
            path = os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                                f'{filename}.{ext}')
        elif os.path.isdir(path):
            path = os.path.join(path, f'{filename}.{ext}')
        with open(path,  'w') as file:
            file.write(str(result))

    return result


if __name__ == '__main__':
    if len(sys.argv) == 2:
        s = sys.argv[1]
    else:
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                            'rosalind_mrna_1_dataset.txt'), 'r') as file:
            s = file.readline()[:-1]

    print(s)

    print(mrna(s, save=True))
