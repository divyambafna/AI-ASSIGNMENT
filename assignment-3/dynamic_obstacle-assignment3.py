import random
from collections import deque

GRID_DIM = 15

def bfs_search(matrix, start_node, target_node):
    queue = deque([start_node])
    visited_nodes = {start_node}
    parent_map = {}
    
    while queue:
        cx, cy = queue.popleft()
        if (cx, cy) == target_node:
            route = []
            while (cx, cy) in parent_map:
                route.append((cx, cy))
                cx, cy = parent_map[(cx, cy)]
            route.append(start_node)
            return route[::-1]
            
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < GRID_DIM and 0 <= ny < GRID_DIM and matrix[nx][ny] == 0 and (nx, ny) not in visited_nodes:
                queue.append((nx, ny))
                visited_nodes.add((nx, ny))
                parent_map[(nx, ny)] = (cx, cy)
    return None

env_grid = [[0] * GRID_DIM for _ in range(GRID_DIM)]

for row in range(GRID_DIM):
    for col in range(GRID_DIM):
        if random.random() < 0.15:
            env_grid[row][col] = 1

start_pos = (0, 0)
goal_pos = (GRID_DIM - 1, GRID_DIM - 1)

env_grid[start_pos[0]][start_pos[1]] = 0
env_grid[goal_pos[0]][goal_pos[1]] = 0

current_pos = start_pos
total_steps = 0

while current_pos != goal_pos:
    current_path = bfs_search(env_grid, current_pos, goal_pos)
    if not current_path:
        print("No path available")
        break
        
    next_step = current_path[1]
    
    if random.random() < 0.2:
        rx = random.randint(0, GRID_DIM - 1)
        ry = random.randint(0, GRID_DIM - 1)
        env_grid[rx][ry] = 1
        
    if env_grid[next_step[0]][next_step[1]] == 1:
        continue
        
    current_pos = next_step
    total_steps += 1

print("Steps taken:", total_steps)
print("Reached Goal:", current_pos == goal_pos)

final_route = bfs_search(env_grid, start_pos, goal_pos)

print("\nBattlefield Grid")
for r in range(GRID_DIM):
    for c in range(GRID_DIM):
        if (r, c) == start_pos:
            print("S", end=" ")
        elif (r, c) == goal_pos:
            print("G", end=" ")
        elif final_route and (r, c) in final_route:
            print("*", end=" ")
        elif env_grid[r][c] == 1:
            print("#", end=" ")
        else:
            print(".", end=" ")
    print()
