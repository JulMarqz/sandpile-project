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


def main() -> None:
    """Start the sandpile simulation and process user commands.

    >>> callable(main)
    True
    """
    rows = read_positive_integer("Enter number of rows: ")
    columns = read_positive_integer("Enter number of columns: ")

    pile = create_pile(rows, columns)

    grains_added = 0
    grains_lost = 0
    topplings = 0

    toppling_history = []
    loss_history = []

    view = SandpileView(rows, columns)
    view.update(pile, grains_added, grains_lost, topplings)

    show_help()

    while True:
        command = input("Enter command: ").strip().lower()
        parts = command.split()

        if command == "quit":
            view.close()
            break

        elif command == "help":
            show_help()

        elif command == "reset":
            pile = create_pile(rows, columns)

            grains_added = 0
            grains_lost = 0
            topplings = 0

            toppling_history = []
            loss_history = []

            view.update(pile, grains_added, grains_lost, topplings)

        elif command == "history":
            show_history(toppling_history, loss_history)

        elif len(parts) > 0 and parts[0] == "run":

            if len(parts) != 2:
                print("Please use: run N")
                continue

            try:
                cycles = int(parts[1])
            except ValueError:
                print("N must be a positive integer.")
                continue

            if cycles <= 0:
                print("N must be a positive integer.")
                continue

            for i in range(cycles):
                row = random.randrange(rows)
                column = random.randrange(columns)

                add_grain(pile, row, column)
                grains_added += 1

                cycle_topplings, cycle_losses = relax(pile)

                topplings += cycle_topplings
                grains_lost += cycle_losses

                toppling_history.append(cycle_topplings)
                loss_history.append(cycle_losses)

            view.update(pile, grains_added, grains_lost, topplings)

        else:
            print("Unknown command. Type 'help' for available commands.")


if __name__ == "__main__":
    main()