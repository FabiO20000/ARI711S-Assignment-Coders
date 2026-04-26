from warehouse import Warehouse
from algorithms import greedy_search, astar_search, reconstruct_path

# This is the main entry point of our program
# It loads the map, runs both algorithms, and prints results

def run():
    # Load warehouse map from file
    problem = Warehouse("maps/warehouse1.txt")

    print("----- GREEDY SEARCH -----")
    greedy_result = greedy_search(problem)

    # Print the path found by greedy search
    print("Path:", reconstruct_path(greedy_result))

    print("\n----- A* SEARCH -----")
    astar_result = astar_search(problem)

    # Print the path found by A*
    print("Path:", reconstruct_path(astar_result))


if __name__ == "__main__":
    run()