"""Matplotlib display support for the Abelian sandpile assignment.

The model is a rectangular list of lists of non-negative integers, indexed as
``pile[row][column]``. Rows run from top to bottom, columns from left to right.
Stable heights 0, 1, 2 and 3 are shown in different colours.

To use the view from your terminal interface:

1. Import ``SandpileView`` and create ``view = SandpileView(rows, columns)``
   once the positive grid dimensions are known.
2. Create and maintain the pile and the cumulative counts of grains added,
   grains lost, and topplings in your own code. The view does not calculate
   these values or implement the model rules.
3. Call ``view.update(pile, grains_added, grains_lost, topplings)`` to draw
   the current pile and show the supplied counts in the figure title. The pile
   must have the same dimensions as the view.
4. On reset, pass the empty pile and zero counts to ``update``. When finished,
   call ``view.close()``. Optionally, ``view.pause(seconds)`` allows the
   window to remain responsive for a chosen time.

The view does not implement simulation controls or read terminal input. Use
the command-line interface to control the simulation. Matplotlib is required;
installation instructions are in the accompanying README.

Examples:
    >>> validate_pile([[0]], 1, 1)
"""

from __future__ import annotations

import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.colors import BoundaryNorm, ListedColormap
from matplotlib.figure import Figure
from matplotlib.image import AxesImage

Pile = list[list[int]]


def validate_pile(pile: Pile, rows: int, columns: int) -> None:
    """Check that a pile is rectangular and contains non-negative integers.

    Args:
        pile: The two-dimensional height grid to check.
        rows: Required number of rows.
        columns: Required number of columns.

    Raises:
        ValueError: If the grid has the wrong shape or an invalid height.

    Examples:
        >>> validate_pile([[0, 1], [2, 3]], 2, 2)
        >>> validate_pile([[0]], 1, 2)
        Traceback (most recent call last):
        ...
        ValueError: pile must have exactly 2 columns in every row
        >>> validate_pile([[0, -1]], 1, 2)
        Traceback (most recent call last):
        ...
        ValueError: pile heights must be non-negative integers
    """
    if len(pile) != rows:
        raise ValueError(f"pile must have exactly {rows} rows")

    for pile_row in pile:
        if len(pile_row) != columns:
            raise ValueError(
                f"pile must have exactly {columns} columns in every row"
            )
        for height in pile_row:
            if not isinstance(height, int) or height < 0:
                raise ValueError("pile heights must be non-negative integers")


class SandpileView:
    """A persistent, display-only Matplotlib window for a sandpile.

    Args:
        rows: Number of pile rows.
        columns: Number of pile columns.

    The caller creates one view and calls update when a redraw is needed. The
    view never reads input itself.

    Examples:
        >>> view = SandpileView(2, 2)
        >>> view.update([[0, 1], [2, 3]], 6, 0, 0)
        >>> view.close()
    """

    def __init__(self, rows: int, columns: int) -> None:
        """Create a window for a pile with the given dimensions.

        Raises:
            ValueError: If either dimension is not positive.

        Examples:
            >>> view = SandpileView(1, 1)
            >>> view.rows, view.columns
            (1, 1)
            >>> view.close()
        """
        if rows <= 0 or columns <= 0:
            raise ValueError("rows and columns must both be positive")

        self.rows = rows
        self.columns = columns
        self.figure: Figure
        self.axes: Axes
        self.image: AxesImage
        self.figure, self.axes = plt.subplots()

        colours = ["#fff4c2", "#f4d06f", "#d99a3d", "#9d5b26"]
        colour_map = ListedColormap(colours)
        colour_norm = BoundaryNorm([-0.5, 0.5, 1.5, 2.5, 3.5], len(colours))
        empty_pile: Pile = [[0 for _ in range(columns)] for _ in range(rows)]
        self.image = self.axes.imshow(
            empty_pile,
            cmap=colour_map,
            norm=colour_norm,
            interpolation="nearest",
        )
        self.axes.set_xlabel("column")
        self.axes.set_ylabel("row")
        self.axes.set_xticks(range(columns))
        self.axes.set_yticks(range(rows))
        self.figure.colorbar(self.image, ax=self.axes, ticks=[0, 1, 2, 3])
        self.figure.tight_layout()
        plt.ion()
        plt.show(block=False)

    def update(
        self,
        pile: Pile,
        grains_added: int,
        grains_lost: int,
        topplings: int,
    ) -> None:
        """Redraw the pile and show its current counters.

        The caller must calculate and maintain the three counters outside this
        viewing module. They are used only as labels in the figure title; this
        method does not calculate or update them.

        Args:
            pile: A rectangular height grid with this view's dimensions.
            grains_added: Total number of grains added by the CLI.
            grains_lost: Total number of grains that left at an edge.
            topplings: Total number of completed topplings.

        Examples:
            >>> view = SandpileView(1, 2)
            >>> view.update([[3, 0]], 3, 0, 0)
            >>> view.close()
        """
        validate_pile(pile, self.rows, self.columns)
        self.image.set_data(pile)
        self.axes.set_title(
            "Abelian sandpile | "
            f"added: {grains_added} | lost: {grains_lost} | "
            f"topplings: {topplings}"
        )
        self.figure.canvas.draw_idle()
        self.figure.canvas.flush_events()
        plt.pause(0.001)

    def pause(self, seconds: float) -> None:
        """Keep the display responsive for a non-negative number of seconds.

        Args:
            seconds: Length of the pause.

        Examples:
            >>> view = SandpileView(1, 1)
            >>> view.pause(0.0)
            >>> view.close()
        """
        if seconds < 0.0:
            raise ValueError("seconds must not be negative")
        if seconds > 0.0:
            plt.pause(seconds)

    def close(self) -> None:
        """Close this view's Matplotlib window.

        Examples:
            >>> view = SandpileView(1, 1)
            >>> view.close()
        """
        plt.close(self.figure)

