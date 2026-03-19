import random
from collections import deque
import time

GRID_SIZE = 20
density_map = {
    "low": 0.1,
    "medium": 0.2,
    "high": 0.35
}

def generate_grid(size, prob_density):
    matrix = [[0 for _ in range(size)] for _ in range(size)]
    for r in range(size):
        for c in range(size):
            if random.random() < prob_density:
                matrix[r][c] = 1
    return matrix

def run_bfs(matrix, start_pos, goal_pos):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    q = deque([start_pos])
    visited_set = {start_pos}
    parents = {}

    moves = [(1,0), (-1,0), (0,1), (0,-1)]
    nodes_expanded = 0

    while q:
        current = q.popleft()
        nodes_expanded += 1

        if current == goal_pos:
            found_path = []
            while current in parents:
                found_path.append(current)
                current = parents[current]
            found_path.append(start_pos)
            found_path.reverse()
            return found_path, nodes_expanded

        for move in moves:
            nxt = (current[0] + move[0], current[1] + move[1])

            if (0 <= nxt[0] < num_rows and
                0 <= nxt[1] < num_cols and
                matrix[nxt[0]][nxt[1]] == 0 and
                nxt not in visited_set):

                q.append(nxt)
                visited_set.add(nxt)
                parents[nxt] = current

    return None, nodes_expanded

level = "low"
chosen_density = density_map[level]
battle_grid = generate_grid(GRID_SIZE, chosen_density)

start_pt = (0, 0)
target_pt = (GRID_SIZE - 1, GRID_SIZE - 1)
battle_grid[start_pt[0]][start_pt[1]] = 0
battle_grid[target_pt[0]][target_pt[1]] = 0

t_start = time.time()
final_path, exp_nodes = run_bfs(battle_grid, start_pt, target_pt)
t_end = time.time()

print("Start:", start_pt)
print("Goal:", target_pt)
print("Density Level:", level)

if final_path:
    print("Path Found")
    print("Path:", final_path)
    print("Path Length:", len(final_path))
else:
    print("No Path Found")

print("\nMeasures of Effectiveness")
print("Nodes Expanded:", exp_nodes)
print("Execution Time:", t_end - t_start, "seconds")