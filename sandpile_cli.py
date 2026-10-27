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


def show_help() -> None:
    """Print the available commands.

    >>> show_help()
    Available commands:
    run N - Run N simulation cycles
    history - Show history plots
    reset - Reset the simulation
    help - Show available commands
    quit - Exit the program
    """
    print("Available commands:")
    print("run N - Run N simulation cycles")
    print("history - Show history plots")
    print("reset - Reset the simulation")
    print("help - Show available commands")
    print("quit - Exit the program")


def show_history(toppling_history: list[int],
                 loss_history: list[int]) -> None:
    """Display plots of topplings and grains lost in each cycle.

    >>> show_history([], [])
    No history available yet.
    """
    if len(toppling_history) == 0:
        print("No history available yet.")
        return

    cycles = list(range(1, len(toppling_history) + 1))

    plt.figure()

    plt.plot(cycles, toppling_history, label="Topplings")
    plt.plot(cycles, loss_history, label="Grains lost")

    plt.xlabel("Simulation cycle")
    plt.ylabel("Number")
    plt.title("Sandpile simulation history")
    plt.legend()
    plt.grid(True)

    plt.show(block=False)
    plt.pause(0.1)
