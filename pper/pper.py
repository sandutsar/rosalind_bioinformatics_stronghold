import os, sys
from math import factorial


def pper(n, k, save=False, path=None, filename='rosalind_pper_1_output', ext='txt'):
    assert n > 0, f'Error: n = {n} must be > 0!'
    assert n <= 100, f'Error: n = {n} must be <= 100!'

    assert k > 0, f'Error: k = {k} must be > 0!'
    assert k <= 10, f'Error: k = {k} must be <= 10!'

    result = int(factorial(n) / factorial(n - k) % int(1e6))
    
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
    if len(sys.argv) == 3:
        n = int(sys.argv[1])
        k = int(sys.argv[2])
    else:
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                            'rosalind_pper_1_dataset.txt'), 'r') as file:
            n, k = list(map(int, file.readline().split()))

    print(n, k)

    print(pper(n, k, save=True))
