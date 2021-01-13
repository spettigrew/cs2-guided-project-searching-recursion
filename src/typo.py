"""
You are a new author that is working on your first book. You are working on a
series of drafts. Each draft is based on the previous draft. The latest draft
of your book has a serious typo. Since each newer draft is based on the
previous draft, all the drafts after the draft containing the typo also include
the typo.

Suppose you have `n` drafts `[1, 2, 3, ..., n]` and you need to find out the
first one containing the typo (which causes all the following drafts to have
the typo as well).

You are given access to an API tool `containsTypo(draft)` that will return
`True` if the draft contains a typo and `False` if it does not.

You need to implement a function that will find the *first draft that contains
a typo*. Also, you have to pay a fee for every call to `containsTypo()`, so
make sure that your solution minimizes the number of API calls.

Example:

Given `n = 5`, and `draft = 4` is the first draft containing a typo.

containsTypo(3) -> False
containsTypo(5) -> True
containsTypo(4) -> True
"""

n = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def firstDraftWithTypo(n):
    # Your code here
    pass
    contains_typo = 4
    min = 0
    max = len(n) - 1
    while not max < min:
        guess = (min + max) // 2
        # if containsTypo were real this line would be:
        # if containsTypo(n[guess]) and not containsTypo(n[guess -1]):
        if n[guess] == contains_typo and n[guess - 1] != contains_typo:
            # resulting in the first occurrence where the typo exists
            return n[guess]
        # if containsTypo were real this line would be:
        # if not containsTypo(n[guess]):
        elif n[guess] < contains_typo:
            min = guess + 1
        else:
            max = guess - 1
    return -1
# print(firstDraftWithTypo(n))

