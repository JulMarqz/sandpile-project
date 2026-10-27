Pile = list[list[int]]

def create_pile(rows: int, columns: int) -> Pile:
    """ Returns a rectangular grid with n x m rows and columns. The cells contain only zeros. 
    
    >>> create_pile(2,2)
    [[0, 0], [0, 0]]
    """ 
    pile = []
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(0)
        pile.append(row)
    return pile

def add_grain(pile: Pile, row: int, column: int) -> None:
    """ Adds exactly one grain to the selected cell. 
    The pile is changed in place and nothing is returned 
        
    >>> pile = [[0, 0], [0, 0]]
    >>> add_grain(pile, 0, 0)
    >>> pile
    [[1, 0], [0, 0]]
    """
    pile[row][column] += 1


def topple(pile: Pile, row: int, column: int) -> int:
    """Topple one unstable cell once. The function may assume that the selected cell has height at least four.
    It changes the pile and returns the number of grains lost through the boundary during this toppling."""
    


def relax(pile: Pile) -> tuple[int, int]:
    pass
    """ Repeatedly find and topple unstable cells until the pile is stable. Return: (number_of_topplings, number_of_lost_grains)"""

def is_stable(pile: Pile) -> bool:
    """is_stable(pile) -> bool
    Return True precisely when every cell has height at most three, and False otherwise"""
    pass
