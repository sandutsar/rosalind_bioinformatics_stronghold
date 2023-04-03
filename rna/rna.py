import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                             os.pardir))
from constants import is_DNA
from exceptions import IterableLengthError, StringIsNotDNAError


def rna(s, path=None, save=False):
    # assert isinstance(s, str), f'Error: type(s) = {type(s).__name__} must be str!'
    # assert all(list(map(_is_DNA, s))), f'Error: Your string is not a valid DNA string! \
    #     It must be composed using {DNA_ALPHABET} alphabet!'
    # assert len(s) <= 1e3, f'Error: len(s) = {len(s)} must be <= 1000!'

    if not isinstance(s, str):
        raise TypeError(f'Error: type(s) = {type(s).__name__} must be str!')
    if not all(list(map(is_DNA, s))):
        raise StringIsNotDNAError()
    if len(s) > 1e3:
        raise IterableLengthError(iterable=s, sign='<=', value=int(1e3))
    
    result = s.replace('T', 'U')

    if save:
        if path is None:
            path = os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                                'rosalind_rna_1_output.txt')
        elif os.path.isdir(path):
            path = os.path.join(path, 'rosalind_rna_1_output.txt')
        with open(path,  'w') as file:
            file.write(result)

    return result

if __name__ == '__main__':
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                           'rosalind_rna_1_dataset.txt'), 'r') as file:
        t = file.readline()[:-1]

    print(t)

    u = rna(t, save=True)
    print(u)