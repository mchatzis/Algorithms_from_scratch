import pytest

from tribonacci import Solution

input_cases = [
    (4, 4),
    (25, 1389537),
    (100, 98079530178586034536500564),
]

@pytest.mark.parametrize("n,exp", input_cases)
def test_tribonacci(n,exp):
    assert Solution().tribonacci(n) == exp