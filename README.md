# Maze Generator

This is a Python program that generates mazes using the recursive backtracking algorithm. It provides a visual representation of the generated maze using the OpenCV library.

## Features
- Generates mazes of specified dimensions
- Customizable cell and wall widths
- Custom starting row and column for the generation
- Visualization of the generated maze using OpenCV

## Usage
To use the maze generator, follow these steps:

1. Create a Python file (e.g., `maze_generator.py`) and copy the provided code into it.
2. Optionally, create a `main.py` file to run the maze generator.
3. Run the Python script.
4. To quit, press `q`.
5. You can save the maze by pressing `a`. Note that you can also save if the maze generation is incomplete, saving the maze generated till that time.

### Example (main.py)
For making a maze of height=40, width=30, cell width=20, wall width=10 and starting the maze generation at row=2 and column=3 , edit the main.py file to:
```python
from maze_generator import *

if __name__ == "__main__":
    maze = Maze(nx=40, ny=30, ix=2, iy=3, cell_width=20, wall_width=10)
    Maze.start_time = time.time()
    maze.make_maze()
``` 
## Acknowledgments
- This maze generator is inspired by the recursive backtracking algorithm.
- Special thanks to OpenCV for providing visualization tools.

## License

This project is licensed under the MIT License, which allows for unrestricted use, modification, and distribution.
