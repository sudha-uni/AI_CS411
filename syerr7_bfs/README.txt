AI ASSIGNMENT_3

Name of Student: Yerramsetty Sudha Sree
UIN: 662518247

15 puzzle is a sliding puzzle game with numbered squares arranged in 4X4 grid with one tile missing.
The puzzle is solved when the numbers are arranged in order amd the blank tile is last.
The actions are defined in terms of direction where empty square can be moved to UP (U), Down(D), Left(L), Right(R).

BFS (Breadth-First Search) is a search algorithm used to explore the shortest path to a goal state by expanding nodes level by level. 
It explores all possible moves from the current state of the 15 puzzle until it reaches the goal state with a set time limit.
If you don't want to use a time limit, just comment out lines 46, 50, 51 and 52. 

Instructions to run the code:

    1)  Before running the script, make sure you have Python installed.
        If not, download Python from https://www.python.org/downloads/.
        Ensure you install Python 3.8 or higher.
        Make sure PATH environment variables are set to Python312 and Python312 Scripts. (for Python 3.12.4 which is the one I'm using)
    2)  Extract the files from <netid>_bfs.zip into a folder.
    3)  Open Terminal/Command Prompt and navigate to the directory where the file is located using cd.
    4)  Run the file using the command: "python <filename>.py"
    5)  When prompted to input the initial configuration, enter numbers between [0, 15] with spaces seperating each number.
        Here, 0 represents the blank space in the puzzle.