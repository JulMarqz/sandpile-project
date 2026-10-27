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
    # asking for a valid grid size
    while True:
        try:
            rows = int(input("Number of rows: "))
            columns = int(input("Number of columns: "))
            if rows > 0 and columns > 0:
                break
            print("Rows and columns must be positive.")
        except ValueError:
            print("Please enter whole numbers.")

    # the empty pile and the counters
    pile = sandpile.create_pile(rows, columns)
    grains_added = 0
    grains_lost = 0
    topplings = 0

    # stores the results of every cycle for the history graphs
    toppling_history = []
    lost_history = []

    # the supplied viewer draws the sandpile
    view = SandpileView(rows, columns)
    view.update(pile, grains_added, grains_lost, topplings)
    print("Commands: run N, history, reset, help, quit")

    # main command loop
    try:
        while True:
            command = input("Command: ").strip().lower()
            parts = command.split()

                # CLI  controls the sandpile simulation
            if parts and parts[0] == "run":
                
                # checks that the user provided exactly one number and that it is a positive integer
                if len(parts) != 2:
                    print("Use: run N (for example, run 100)")
                    continue
                try:
                    n = int(parts[1])
                except ValueError:
                    print("N must be a positive whole number.")
                    continue
                if n <= 0:
                    print("N must be a positive whole number.")
                    continue

        # the actual simulation loop
