from test import Case, test_me

"""
String Rotation:Assumeyou have a method isSubstring which checks if one word is a substring
of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one
call to isSubstring (e.g.,"waterbottle" is a rotation of"erbottlewat").

Solution: check if rotated string is contained within the {original}{original}
"""


def is_substring(smaller: str, bigger: str):
	return smaller in bigger

def solution(original: str, rotated: str):
	if len(original) != len(rotated):
		return False
	if len(original) == 0:
		return False
	
	doubled_original = "".join([original,original])
	return is_substring(rotated, doubled_original)




test_cases: list[Case] = [
    {
        "i": ("original", "ginalori"),
        "o": True,
		
    },
	{
		"i": ("o", "o"),
        "o": True,
	},
	{
		"i": ("ob", "bo"),
        "o": True,
	},
	{
		"i": ("oobo", "oobo"),
        "o": True,
	},
	{
		"i": ("abcd", "dabc"),
        "o": True,
	},
	{
		"i": ("", ""),
        "o": False,
	},
]

test_functions = [
    solution
]

if __name__ == "__main__":
    test_me(test_cases, test_functions)
