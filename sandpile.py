Pile = list[list[int]]

def create_pile(rows: int, columns: int) -> Pile:
    """Returns a rectangular grid with n x m rows and columns. Every cell must initially
       contain zero. The CLI must reject non-positive dimensions before calling this function."""    
    pass


def add_grain(pile: Pile, row: int, column: int) -> None:
    """Add exactly one grain to the selected cell. The function changes the supplied pile and returns None. The
    CLI is responsible for checking that the row and column are inside the grid."""
    pass


def topple(pile: Pile, row: int, column: int) -> int:
    """Topple one unstable cell once. The function may assume that the selected cell has height at least four.
    It changes the pile and returns the number of grains lost through the boundary during this toppling."""
    pass


def relax(pile: Pile) -> tuple[int, int]:
    pass
    """ Repeatedly find and topple unstable cells until the pile is stable. Return: (number_of_topplings, number_of_lost_grains)"""

def is_stable(pile: Pile) -> bool:
    """is_stable(pile) -> bool
    Return True precisely when every cell has height at most three, and False otherwise"""
    pass
