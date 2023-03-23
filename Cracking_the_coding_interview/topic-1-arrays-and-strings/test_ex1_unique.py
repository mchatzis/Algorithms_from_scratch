import pytest

from ex1_is_unique import Solution

test_cases = [  
                ([],False),
                ([1,2,3,1],True),
                ([1,2,3,4],False),
                ([1,1,1,3,3,4,3,2,4,2],True),
            ]

# Using pytest, parameterized testing, for test_cases
@pytest.mark.parametrize("test_input,expected", test_cases)
def test_containsDuplicate(test_input, expected):
    assert Solution().containsDuplicate(test_input) == expected
