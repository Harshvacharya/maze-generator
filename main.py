from maze_generator import *


if __name__=="__main__":
    
    h,w=40,30
    ix,iy=int(h/2),int(w/2)
    maze=Maze(h,w,ix,iy)
    Maze.start_time=time.time()
    maze.make_maze()