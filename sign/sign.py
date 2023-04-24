import os, sys
from math import factorial
from random import choice


def sign(n, save=False, path=None, filename='rosalind_sign_1_output', ext='txt'):
    assert n > 0, f'Error: n = {n} must be > 0!'
    assert n <= 6, f'Error: n = {n} must be <= 6!'
    
    signed_permutations = 2**n*factorial(n)
    result = []
    while len(result) != signed_permutations:
        nums = [x for x in [x for x in range(-n, n+1)]]
        nums.remove(0)
        temp = []
        for _ in range(n):
            el = choice(nums)
            nums.remove(el)
            nums.remove(-el)
            temp += [el]
        if temp not in result:
            result += [temp]
    
    if save:
        if path is None:
            path = os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                                f'{filename}.{ext}')
        elif os.path.isdir(path):
            path = os.path.join(path, f'{filename}.{ext}')
        with open(path,  'w') as file:
            file.write(str(signed_permutations) + '\n')
            file.writelines([' '.join([str(x) for x in line]) + '\n' for line in result])

    return signed_permutations, result


if __name__ == '__main__':
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    else:
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                            'rosalind_sign_1_dataset.txt'), 'r') as file:
            n = int(file.readline()[:-1])

    print(n)

    print(*sign(n, save=True))
