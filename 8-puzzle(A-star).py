from collections import deque

# Goal configuration (target state)
goal_state = [1,2,4,5,3,6,7,8,0]

# Heuristic function: Manhattan distance
def heuristic(state):
    misplaced = 0
    for i in range(9):
        if state[i] != goal_state[i] and state[i] != 0:
            misplaced += 1
    return misplaced

# Function to generate valid neighbors
def get_neighbors(state):
    neighbors = []
    index_of_blank = state.index(0)
    x, y = index_of_blank // 3, index_of_blank % 3
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    for dx, dy in moves:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_index = new_x * 3 + new_y
            # Swap the blank space with the tile
            new_state = state[:]
            new_state[index_of_blank], new_state[new_index] = new_state[new_index], new_state[index_of_blank]
            neighbors.append(new_state)
    return neighbors

# A* search algorithm with a dictionary for fast state retrieval
def a_star(start):
    open_set = {tuple(start): heuristic(start)}  # Priority queue simulated using a dictionary
    came_from = {}  # To reconstruct the path
    g_score = {tuple(start): 0}  # Cost from start to current state
    f_score = {tuple(start): heuristic(start)}  # Estimated total cost

    while open_set:
        # Get the state with the lowest f_score (this time we remove the min from the dictionary)
        current = min(open_set, key=open_set.get)  # Get the state with the minimum f_score

        # If we reach the goal state
        if list(current) == goal_state:
            return reconstruct_path(came_from, current)

        del open_set[current]  # Remove the state from open_set

        # Generate neighbors
        for neighbor in get_neighbors(list(current)):
            tentative_g_score = g_score[current] + 1  # Cost to move is 1

            if tuple(neighbor) not in g_score or tentative_g_score < g_score[tuple(neighbor)]:
                came_from[tuple(neighbor)] = current
                g_score[tuple(neighbor)] = tentative_g_score
                f_score[tuple(neighbor)] = g_score[tuple(neighbor)] + heuristic(neighbor)
                open_set[tuple(neighbor)] = f_score[tuple(neighbor)]  # Add neighbor to open_set with f_score

    return None  # If no solution exists

# Reconstruct the path from start to goal
def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

# Helper function to print the solution path
def print_solution(path):
    for state in path:
        for i in range(0, 9, 3):
            print(state[i:i+3])
        print('||||||||||||||')

# Example usage
start_state = [1,2,3,4,5,6,7,8,0]
path = a_star(start_state)
if path:
    print("Solution found:")
    print_solution(path)
else:
    print("No solution found.")