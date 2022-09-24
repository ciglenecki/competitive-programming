s = "abbc"
b = "cbabadcbbabbcbabaabccbabc"


s_store = {}

# create store based on b because there might be a letter in b which is not contained in a
for letter in b:
    if letter not in s_store:
        s_store[letter] = 0

# fill the store
for letter in s:
    if letter not in s_store:
        raise Exception(
            "can't find the the permutation because there isn't such a letter in b"
        )
    s_store[letter] += 1

left_idx = 0
# todo: check for s = b - 1
for right_idx, letter_right in enumerate(b):
    letter_left = b[left_idx]

    if (right_idx - left_idx) >= len(s):
        left_idx += 1
        s_store[letter_left] += 1

    s_store[letter_right] -= 1
    if all(map(lambda x: x == 0, s_store.values())):
        print(b[left_idx : right_idx + 1])
