"""Command-line interface for the sandpile project."""

import random
import matplotlib.pyplot as plt

from sandpile import create_pile, add_grain, relax
from sandpile_support.view import SandpileView


def read_positive_integer(prompt: str) -> int:
    """Repeatedly ask the user for a positive integer until valid input is entered.

    >>> read_positive_integer("Enter rows: ")  # doctest: +SKIP
    5
    """
    while True:
        user_input = input(prompt)

        try:
            number = int(user_input)
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if number <= 0:
            print("Please enter a positive integer.")
            continue

        return number

