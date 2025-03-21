AI ASSIGNMENT_4

Name of Student: Yerramsetty Sudha Sree
UIN: 662518247

15 puzzle is a sliding puzzle game with numbered squares arranged in 4X4 grid with one tile missing.
The puzzle is solved when the numbers are arranged in ascending order and the blank tile is last.
The actions are defined in terms of direction where empty square can be moved to from it's current state: UP(U), Down(D), Left(L), or Right(R).

IDDFS (Iterative Deepening Depth-First Search) is a search algorithm that combines the depth-first search's space efficiency with the breadth-first search's ability to find the shortest path.
It explores nodes depth by depth, starting from depth 0, gradually increasing the depth limit until the goal state is found.
This approach ensures optimal solutions while using less memory compared to BFS. 

Instructions to run the code:

    1)  Before running the script, make sure you have Python installed.
        If not, download Python from https://www.python.org/downloads/.
        Ensure you install Python 3.8 or higher.
        Make sure PATH environment variables are set to Python312 and Python312 Scripts. (for Python 3.12.4 which is the one I'm using)
    2)  Extract the files from <netid>_iddfs.zip into a folder.
    3)  Open Terminal/Command Prompt and navigate to the directory where the file is located using cd.
    4)  Run the file using the command: "python <filename>.py"
    5)  When prompted to input the initial configuration, enter numbers between [0, 15] inclusively with spaces seperating each number.
        Here, 0 represents the blank space in the puzzle.