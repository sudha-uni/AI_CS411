import time
import sys
from collections import deque

# defining direction vectors for the four possible moves in a 4x4 grid (UP, DOWN, LEFT, RIGHT)
MOVES = {
    'UP': -4, 'DOWN': 4, 'LEFT': -1, 'RIGHT': 1
}

# defining goal state for the 15-puzzle
GOAL_STATE = tuple(range(1, 16)) + (0,)

# node class - each node stores the current puzzle state, its parent node, the move that led to this state, and the depth in the tree
class Node:
    def __init__(self, state, parent=None, move=None, depth=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth

    # checks if the current state is the goal state
    def is_goal(self):
        return self.state == GOAL_STATE

    # backtracking
    def get_path(self):
        node, path = self, []
        while node:
            if node.move:
                path.append(node.move)
            node = node.parent
        return path[::-1]
    
    # storing states
    def __hash__(self):
        return hash(self.state)

    def __eq__(self, other):
        return self.state == other.state

# valid moves from current state
def get_possible_moves(state):
    zero_index = state.index(0)
    moves = []
    if zero_index % 4 > 0:  
        moves.append('LEFT')
    if zero_index % 4 < 3:  
        moves.append('RIGHT')
    if zero_index // 4 > 0:  
        moves.append('UP')
    if zero_index // 4 < 3:  
        moves.append('DOWN')
    return moves

def apply_move(state, move):
    zero_index = state.index(0)
    move_offset = MOVES[move]
    new_zero_index = zero_index + move_offset

    new_state = list(state)
    new_state[zero_index], new_state[new_zero_index] = new_state[new_zero_index], new_state[zero_index]

    return tuple(new_state)

# cycle detection function to avoid exploring repeated states in the search
def is_cycle(node):
    ancestor = node.parent
    while ancestor:
        if ancestor.state == node.state:
            return True
        ancestor = ancestor.parent
    return False

# depth limited search
def depth_limited_search(start, depth_limit):
    frontier = deque([Node(start)])
    nodes_expanded = 0
    memory_used = 0

    while frontier:
        node = frontier.pop()
        nodes_expanded += 1

        # memory usage calculation
        memory_used += sys.getsizeof(node)
        memory_used += sys.getsizeof(node.state)
        if node.parent:
            memory_used += sys.getsizeof(node.parent)

        if node.is_goal():
            return node, nodes_expanded, memory_used, False

        if node.depth < depth_limit:
            for move in get_possible_moves(node.state):
                new_state = apply_move(node.state, move)
                child_node = Node(new_state, node, move, node.depth + 1)

                if not is_cycle(child_node):
                    frontier.append(child_node)

    return None, nodes_expanded, memory_used, True  # no solution

# IDDFS
def iterative_deepening_search(start):
    depth = 0
    total_nodes_expanded = 0
    total_memory_used = 0

    while True:
        result, nodes_expanded, memory_used, cutoff = depth_limited_search(start, depth)
        total_nodes_expanded += nodes_expanded
        total_memory_used += memory_used
        if result:
            return result.get_path(), total_nodes_expanded, total_memory_used, False
        if not cutoff:
            return None, total_nodes_expanded, total_memory_used, True
        depth += 1

def main():
    print("Enter the 15-puzzle board as 16 space-separated numbers (use 0 for the blank space):")
    user_input = input().strip()
    board = tuple(map(int, user_input.split()))

    if len(board) != 16 or set(board) != set(range(16)):
        print("Invalid input. Please enter exactly 16 distinct numbers from 0 to 15.")
        return

    start_time = time.time()
    solution, nodes_expanded, total_memory_used, failure = iterative_deepening_search(board)
    end_time = time.time()
    if failure:
        print("No solution found.")
    else:
        print(f"Moves: {solution}")
    
    print(f"Number of Nodes Expanded: {nodes_expanded}")
    print(f"Total Memory Used (bytes): {total_memory_used}")
    print(f"Time Taken: {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    main()
