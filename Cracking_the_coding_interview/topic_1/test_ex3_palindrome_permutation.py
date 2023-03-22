import pytest

from ex3_palindrome_permutation import palindromeString

input_cases = [
    ("carrace", True),
    ("ferel", False),
    ("baaab", True),
    ("caaabbcc", False),
    ("abbacc", True),
    ("abbaccdeee", False),
]

@pytest.mark.parametrize("s,exp",input_cases)
def test_palindromeString(s,exp):
    assert palindromeString(s) is exp