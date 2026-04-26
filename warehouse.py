import math

# This class models our warehouse environment.
# It is responsible for:
# - Reading the grid
# - Finding the start (A) and goal (B)
# - Providing valid movements (neighbors)
# - Calculating the heuristic

class Warehouse:
    def __init__(self, filename):
        # Here we read the warehouse layout from a text file
        # Each line becomes a row in the grid
        with open(filename) as f:
            self.grid = [list(line.strip()) for line in f.readlines()]

        # Store grid dimensions
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])

        # Now we scan the grid to locate the start (A) and goal (B)
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == 'A':
                    # Found the starting position of the robot
                    self.start = (i, j)
                elif self.grid[i][j] == 'B':
                    # Found the goal position (target bin)
                    self.goal = (i, j)

    def neighbors(self, state):
        # This function returns all valid moves from the current position
        # We only allow movement up, down, left, right

        r, c = state

        # Define possible movements
        moves = [
            ("UP", (r-1, c)),
            ("DOWN", (r+1, c)),
            ("LEFT", (r, c-1)),
            ("RIGHT", (r, c+1))
        ]

        results = []

        # Here we check which moves are valid
        for action, (nr, nc) in moves:
            # Check boundaries (stay inside grid)
            if 0 <= nr < self.rows and 0 <= nc < self.cols:

                # Check if the cell is not a wall (#)
                if self.grid[nr][nc] != '#':
                    # If valid, we add it to the list of neighbors
                    results.append((action, (nr, nc)))

        # Return all valid moves from current state
        return results

    def heuristic(self, state):
        # This is our heuristic function (Euclidean distance)
        # It estimates how far we are from the goal

        x1, y1 = state
        x2, y2 = self.goal

        # Apply Euclidean distance formula
        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)