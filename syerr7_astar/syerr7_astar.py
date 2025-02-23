import copy
import time
import sys

class Node:
    def __init__(self, position, moves, heuristic):
        self._position = position
        self._moves = moves
        self._heuristic = heuristic
        self._hScore = None

    def getPosition(self):
        return copy.deepcopy(self._position)

    def getGScore(self):
        return len(self._moves)

    def getHScore(self):
        if self._hScore is None:
            self._hScore = self._heuristic.compute(self)
        return self._hScore

    def getFScore(self):
        return self.getGScore() + self.getHScore()

    def getMoves(self):
        return copy.copy(self._moves)

    def getHeuristic(self):
        return self._heuristic

    def getCoordByValue(self, value):
        for i, row in enumerate(self._position):
            if value in row:
                return [i, row.index(value)]
        return None

class Build_Node:
    def getChildNodes(self, node):
        children = []
        iSpace, jSpace = node.getCoordByValue(0)
        for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            iSwap, jSwap = iSpace + i, jSpace + j
            if 0 <= iSwap < 4 and 0 <= jSwap < 4:
                position = node.getPosition()
                position[iSpace][jSpace], position[iSwap][jSwap] = position[iSwap][jSwap], 0
                moves = node.getMoves()
                moves.append(self._getMoveNameFromDelta(i, j))
                child = Node(position, moves, node.getHeuristic())
                children.append(child)
        return children

    def _getMoveNameFromDelta(self, iDelta, jDelta):
        if iDelta == -1:
            return 'up'
        if iDelta == 1:
            return 'down'
        if jDelta == -1:
            return 'left'
        if jDelta == 1:
            return 'right'

class Node_Pool:
    def __init__(self):
        self._pool = []
        self._history = {}
        self._nodes_expanded = 0
        self._memory_used = 0

    def add(self, node):
        position_str = str(node.getPosition())
        if position_str in self._history:
            return
        self._history[position_str] = True
        self._insort(node)
        self._memory_used += self._get_node_size(node)

    def pop(self):
        self._nodes_expanded += 1
        node = self._pool.pop(0)
        self._memory_used -= self._get_node_size(node)
        return node

    def isEmpty(self):
        return len(self._pool) == 0

    def _insort(self, node):
        lo, hi = 0, len(self._pool)
        while lo < hi:
            mid = (lo + hi) // 2
            if node.getFScore() < self._pool[mid].getFScore():
                hi = mid
            else:
                lo = mid + 1
        self._pool.insert(lo, node)

    def getNodesExpanded(self):
        return self._nodes_expanded

    def getMemoryUsed(self):
        return self._memory_used

    def _get_node_size(self, node):
        size = sys.getsizeof(node)
        size += sys.getsizeof(node._position)
        size += sys.getsizeof(node._moves)
        size += sys.getsizeof(node._heuristic)
        size += sys.getsizeof(node._hScore)
        return size

class A_Star:
    def __init__(self, heuristic):
        self._nodePool = Node_Pool()
        self._nodeBuilder = Build_Node()
        self._heuristic = heuristic

    def solve(self, position):
        self._bootstrap(position)
        while not self._nodePool.isEmpty():
            currentNode = self._nodePool.pop()
            if currentNode.getHScore() == 0:
                return currentNode.getMoves(), self._nodePool.getNodesExpanded(), self._nodePool.getMemoryUsed()
            children = self._nodeBuilder.getChildNodes(currentNode)
            for child in children:
                self._nodePool.add(child)
        return None, self._nodePool.getNodesExpanded(), self._nodePool.getMemoryUsed()

    def _bootstrap(self, position):
        initial_node = Node(position, [], self._heuristic)
        self._nodePool.add(initial_node)

class Heuristic_Class:
    def __init__(self, type):
        self.type = type

    def compute(self, node):
        if self.type == "misplaced":
            return self._misplaced_tiles(node)
        elif self.type == "manhattan":
            return self._manhattan_distance(node)
        else:
            raise ValueError(f"Unknown heuristic type: {self.type}")

    def _misplaced_tiles(self, node):
        position = node.getPosition()
        misplaced_count = 0
        expected = 1
        for i in range(4):
            for j in range(4):
                if position[i][j] != 0 and position[i][j] != expected:
                    misplaced_count += 1
                expected += 1
        return misplaced_count

    def _manhattan_distance(self, node):
        position = node.getPosition()
        total_distance = 0
        for i in range(4):
            for j in range(4):
                value = position[i][j]
                if value != 0:
                    target_i, target_j = divmod(value - 1, 4)
                    total_distance += abs(i - target_i) + abs(j - target_j)
        return total_distance

def get_user_input():
    while True:
        try:
            user_input = input("Enter 16 numbers (0-15) separated by spaces: ")
            numbers = list(map(int, user_input.split()))
            if len(numbers) != 16:
                print(f"Invalid input: You entered {len(numbers)} numbers. Please enter exactly 16 numbers.")
                continue
            if not all(0 <= n <= 15 for n in numbers) or len(set(numbers)) != 16:
                raise ValueError
            return [numbers[i:i+4] for i in range(0, 16, 4)]
        except ValueError:
            print("Invalid input. Please ensure you enter 16 unique numbers between 0 and 15, separated by spaces.")

def get_heuristic_choice():
    while True:
        print("Choose the heuristic to use:")
        print("1. Number of misplaced tiles")
        print("2. Manhattan Distance")
        choice = input("Enter your choice (1 or 2): ")
        if choice == "1":
            return Heuristic_Class("misplaced")
        elif choice == "2":
            return Heuristic_Class("manhattan")
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    position = get_user_input()
    heuristic = get_heuristic_choice()
    a_star_solver = A_Star(heuristic)

    start_time = time.time()  # Record start time
    solution, nodes_expanded, memory_used = a_star_solver.solve(position)
    end_time = time.time()  # Record end time

    # Display the solution
    if solution is not None:
        print("Solution found!")
        print("Moves:", solution)
        print("Number of nodes expanded:", nodes_expanded)
        print("Memory used (in bytes):", memory_used)
        print("Time taken (in seconds):", end_time - start_time)  # Print time taken
    else:
        print("No solution found.")
