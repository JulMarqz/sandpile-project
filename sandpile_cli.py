
import sandpile


def print_pile(pile):
    """Print the sandpile in a readable format."""
    for row in pile:
        for grain in row:
            print(grain, end=" ")
        print()


def main():
    """Run the sandpile command-line interface."""

    print("Welcome to the Sandpile Simulator!")

    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns: "))

    pile = sandpile.create_pile(rows, columns)

    print("\nSandpile created!")
    print_pile(pile)

    while True:
        print("\nChoose an option:")
        print("1. Show sandpile")
        print("2. Add a grain")
        print("3. Topple a cell")
        print("4. Relax sandpile")
        print("5. Check if stable")
        print("6. Quit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            print_pile(pile)

        elif choice == "2":
            row = int(input("Enter row: "))
            column = int(input("Enter column: "))

            if 0 <= row < rows and 0 <= column < columns:
                sandpile.add_grain(pile, row, column)
                print("Grain added!")
                print_pile(pile)
            else:
                print("Invalid row or column.")

        elif choice == "3":
            row = int(input("Enter row: "))
            column = int(input("Enter column: "))

            if not (0 <= row < rows and 0 <= column < columns):
                print("Invalid row or column.")
            elif pile[row][column] < 4:
                print("This cell is not unstable.")
            else:
                lost = sandpile.topple(pile, row, column)
                print("Grains lost:", lost)
                print_pile(pile)

        elif choice == "4":
            topplings, lost = sandpile.relax(pile)
            print("Number of topplings:", topplings)
            print("Grains lost:", lost)
            print_pile(pile)

        elif choice == "5":
            if sandpile.is_stable(pile):
                print("The sandpile is stable.")
            else:
                print("The sandpile is unstable.")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please choose 1-6.")


if __name__ == "__main__":
    main()
