# From Leetcode: 266. Palindrome Permutation

def palindromeString(s):
    # If the len is even, there can be no odd frequencies
    # If the len is odd, there can be max 1

    max = 0
    if (len(s) % 2 == 1):
        max = 1

    from collections import Counter
    odds = 0
    counter = Counter(s)
    for key in counter.keys():
        if (counter[key] % 2 == 1):
            odds += 1
        if odds > max:
            return False    
    return True