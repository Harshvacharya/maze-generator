# Maze Generator

This is a Python maze generator that generates mazes of customizable sizes.

## Features

- Generates mazes of arbitrary sizes
- Customizable cell width and wall width
- Visualization using OpenCV
- Randomized maze generation algorithm

## Usage

To generate a maze, create an instance of the `Maze` class with the desired parameters:

```python
nx, ny = 30, 30  # Size of the maze
ix, iy = int(nx / 2), int(ny / 2)  # Starting cell coordinates
maze = Maze(nx, ny, ix, iy, cell_width=4, wall_width=4)  # Create Maze instance
maze.make_maze()  # Generate the maze
