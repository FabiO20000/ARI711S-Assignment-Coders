import heapq
from node import Node

# -------------------------------
# GREEDY BEST-FIRST SEARCH
# -------------------------------

def greedy_search(problem):
    # Here we initialise the starting node
    start = Node(problem.start)

    # The frontier is a priority queue (min-heap)
    frontier = []

    # In greedy search, priority = heuristic only
    heapq.heappush(frontier, (problem.heuristic(start.state), start))

    # We use a set to keep track of visited states
    explored = set()

    while frontier:
        # Remove the node with the lowest heuristic value
        _, current = heapq.heappop(frontier)

        # Check if we reached the goal
        if current.state == problem.goal:
            return current

        # Mark current state as explored
        explored.add(current.state)

        # Expand neighbors
        for action, state in problem.neighbors(current.state):
            if state not in explored:
                # Create a new node for each neighbor
                child = Node(state, current, action)

                # Push into frontier using heuristic as priority
                heapq.heappush(frontier, (problem.heuristic(state), child))

    return None


# -------------------------------
# A* SEARCH
# -------------------------------

def astar_search(problem):
    # Start node
    start = Node(problem.start)

    frontier = []

    # For A*, we start with f(n) = 0
    heapq.heappush(frontier, (0, start))

    explored = set()

    while frontier:
        # Pop node with lowest f(n)
        _, current = heapq.heappop(frontier)

        # Goal test
        if current.state == problem.goal:
            return current

        explored.add(current.state)

        # Explore neighbors
        for action, state in problem.neighbors(current.state):
            # g(n): cost so far
            g = current.cost + 1

            # h(n): heuristic
            h = problem.heuristic(state)

            # f(n) = g(n) + h(n)
            f = g + h

            if state not in explored:
                # Create new node with updated cost
                child = Node(state, current, action, g)

                # Push into priority queue using f(n)
                heapq.heappush(frontier, (f, child))

    return None


# -------------------------------
# PATH RECONSTRUCTION
# -------------------------------

def reconstruct_path(node):
    # This function traces back from goal to start using parent links
    path = []

    while node.parent:
        path.append(node.state)
        node = node.parent

    # Add the start node
    path.append(node.state)

    # Reverse to get correct order (start -> goal)
    return path[::-1]