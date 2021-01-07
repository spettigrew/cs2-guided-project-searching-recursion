"""
I was bored one day and decided to look at last names in the phonebook for my
area.

I flipped open the phonebook to a random page near the middle and started
perusing. I wrote each last name that I was unfamiliar with down on paper in
increasing order. When I got to the end of the phonebook, I was having so much
fun I decided to start from the beginning and keep going until I reached the
page where I had started.

When I was finished, I had a list of interesting last names that were mostly
alphabetical. The problem was that my list starts somehere near the middle of
the alphabet, reaches the end, and then starts from the beginning of the
alphabet. In other words, my list of names is sorted, but it is "rotated."

Example:

surnames = [
    'liu',
    'mcdowell',
    'nixon',
    'sparks',
    'zhang',
    'ahmed',  # <-- rotates here!
    'brandt',
    'davenport',
    'farley',
    'glover',
    'kennedy',
]
(Find the first letter that is lower that the first letter in the first name.)

Write a function that finds the index of the "rotation point". The "rotation
point" is where I started working from the beginning of the phone book. The
list I came up was absolutely huge, so make sure your solution is efficient.

*Note: you should be able to come up with a solution that has O(log n) time
complexity.*
"""
def find_rotation_point(surnames):
    # Your code here
    # get the first name and use it compare against all the other guesses
    first_surname = surnames[0]
    # create our search space
    top_index = 0     # top = top  of list
    bottom_index = len(surnames) - 1   # bottom = bottom of list

    # while top_index < bottom_index:
    while top_index < bottom_index:
        # make guesses, (specifically in the middle of our space)
        # guess_index = top_index + ((bottom_index - top_index) // 2)
        guess_index = (bottom_index + top_index) // 2
        # check if the guess is lower or greater that the first_surname
        # if guess is greater that the first_surname, 
        if surnames[guess_index] >= first_surname:
            # move the top, to the new guess location
            top_index = guess_index
        # otherwise, if the guess is lower, move the bottom up
        else:
            bottom_index = guess_index
        # if only two items left, return the lower item 
        if top_index + 1 == bottom_index:
            # the lower item, should be the floor
            return bottom_index
    


surnames = [
    'liu',
    'mcdowell',
    'nixon',
    'sparks',
    'zhang',
    'ahmed',  # <-- rotates here!
    'brandt',
    'davenport',
    'farley',
    'glover',
    'kennedy',
]

print(find_rotation_point(surnames))