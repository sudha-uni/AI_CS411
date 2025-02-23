AI ASSIGNMENT_5

Name of Student: Yerramsetty Sudha Sree
UIN: 662518247

15 puzzle is a sliding puzzle game with numbered squares arranged in 4X4 grid with one tile missing.
The puzzle is solved when the numbers are arranged in ascending order and the blank tile is last.
The actions are defined in terms of direction where empty square can be moved to from it's current state: UP(U), Down(D), Left(L), or Right(R).

A* (A-star) is an efficient search algorithm that finds the shortest path to a goal by combining Dijkstra's algorithm and greedy best-first search. 
It uses the cost function f(n) = g(n) + h(n), where g(n) is the cost from the start and h(n) is a heuristic estimate to the goal. 
By leveraging heuristics like the number of misplaced tiles or Manhattan distance, A* narrows the search space, ensuring optimal and complete solutions 
with relatively low memory usage compared to breadth-first search (BFS).

Instructions to run the code:

    1)  Before running the script, make sure you have Python installed.
        If not, download Python from https://www.python.org/downloads/.
        Ensure you install Python 3.8 or higher.
        Make sure PATH environment variables are set to Python312 and Python312 Scripts. (for Python 3.12.4 which is the one I'm using)
    2)  Extract the files from <netid>_astar.zip into a folder.
    3)  Open Terminal/Command Prompt and navigate to the directory where the file is located using cd.
    4)  Run the file using the command: "python <filename>.py"
    5)  When prompted to input the initial configuration, first enter the heuristic you want to use for the A-star algorithm, 
        either: 
            1) Number of misplaced tiles 
                    (or) 
            2) Manhattan distance
    6)  After that, enter numbers between [0, 15] inclusively with spaces seperating each number. Here, 0 represents the blank space in the puzzle.