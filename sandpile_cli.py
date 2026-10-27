"""Command-line interface for the Abelian sandpile simulation."""

import random

import matplotlib.pyplot as plt
import sandpile
from sandpile_support.view import SandpileView


def main() -> None:
    """Let the user run and view a sandpile simulation.

    >>> callable(main)
    True
    """
    # Asking for a valid grid size.
    while True:
        try:
            rows = int(input("Number of rows: "))
            columns = int(input("Number of columns: "))
            if rows > 0 and columns > 0:
                break
            print("Rows and columns must be positive.")
        except ValueError:
            print("Please enter whole numbers.")

    # The empty pile and the counters.
    pile = sandpile.create_pile(rows, columns)
    grains_added = 0
    grains_lost = 0
    topplings = 0

    # Stores the results of every cycle for the history graphs.
    toppling_history = []
    lost_history = []

    # The supplied viewer draws the sandpile.
    view = SandpileView(rows, columns)
    view.update(pile, grains_added, grains_lost, topplings)