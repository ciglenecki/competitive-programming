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
    if i == 100002:
        break
    primes.append(prime)

set_primes = set(primes)
# print(set_primes)

with open("input_py.txt") as f:
    in_lines = f.read().splitlines()

with open("my_out.txt") as f:
    out_lines = f.read().splitlines()

in_lines = [int(a) for a in in_lines[1:]]
out_lines = [int(a) for a in out_lines]

for a, b in zip(out_lines, in_lines):
    res = int(a) + int(b)
    if a not in set_primes:
        print("A", type(a))
        exit(1)
    if b not in set_primes:
        print(b)
        exit(1)
    if res in set_primes:
        print(a, b, res)
