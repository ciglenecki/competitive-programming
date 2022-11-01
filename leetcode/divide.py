"""
we shifted the number n once and thereby multiplying it by 2 each time

whenever we check for m & 1 we are effectively know that the this bit is responsible for contributing 4 * n to the total result

instead of doing 2**pow we have the current value that we need to add inside of n

=====================================
0b1111
   _
   421
...
0b11
=====================================
This is also possible, but we can avoid pow by shifting (multiplying by two):

pow = 0
while m != 0:
	
	if (m & 1):
		result += (n * 2 ** pow)

	m = m >> 1
	pow += 1
=====================================
"""

n = 13
m = 15
result = 0
while m != 0:
	
	if (m & 1):
		result += n

	m = m >> 1
	n = n << 1
print(result)