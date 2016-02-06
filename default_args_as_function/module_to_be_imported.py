"""
Used by primary_module to supply default parameter value for myfunction

Generates a random number for the default value in the range of 0 to
32768.
"""

import random


def function_to_supply_default_value():
    """
    Generate a random integer w/ the generator seed set to current time
    """

    random.seed()
    return int(random.random() * 32768)
