import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                             os.pardir))
# from constants import DNA_ALPHABET
from exceptions import IterableLengthError, StringIsNotDNAError
from utils import complement_table, is_DNA


def revc(s, save=False, path=None, filename='rosalind_revc_1_output', ext='txt'):
    # assert isinstance(s, str), f'Error: type(s) = {type(s).__name__} must be str!'
    # assert is_DNA(s), f'Error: Your string is not a valid DNA string! \
    #     It must be composed using {DNA_ALPHABET} alphabet!'
    # assert len(s) <= 1e3, f'Error: len(s) = {len(s)} must be <= 1000!'

    if not isinstance(s, str):
        raise TypeError(f'Error: type(s) = {type(s).__name__} must be str!')
    if not is_DNA(s):
        raise StringIsNotDNAError()
    if len(s) > 1e3:
        raise IterableLengthError(iterable=s, sign='<=', value=int(1e3))
    
    result = [complement_table(s)[nt] for nt in s]
    result.reverse()
    result = ''.join(result)
    
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
                            'rosalind_revc_1_dataset.txt'), 'r') as file:
            s = file.readline()[:-1]

    print(s)

    print(revc(s, save=True))
