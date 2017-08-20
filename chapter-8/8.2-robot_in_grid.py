def get_robot_path(grid):
    if grid is None:
        return []
    path = []
    get_robot_path_recur(grid, (0, 0), path, set())
    return path

def get_robot_path_recur(grid, pos, path, no_path_point):
    row, col = pos
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
        return False
    if not grid[row][col]:
        return False

    if pos in no_path_point:
        return False

    path.append(pos)
    if row == len(grid) - 1 and col == len(grid[0]) - 1:
        return True

    path_exists = get_robot_path_recur(grid, (row+1, col), path, no_path_point)
    if path_exists:
        return True
    path_exists = get_robot_path_recur(grid, (row, col+1), path, no_path_point)
    if path_exists:
        return True

    path.pop()
    no_path_point.add(pos)
    return False


if __name__ == '__main__':

    grid = [[False] * 4 for i in range(5)]

    grid[0][0] = True
    grid[0][1] = True
    grid[0][2] = True

    grid[1][1] = True
    grid[1][2] = True
    grid[1][3] = True

    grid[2][3] = True
    grid[3][3] = True
    grid[4][3] = True

    print(get_robot_path(grid))

    grid[3][3] = False

    print(get_robot_path(grid))
