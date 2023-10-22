#-------------------------------------------------------------------------------
# Name:        module8
# Purpose:
#
# Author:      akhil
#
# Created:     17/08/2023
# Copyright:   (c) akhil 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def is_solvable_dfs(grid):
    target = [[1, 2, 3], [4, 5, 6], [7, 8, 'B']]

    def grid_to_tuple(grid):
        return tuple(tuple(row) for row in grid)

    start = grid_to_tuple(grid)
    target_state = grid_to_tuple(target)

    visited = set()
    stack = [(start, 0)]

    while stack:
        current, depth = stack.pop()

        if current == target_state:
            return depth

        if current in visited:
            continue

        visited.add(current)

        row, col = -1, -1
        for r in range(3):
            for c in range(3):
                if current[r][c] == 'B':
                    row, col = r, c
                    break

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_grid = [list(row) for row in current]
                new_grid[row][col], new_grid[new_row][new_col] = new_grid[new_row][new_col], new_grid[row][col]
                new_state = grid_to_tuple(new_grid)
                stack.append((new_state, depth + 1))

    return -1  # No solution found

# Example usage
random_grid = [
    [3, 2, 1],
    [4, 5, 6],
    [8, 7, ]
]

steps = is_solvable_dfs(random_grid)
if steps != -1:
    print(f"Solution found in {steps} steps.")
else:
    print("No solution found.")