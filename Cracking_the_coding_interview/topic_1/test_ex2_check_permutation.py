import pytest

from ex2_check_permutation import Solution

test_input = [
    ("anagram", "nagaram", True),
    ("rat", "car", False),
    ("abc", "bac", True),
    ("aac", "ac", False),
    ("aab", "abb", False),
]

@pytest.mark.parametrize("s,t,expected", test_input)
def test_isAnagram(s,t,expected):
    assert Solution().isAnagram(s,t) is expected