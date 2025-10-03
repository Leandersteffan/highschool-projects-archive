import random
import matplotlib.pyplot as plt
from matplotlib import colors


def visualize_labyrinth(labyrinth):
    rows = len(labyrinth)
    cols = len(labyrinth[0])

    # Create a color map for visualization
    cmap = colors.ListedColormap(['black', 'white', 'gray', 'red'])

    # Create a matrix to represent the labyrinth for visualization
    labyrinth_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if labyrinth[i][j] == '8':
                labyrinth_matrix[i][j] = 0  # Wall (black)
            elif labyrinth[i][j] == '0':
                labyrinth_matrix[i][j] = 1  # Free way (white)
            elif labyrinth[i][j] == '1':
                labyrinth_matrix[i][j] = 2  # Start position (gray)
            else:
                labyrinth_matrix[i][j] = 3  # Random element (red)

    # Create the figure and plot the labyrinth
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.imshow(labyrinth_matrix, cmap=cmap, origin='lower')

    # Set the ticks and labels
    ax.set_xticks(range(cols))
    ax.set_yticks(range(rows))
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    # Set the grid lines
    ax.set_xticks([x - 0.5 for x in range(1, cols)], minor=True)
    ax.set_yticks([y - 0.5 for y in range(1, rows)], minor=True)
    ax.grid(which='minor', color='gray', linestyle='-', linewidth=1)

    plt.show()

'''def create_labyrinth(rows, cols):
    labyrinth = [['8' for _ in range(cols)] for _ in range(rows)]

    # Set the entry point
    labyrinth[0][0] = '1'

    # Set random elements
    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            if random.random() < 0.2:  # Adjust the probability as desired
                labyrinth[row][col] = '2'

    return labyrinth'''

def create_labyrinth(size):
    # Initialize the labyrinth grid with walls
    labyrinth = [['8'] * size for _ in range(size)]

    # Set the starting position
    start_row, start_col = random.randint(0, size-1), random.randint(0, size-1)
    labyrinth[start_row][start_col] = '1'

    # Recursive function to create paths in the labyrinth
    def create_paths(row, col):
        # Define possible directions (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        random.shuffle(directions)

        for drow, dcol in directions:
            new_row, new_col = row + drow, col + dcol

            # Check if the new position is within the labyrinth boundaries
            if 0 <= new_row < size and 0 <= new_col < size and labyrinth[new_row][new_col] == '8':
                # Count the number of neighboring walls
                wall_count = 0
                for drow, dcol in directions:
                    neighbor_row, neighbor_col = new_row + drow, new_col + dcol
                    if 0 <= neighbor_row < size and 0 <= neighbor_col < size and labyrinth[neighbor_row][neighbor_col] == '8':
                        wall_count += 1

                # Create a path if there are exactly 3 neighboring walls
                if wall_count == 3:
                    labyrinth[new_row][new_col] = '0'  # Mark the position as a free way
                    create_paths(new_row, new_col)  # Recursively create paths from the new position

    create_paths(start_row, start_col)
    return labyrinth

labyrinth = create_labyrinth(50)
print(labyrinth)
visualize_labyrinth(labyrinth)
