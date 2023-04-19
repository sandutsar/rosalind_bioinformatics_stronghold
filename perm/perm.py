import os, sys
from math import factorial
from random import choice


def perm(n, save=False, path=None, filename='rosalind_perm_1_output', ext='txt'):
    assert n > 0, f'Error: n = {n} must be > 0!'
    assert n <= 7, f'Error: n = {n} must be <= 7!'

    permutations = factorial(n)
    result = []
    while len(result) != permutations:
        nums = [x for x in range(1, n+1)]
        temp = []
        for _ in range(n):
            el = choice(nums)
            nums.remove(el)
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
            file.write(str(permutations) + '\n')
            file.writelines([' '.join([str(x) for x in line]) + '\n' for line in result])

    return permutations, result


if __name__ == '__main__':
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    else:
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                            'rosalind_perm_1_dataset.txt'), 'r') as file:
            n = int(file.readline()[:-1])

    print(n)
    
    print(*perm(n, save=True))
