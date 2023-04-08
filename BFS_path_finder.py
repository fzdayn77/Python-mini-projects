import curses
from curses import wrapper
import queue
import time

'''
Symbols:
  S -> start-point
  E -> end-point
  # -> obstacle
  X -> path

If you want to change the maze, you need to change the first parameter
in the find_path-function-call in the main-function to the corresponding
maze-name.
'''

maze_1 = [
    ["#", "S", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "E", "#"]
]

maze_2 = [
    ["#", "#", "#", "#", "#", "#", "#", "S", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "E", "#", "#", "#", "#", "#"]
]

maze_3 = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["S", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "E"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#"]
]


def print_maze(maze, stdscr, path=[]):
    BLUE = curses.color_pair(1)
    GREEN = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                stdscr.addstr(i*2, j*3, 'X', GREEN)
            else:
                stdscr.addstr(i*2, j*3, value, BLUE)


def find_start(maze, start_char):
    '''
    returns the coordinates of the starting point
    '''
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start_char:
                return i, j
            

def find_path(maze, stdscr):
    start_char = 'S'
    end_char = 'E'
    start_position = find_start(maze, start_char)

    q = queue.Queue()  # stores the cuurent position and the path
    q.put((start_position, [start_position]))

    visited = set()

    while not q.empty():
        current_pos, path = q.get()
        row, column = current_pos

        stdscr.clear()
        print_maze(maze, stdscr, path)
        time.sleep(0.3)
        stdscr.refresh()

        if maze[row][column] == end_char:
            return path
        
        neighbors = find_neighbors(maze, row, column)
        for neighbor in neighbors:
            neighbor_row, neighbor_column = neighbor
            if (neighbor in visited) or (maze[neighbor_row][neighbor_column] == '#'):
                continue

            new_path = path + [neighbor]
            q.put((neighbor, new_path))
            visited.add(neighbor)


def find_neighbors(maze, row, column):
    '''
    returns a list of all the neighbors to a single node
    '''
    neighbors = []

    if row > 0:  # going UP
        neighbors.append((row - 1, column))
    if row < len(maze)-1:  # going DOWN
        neighbors.append((row + 1, column))
    if column > 0:  # going LEFT
        neighbors.append((row, column - 1))
    if column < len(maze[0])-1:  # going RIGHT
        neighbors.append((row, column + 1))
    
    return neighbors


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)

    #----------- change maze-name here -----------#
    find_path(maze_1, stdscr)
    stdscr.getch()
    

wrapper(main)