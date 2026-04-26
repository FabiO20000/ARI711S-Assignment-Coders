# This class represents each node in our search tree.
# In simple terms, each node stores a position in the grid
# along with information about how we got there.

class Node:
    def __init__(self, state, parent=None, action=None, cost=0):
        # Here we store the current position (row, col)
        self.state = state

        # This keeps track of the previous node (used to reconstruct the path later)
        self.parent = parent

        # The action taken to reach this node (not heavily used here but good practice)
        self.action = action

        # g(n): the cost from the start node to this node
        self.cost = cost

    def __lt__(self, other):
        # This method allows nodes to be compared in a priority queue
        # We compare based on cost so that lower-cost nodes are prioritized
        return self.cost < other.cost