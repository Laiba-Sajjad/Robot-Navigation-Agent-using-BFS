# Robot-Navigation-Agent-using-BFS
An AI based a robot navigation Agent using BFS, which can conduct blind searches to find its path from start to goal
state. As input, the system will take a description of the maize stored as a text file. The maize is a 2x2
grid with obstacles inside it.
The obstacles are filled rectangles of unknown dimensions and can be found anywhere in the maize.
The robot cannot be in those cells. There are 3 actions allowed. Up one cell (cost is 1), right one cell
(cost is 3), diagonally up towards the right (cost is 2).

The system will output:
1. The complete path if goal is found otherwise show path’s followed by algorithm to search for
goal
2. The sequence of actions performed to reach the goal from start
3. The total cost of the path
4. A grid which shows the path followed. You do not need graphics for this output. The grid can
be made textually using 1 for obstacles, 0 for empty cells and ‘#’ for path followed.

FORMAT OF INPUT FILE
dimensions of the grid (line one TotalCols x TotalRows)
start coordinates (line two)
goal coordinates (line three)
the grid itself (one line per row). There will be a zero for no obstacle and one for an obstacle. (for gird please see grid.txt file)
