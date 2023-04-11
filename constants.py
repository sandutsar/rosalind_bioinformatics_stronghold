DNA_ALPHABET = 'ACGT'
RNA_ALPHABET = DNA_ALPHABET.replace('T', 'U')


COMPLEMENT = {key:value for key, value in \
              zip(DNA_ALPHABET, DNA_ALPHABET[::-1])}
