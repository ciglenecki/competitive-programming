# Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/
from itertools import combinations
from tqdm import tqdm


def gen_primes():
    """Generate an infinite sequence of prime numbers."""
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}

    # The running integer that's checked for primeness
    q = 2

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1


primes = []
for i, prime in enumerate(gen_primes()):
    if i == 100000:
        break
    primes.append(prime)
set_primes = set(primes)

with open("input_py.txt", "w") as input_file, open("output_py.txt", "w") as output_file:
    # input_file.write(f"{len(set_primes)}\n")
    for a in tqdm(primes):
        for b in primes:
            total = a + b
            if total not in primes and total <= primes[-1]:
                input_file.write(f"{a}\n")
                output_file.write(f"{b}\n")
                break
    input_file.close()
    output_file.close()

print("Done")
