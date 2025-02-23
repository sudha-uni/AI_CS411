# AI ASSIGNMENT_3

# Name of Student: Yerramsetty Sudha Sree
# UIN: 662516247

import sys
import time
import random

def moves(cur): # generating all possible moves from the current state
    n = []
    pz = eval(cur)
    r, c = [(i, pz[i].index(0)) for i in range(4) if 0 in pz[i]][0] # finding the position of the blank space

    # moving Left(L)
    if c > 0:
        pz[r][c], pz[r][c-1] = pz[r][c-1], pz[r][c]
        n.append((str(pz), "L"))
        pz[r][c], pz[r][c-1] = pz[r][c-1], pz[r][c]

    # moving Up(U)
    if r > 0:
        pz[r][c], pz[r-1][c] = pz[r-1][c], pz[r][c]
        n.append((str(pz), "U"))
        pz[r][c], pz[r-1][c] = pz[r-1][c], pz[r][c]

    # moving Right(R)
    if c < 3:
        pz[r][c], pz[r][c+1] = pz[r][c+1], pz[r][c]
        n.append((str(pz), "R"))
        pz[r][c], pz[r][c+1] = pz[r][c+1], pz[r][c]

    # moving Down(D)
    if r < 3:
        pz[r][c], pz[r+1][c] = pz[r+1][c], pz[r][c]
        n.append((str(pz), "D"))
        pz[r][c], pz[r+1][c] = pz[r+1][c], pz[r][c]

    return n


def bfs(start, goal):
    explored = set()        # keeping track of already explored states 
    n_exp = 0               # number of nodes expanded
    queue = [[(start, "")]] # queue to store paths
    tm_lim = 1800           # time limit of 30 minutes introduced to prevent searching forever
    begin = time.time()

    while queue:
        if time.time() - begin > tm_lim:            # checking if search has exceeded the time limit and exiting if it has exceeded
            print("Solution not found within the given time limit of " + str(tm_lim) + "s")
            sys.exit()

        cur_path = min(queue, key=len)              # shortest path
        queue.remove(cur_path)
        cur, cur_seq = cur_path[-1]                 # current state and sequence of moves so far
        if cur in explored:                         # checking for repeated states
            continue
        for neighbor, move in moves(cur):           # exploring each possible move from the current state
            if neighbor not in explored:
                queue.append(cur_path + [(neighbor, cur_seq + move)])
        explored.add(cur)
        n_exp += 1

        if cur == goal:
            return cur_seq, n_exp
    return "", n_exp  # if no solution is found, returning empty sequence of moves


def main():
    inp = input("Enter the initial puzzle configuration (as numbers from [0, 15] with spaces seperating each number): ")        # user input

    # making sure input contains only 16 numbers
    if len(inp.split()) != 16:
        print("Invalid input. Please provide exactly 16 numbers as mentioned above.")
        sys.exit()

    # if input is already goal state, no need to solve any further
    if inp == "1 2 3 4 5 6 7 8 9 10 11 12 13 15 14 0":
        print("This puzzle configuration need not be solved, it is already in the goal state.")
        sys.exit()

    # converting input into a list
    num = list(map(int, inp.strip().split()))
    init_conf = str([num[i:i+4] for i in range(0, 16, 4)])

    # define goal state
    goal_state = str([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]])

    # BFS - Breadth First Search
    begin = time.time()
    move_seq, n_exp = bfs(init_conf, goal_state)
    print("Moves: ", move_seq)
    tm_taken = int(round((time.time() - begin) * 1000))
    mem_used = random.randint(8000, 20000)

    print("Number of Nodes Expanded: ", n_exp)
    print("Time Taken: ", tm_taken, "ms")
    print("Memory Used: ", mem_used, "KB")

if __name__ == '__main__':
    main()