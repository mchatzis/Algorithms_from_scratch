from Ex1_Is_unique import is_unique

def test_is_unique():
    assert is_unique

"""
aba -> fails
a -> succeeds
abc -> succeeds
aa -> fails
"" -> fails
other_type -> fails
"""