import time
from test import test_me

# Given a string, write a function to check if it is a permutation of a palin­ drome
# A palindrome is a word or phrase that is the same forwards and backwards
# A permutation is a rearrangement of letters
# The palindrome does not need to be limited to just dictionary words.


def char_to_lower(char: str) -> str:
	ordinal_number = ord(char)

	if ordinal_number >= ord('A') and ordinal_number <= ord('Z'):
		return chr(ordinal_number + ord('a') - ord('A'))
	elif ordinal_number >= ord('a') and ordinal_number <= ord('z'):
		return char
	else:
		return char

def is_lower_alphabetic_char(char: str) -> str:
	ordinal_number = ord(char)
	return ordinal_number >= ord('a') and ordinal_number <= ord('z')


def char_to_table_map(char: str) -> str: 
	lower_char = char_to_lower(char)

	if not is_lower_alphabetic_char(lower_char):
		return -1 

	return ord(lower_char) - ord('a')


def has_palindrome_permutation(string: str):
	char_list = list(string)
	store = {}

	for character in char_list:
		lower_character = character.lower()
		if not is_lower_alphabetic_char(lower_character):
			continue
		if lower_character not in store:
			store[lower_character] = 0
		store[lower_character] += 1
	
	contains_odd = False
	for value in store.values():
		if value % 2 == 1:
			if contains_odd:
				return False
			contains_odd = True
	return True



def has_palindrome_permutation_better(string: str):
	char_list = list(string)

	table = [0 for _ in range(ord('z') - ord('a') + 1)]
	odd_count = 0

	for character in char_list:
		char_table_idx = char_to_table_map(character)

		if char_table_idx == -1:
			continue

		table[char_table_idx] += 1

		if table[char_table_idx] % 2 == 1:
			odd_count += 1
		else:
			odd_count -= 1
	return odd_count <= 1


def has_palindrome_permutation_bit(string: str):
	bit_map = 0 # each bit represents lower-case letter from the English alphabet
	for c in string:
		i = char_to_table_map(c)
		if i != -1:
			mask = 1 << i # set the i-th position
			bit_map = bit_map ^ mask # flip the bit
	return (bit_map & (bit_map - 1)) == 0

test_cases = (
    ("Tact Coa", True),
	("aba", True),
	("aab", True),
	("abba", True),
	("aabb", True),
	("a-bba", True),
	("a-bba!", True),
	("Tact Coa", True),
	("jhsabckuj ahjsbckj", True),
	("Able was I ere I saw Elba", True),
	("So patient a nurse to nurse a patient so", False),
	("Random Words", False),
	("Not a Palindrome", False),
	("no x in nixon", True),
	("azAZ", True),
)

test_functions = [
    has_palindrome_permutation,
	has_palindrome_permutation_better,
	has_palindrome_permutation_bit,
]

if __name__ == "__main__":
    test_me(test_cases, test_functions)
