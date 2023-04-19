import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                             os.pardir))
from constants import MONOISOTOPIC_MASS_TABLE#, RNA_CODON_TABLE
from exceptions import IterableLengthError, StringIsNotProteinError
from utils import is_protein


def prtm(p, save=False, path=None, filename='rosalind_prtm_1_output', ext='txt'):
    # assert isinstance(p, str), f'Error: type(p) = {type(p).__name__} must be str!'
    # assert is_protein(p), f'Error: Your string is not a valid protein string! \
    #     It must be composed using {set(RNA_CODON_TABLE.values())} alphabet!'
    # assert len(p) <= 1e3, f'Error: len(p) = {len(p)} must be <= 1000!'

    if not isinstance(p, str):
        raise TypeError(f'Error: type(p) = {type(p).__name__} must be str!')
    if not is_protein(p):
        raise StringIsNotProteinError()
    if len(p) > 1e3:
        raise IterableLengthError(iterable=p, sign='<=', value=int(1e3))
    
    result = round(sum([MONOISOTOPIC_MASS_TABLE[aa] for aa in p]), 3)
    
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
        p = sys.argv[1]
    else:
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                            'rosalind_prtm_1_dataset.txt'), 'r') as file:
            p = file.readline()[:-1]

    print(p)

    print(prtm(p, save=True))
