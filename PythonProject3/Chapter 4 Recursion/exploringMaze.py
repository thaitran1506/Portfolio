"""
We will assume that our maze is divided up into squares. Each square of the maze is either open or occupied by a section
of the wall. The turtle can only pass through the open squares of the maze. If the turtle bumps into a wall, it must
try a different direction. Requires a systematic approach. Here is the procedure

    1. From the starting position we will first try going north one square and then recursively try our procedure from there
    2. If we are not successful by trying a northern path as the first step then we will take a step to the south and
    recursively try our procedure.
    3. If south does not work then we will try a step to the west as our first step and recursively try our procedure.
    4. If north, south, and west have not been successful then we will apply the procedure recursively from a position
    one step to our east
    5. If none of these directions works then there is no way to get out of the maze and we fail.

That sounds easy, but there are a couple of details to talk about first. Suppose we take our first recursive step by
going north. By following our procedure, our next step would also be to the north. But if the north is blocked by the
wall, we must look at the next step of the procedure and try going south. Unfortunately, that will take us right back
to our original starting place. If we apply the recursive procedure from there, we will just go back one step to the
north and be in an infinite loop. So we must have a strategy to remember where we have been. In this case we will assume
that we have a bag of bread crumbs we can drop along our way. If we take a step in a certain direction and find that
there is a bread crumb already on that square, we know what we should immediately back up and try the next direction
in our procedure. As we will see when we look at the code for this algorithm, back up is as simple as returning from
a recursive function call.
As we do for all recursive algorithm, let us review the base cases. There are four base cases to consider:
    1. the turtle has run into a wall. Since the square is occupied by a wall, no further exploration can take place
    2. The turtle has found a square that has already been explored. We do not want to continue exploring from this
    position so we don't get into a loop
    3. We have found an outside edge, not occupied by a wall. In other words, we have found an exit from the maze
    4. We have explored a square unsuccessfully in all four directions.

We are going to use the turtle module to draw and explore the maze. The Maze object will provide the following methods
for us to use in writing our search algorithms:
    - __init__ reads a data file representing a maze, initializes the internal representation of the maze, and finds
    the starting position of the turtle.
    - draw_maze Draws the maze in a window on the screen
    - update_position updates the internal representation of the maze and changes the position of the turtle in the window
    - is_exit checks to see if the turtle has found an exit from the maze
The Maze class also overloads the index operator [] so that our algorithm can easily access the status of any particular
square
"""

import turtle
START = "S"
OBSTACLE = "+"
TRIED = "."
DEAD_END = "-"
PART_OF_PATH = "O"

class Maze:
    def __init__(self, maze_filename):
        with open(maze_filename, "r") as maze_file:
            self.maze_list = [
                [ch for ch in line.rstrip("\n")]
                for line in maze_file.readlines()
            ]
        self.rows_in_maze = len(self.maze_list)
        self.columns_in_maze = len(self.maze_list[0])
        for row_idx, row in enumerate(self.maze_list):
            if START in row:
                self.start_row = row_idx
                self.start_col = row.index(START)
                break
        self.x_translate = -self.columns_in_maze / 2
        self.y_translate = self.rows_in_maze / 2
        self.t = turtle.Turtle()
