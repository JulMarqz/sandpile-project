Pile = list[list[int]]

def create_pile(rows: int, columns: int) -> Pile:
    """ Returns a rectangular grid with n x m rows and columns. The cells contain only zeros. 
    
    >>> create_pile(2,2)
    [[0, 0], [0, 0]]
    """ 
    return [[0 for j in range(columns)] for i in range(rows)]


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
    """Topple one unstable cell once and return the grains lost at the edge.
    The cell is assumed to have height at least four. The pile is changed
    in place. 

    >>> pile = [[4, 1],[2, 2]]
    >>> topple(pile, 0, 0)
    2
    >>> pile
    [[0, 2], [3, 2]]
    """

    lost = 0

    pile[row][column] -= 4

    # if north neighbor exists
    if row > 0:
        pile[row - 1][column] += 1
    else:
        lost += 1                    

    # if south neighbor exists
    if row < len(pile) - 1:       
        pile[row + 1][column] += 1
    else:
        lost += 1      

    # if west neighbor exists
    if column > 0:
        pile[row][column - 1] += 1
    else:
        lost += 1          

    # if east neighbor exists
    if column < len(pile[0]) - 1:    
        pile[row][column + 1] += 1
    else:
        lost += 1               

    return lost


def relax(pile: Pile) -> tuple[int, int]:
    """ Repeatedly find and topple unstable cells until the pile is stable. Returns number of topplings and number of lost grains 
    
    >>> pile = [[1, 2, 3, 4], [1, 2, 3, 4]]
    >>> result = relax(pile)
    >>> result
    (4, 6)
    >>> pile
    [[1, 3, 1, 2], [1, 3, 1, 2]]
    """

    number_of_topplings = 0
    number_of_lost_grains = 0

    len_row = len(pile)
    len_column = len(pile[0])

    i = 0
    j = 0

    while i < len_row:
        if pile[i][j] >= 4:
            number_of_lost_grains += topple(pile, i, j)
            number_of_topplings += 1

            # go back after toppling
            if i > 0:        # if north neighbor exists go north
                i -= 1
            elif j > 0:      # else if west
                j -= 1
            # else stay at (0, 0)

        else:
            j += 1           # go east
            if j == len_column:  # end of row
                j = 0
                i += 1

    return number_of_topplings, number_of_lost_grains


def is_stable(pile: Pile) -> bool:
    """ Returns True precisely when every cell has height at most three, and False otherwise 

    >>> pile = [[2, 1], [1, 3]]
    >>> is_stable(pile)
    True

    >>> pile = [[2, 4], [1, 3]]
    >>> is_stable(pile)
    False
    """
    
    for i in pile:
        for j in i:
            if j > 3:
                return False
        return True
