import random
import numpy as np
import cv2
import time


class Cell:
    wall_pairs={'N':'S','S':'N','E':'W','W':'E'}
    
    def __init__(self,x,y):
        self.x,self.y=x,y
        self.walls={'N':True,'S':True,'W':True,'E':True}

    def check_neighbours(self):
        return all(self.walls.values())

    def merge(self,other,wall):
        self.walls[wall]=False
        other.walls[Cell.wall_pairs[wall]]=False


class Maze:
    def __init__(self,nx,ny,ix,iy,cell_width=4,wall_width=4):
        self.nx,self.ny,self.ix,self.iy=nx,ny,ix,iy
        self.cell_width,self.wall_width=2*(cell_width//2),2*(wall_width//2)
        try:
            self.map=[[Cell(x,y) for x in range(nx)] for y in range(ny)]
        except MemoryError:
            print(len(self.map),len(self.map[-1]))
        self.walls=['N','E','W','S']
        self.draw_image(width=((ny)*(self.cell_width+self.wall_width)+1),height=((nx)*(self.cell_width+self.wall_width)+1))

    def cell_at(self,x,y):
        return self.map[y][x]

    def draw_image(self,width,height,color=(0,0,0)):
        self.image=np.zeros((width,height,3),np.uint8)
        self.image[:]=color

    def get_neighbours(self,cell):
        neighbours=[]
        x,y=cell.x,cell.y
        self.moves=[('S',(0,1)),('E',(1,0)),('W',(-1,0)),('N',(0,-1))]
        for wall,(dx,dy) in self.moves:
            x2,y2=x+dx,y+dy
            if (0<= x2 < self.nx) and (0<=y2<self.ny):
                new_cell=self.cell_at(x2,y2)
                if new_cell.check_neighbours():
                    neighbours.append((wall,new_cell))
        return neighbours

    def color_cell(self,cell,color):
        x,y=cell.x*(self.cell_width+self.wall_width)+(self.cell_width+self.wall_width)//2,cell.y*(self.cell_width+self.wall_width)+(self.cell_width+self.wall_width)//2
        x1,y1=x-(self.cell_width)//2,y-(self.cell_width)//2
        x2,y2=x+(self.cell_width)//2,y+(self.cell_width)//2
        self.image[y1:y2+1,x1:x2+1]=color

    def color_wall(self,cell,color):
        cell_walls=[]
        for w in self.walls:
            if not cell.walls[w]:
                cell_walls.append(w)
                
        b=(self.cell_width)//2
        a=(self.cell_width+2*self.wall_width)//2
        x,y=cell.x*(self.cell_width+self.wall_width)+(self.cell_width+self.wall_width)//2,cell.y*(self.cell_width+self.wall_width)+(self.cell_width+self.wall_width)//2
        d={'N':(x-b,y-a,x+b,y-b),'S':(x-b,y+b,x+b,y+a),'E':(x+b,y-b,x+a,y+b),'W':(x-a,y-b,x-b,y+b)}
        for wall in cell_walls:
            x1,y1,x2,y2=d[wall]
            self.image[y1:y2+1,x1:x2+1]=color
            
    def color(self,cell,color):
        self.color_cell(cell,color)
        self.color_wall(cell,color)

    def make_maze2(self):
        self.cell_stack=np.array([])
        self.current_cell=self.cell_at(self.ix,self.iy)
        self.icell=self.current_cell
        self.n=self.nx*self.ny
        self.nv=1
        while True:
            if self.nv<self.n or self.current_cell!=self.icell:
                neighbours=self.get_neighbours(self.current_cell)
                if len(neighbours)==0:
                    self.color(self.current_cell,(255,255,255))
                    self.current_cell,self.cell_stack=self.cell_stack[-1],self.cell_stack[:-1]
                    continue
                wall,new_cell=random.choice(neighbours)
                self.current_cell.merge(new_cell,wall)
                self.cell_stack=np.append(self.cell_stack,[self.current_cell],axis=0)
                self.color(self.current_cell,(255,0,0))
                self.current_cell=new_cell
                self.nv+=1
            else:
                self.color(self.current_cell,(255,255,255))
                break
            '''
            cv2.imshow('Image',self.image)
            if cv2.waitKey(1) & 0xFF==ord('q'):
                cv2.destroyAllWindows()
                break
            
            if cv2.waitKey(1) & 0xFF==ord('a'):
                cv2.destroyAllWindows()
                cv2.imwrite('maze'+str(random.randint(10**3,10**4))+'.png',self.image)
                break'''

    def make_maze(self):
        self.cell_stack=[]
        self.current_cell=self.cell_at(self.ix,self.iy)
        self.icell=self.current_cell
        self.n=self.nx*self.ny
        self.nv=1
        while True:
            if self.nv<self.n or self.current_cell!=self.icell:
                neighbours=self.get_neighbours(self.current_cell)
                if len(neighbours)==0:
                    self.color(self.current_cell,(255,255,255))
                    self.current_cell=self.cell_stack.pop()
                    continue
                wall,new_cell=random.choice(neighbours)
                self.current_cell.merge(new_cell,wall)
                self.cell_stack.append(self.current_cell)
                self.color(self.current_cell,(0,255,255))
                self.current_cell=new_cell
                self.nv+=1
            else:
                self.color(self.current_cell,(255,255,255))
                break
        
            cv2.imshow('Image',self.image)
            if cv2.waitKey(1) & 0xFF==ord('q'):
                cv2.destroyAllWindows()
                return
            if cv2.waitKey(1) & 0xFF==ord('a'):
                cv2.destroyAllWindows()
                cv2.imwrite('maze'+str(random.randint(10**3,10**4))+'.png',self.image)
                image_file_name='maze'+str(random.randint(10**3,10**4))+'.png'
                cv2.imwrite(image_file_name,self.image)
                print("Saved as ",image_file_name)
                
        cv2.imshow("Image", self.image)
        if cv2.waitKey(0) & 0xFF==ord('a'):
            cv2.destroyAllWindows()
            image_file_name='maze'+str(random.randint(10**3,10**4))+'.png'
            cv2.imwrite(image_file_name,self.image)
            print("Saved as ",image_file_name)
            



#cv2.imwrite('maze'+str(maze.nx)+'x'+str(maze.ny)+'('+str(maze.cell_width)+')'+str(random.randint(10**3,10**4))+'.png',maze.image)



        
