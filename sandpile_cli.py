
"""
Command-line interface for the Abelian sandpile simulation.
"""

import random
import matplotlib.pyplot as plt
from sandpile_support.view import SandpileView
import sandpile


def main() -> None:
    """Run the sandpile simulation and respond to user commands.

    >>> callable(main)
    True
    """
    # Ask for a valid grid size
    while True:
        try:
            rows = int(input("Number of rows: "))
            columns = int(input("Number of columns: "))

            if rows > 0 and columns > 0:
                break

            print("Rows and columns must be positive.")

        except ValueError:
            print("Please enter whole numbers.")

        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            return

    # Create the empty pile and counters
    pile = sandpile.create_pile(rows, columns)

    grains_added = 0
    grains_lost = 0
    topplings = 0

    # Lists for storing history
    toppling_history = []
    lost_history = []

    # The visualization
    view = SandpileView(rows, columns)
    view.update(pile, grains_added, grains_lost, topplings)

    print("Commands: run N, history, reset, help, quit")

    # Main command loop
    try:
        while True:
            user_input = input("Command: ").strip().lower()
            parts = user_input.split()

            if len(parts) == 0:
                continue

            command = parts[0]

            # QUIT
            if command == "quit" and len(parts) == 1:
                print("Goodbye!")
                break

            # HELP
            elif command == "help" and len(parts) == 1:
                print("run N   - Run N random cycles")
                print("history - Show history graphs")
                print("reset   - Reset the simulation")
                print("help    - Show commands")
                print("quit    - Exit the program")

            # RESET
            elif command == "reset" and len(parts) == 1:
                pile = sandpile.create_pile(rows, columns)

                grains_added = 0
                grains_lost = 0
                topplings = 0

                toppling_history.clear()
                lost_history.clear()

                view.update(
                    pile, grains_added, grains_lost, topplings
                )

                print("Simulation reset.")

            # RUN
            elif command == "run":

                # Check that N was provided
                if len(parts) != 2:
                    print("Use: run N (example: run 100)")
                    continue

                try:
                    n = int(parts[1])
                except ValueError:
                    print("N must be a positive whole number.")
                    continue

                if n <= 0:
                    print("N must be a positive whole number.")
                    continue

                # Run N simulation cycles
                for i in range(n):

                    # Choose a random cell
                    row = random.randrange(rows)
                    column = random.randrange(columns)

                    # Add one grain
                    sandpile.add_grain(pile, row, column)
                    grains_added = grains_added + 1

                    # Relax the pile
                    cycle_topplings, cycle_lost = sandpile.relax(pile)

                    # Update the counters
                    topplings = topplings + cycle_topplings
                    grains_lost = grains_lost + cycle_lost

                    # Save the results for this cycle
                    toppling_history.append(cycle_topplings)
                    lost_history.append(cycle_lost)

                # Update the visualization after all cycles
                view.update(
                    pile, grains_added, grains_lost, topplings
                )

                print("Finished running cycles.")

            # HISTORY
            elif command == "history" and len(parts) == 1:

                if len(toppling_history) == 0:
                    print("No history yet. Try: run 100")
                    continue

                # Cycle numbers start at 1
                cycles = range(1, len(toppling_history) + 1)

                # Draw the history graph.
                plt.figure("Sandpile History")
                plt.clf()

                plt.plot(
                    cycles, toppling_history, label="Topplings"
                )
                plt.plot(
                    cycles, lost_history, label="Grains lost"
                )

                plt.xlabel("Cycle number")
                plt.ylabel("Count per cycle")
                plt.title("Sandpile History")
                plt.legend()

                # Show the graph and keep the terminal usable
                plt.show(block=False)
                plt.pause(0.1)

            # INVALID COMMAND
            else:
                print("Unknown command. Type 'help'.")

    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")

    finally:
        # Close all visualization windows
        view.close()
        plt.close("all")


if __name__ == "__main__":
    main()
