# Maze Generator

This is a maze generator written in Python using the OpenCV library to visualize the generated maze. The generator uses a recursive backtracking algorithm to create a maze with a specified number of rows and columns.

## Features
- Generates a maze of specified dimensions
- Allows customization of cell and wall widths
- Visualizes the generated maze using OpenCV

## Getting Started
To use the maze generator, follow these steps:

1. Ensure you have Python and OpenCV installed on your system.
2. Copy the provided Python code into a Python file (e.g., `maze_generator.py`).
3. Run the Python script.

## Usage
```python
# Define maze dimensions
nx, ny = 30, 30
# Define starting position
ix, iy = int(nx / 2), int(ny / 2)
# Create maze object with specified dimensions and cell/wall widths
maze = Maze(nx, ny, ix, iy, cell_width=4, wall_width=4)
# Generate and visualize the maze
maze.make_maze()
