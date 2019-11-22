"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Score categories.
# Change the values as you see fit.
YACHT = None
ONES = None
TWOS = r"[2]"
THREES = None
FOURS = None
FIVES = None
SIXES = None
FULL_HOUSE = r"(\d){3}(\d){2}"
FOUR_OF_A_KIND = None
LITTLE_STRAIGHT = None
BIG_STRAIGHT = None
CHOICE = None

import re
def score(dice, category):
    dice = str(sorted(dice))
    print(dice, " ", type(dice))
    print(''.join(dice))
    matches = re.findall(category, "22233")
    print(matches)
    

    
score([2, 2, 2, 3, 3], FULL_HOUSE)