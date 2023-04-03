import os

class _StringIsNotDNA(Exception):
    def __init__(self, message=None):
        if message is None:
            message = 'Error: your string is not a DNA string!'
        super().__init__(message)

class _StringIsOutOfRange(Exception):
    def __init__(self, string, message=None):
        if message is None:
            message = 'Error: len(' + [name for name in globals() \
                                   if globals()[name] == string][0] \
                + ') = ' + str(len(string)) + ' must be at most 1000!'
        super().__init__(message)

_DNA_ALPHABET = 'ACGT'

def _is_DNA(nt):
    return True if nt in _DNA_ALPHABET else False

def dna(s, path=None, save=False):
    # assert all(list(map(_is_DNA, s))), f'Error: your string is not a DNA string'
    # assert len(s) <= 1e3, f'Error: len(s) = {len(s)} must be at most 1000!'

    if not all(list(map(_is_DNA, s))):
        raise _StringIsNotDNA()
    if len(s) > 1e3:
        raise _StringIsOutOfRange(s)

    result = [s.count(nt) for nt in _DNA_ALPHABET]

    if save:
        if path is None:
            path = os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                                'rosalind_dna_1_output.txt')
        else:
            path = os.path.join(os.getcwd(), 'rosalind_dna_1_output.txt')
        with open(path,  'w') as file:
            file.write(' '.join([str(x) for x in result]))

    return result

if __name__ == '__main__':
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                           'rosalind_dna_1_dataset.txt'), 'r') as file:
        s = file.readline()[:-1]

    print(s)

    print(*dna(s, save=True))
