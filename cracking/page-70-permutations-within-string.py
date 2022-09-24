# optimal O(b)

s = "abbc"
b = "cbabadcbbabbcbabaabccbabc"


store = {}

# create store based on b because there might be a letter in b which is not contained in a

# O(b)
for letter in b:
    if letter not in store:
        store[letter] = 0

# O(b) fill the store
for letter in s:
    if letter not in store:
        raise Exception(
            "can't find the the permutation because there isn't such a letter in b"
        )
    store[letter] += 1

left_idx = 0
# O(b)
matching_letter_count = 0  # how many keys in the store are currently at zero?
for right_idx, right_letter in enumerate(b):
    left_letter = b[left_idx]

    if (right_idx - left_idx) >= len(s):
        left_idx += 1
        if store[left_letter] == 0:
            matching_letter_count -= (
                1  # we are losing one matched letter because it was previously at zero
            )
        store[left_letter] += 1

    store[right_letter] -= 1

    if store[right_letter] == 0:
        matching_letter_count += 1

    if matching_letter_count == len(store) - 1:
        print(b[left_idx : right_idx + 1])
    # if all(
    #     map(lambda x: x == 0, store.values())
    # ):  # constant ? because of amount of letters ?
    #     print(b[left_idx : right_idx + 1])
