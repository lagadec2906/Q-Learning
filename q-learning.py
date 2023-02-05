import numpy as np
import random

print("We are lloking for a maze!")
adjacence= np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])

"""
This function will generate a random grid 4*4.
It also process an adjacence matrix for the next step of resolution
"""
def generate_grid_and_adjacence():
    grid_barrier = np.array([[[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1]],
                             [[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1]],
                             [[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1]],
                             [[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1]]])

    
    #We construct a random map
    for i in range (0,len(grid_barrier)):
        for j in range (0,len(grid_barrier[0])):
            for k in range (0,len(grid_barrier[0][0])):
                if (grid_barrier[i][j][k] == -1):
                  grid_barrier[i][j][k] = random.randint(0, 1)       # random number between 0 and 1 : generate a barrier
                  # propagation of wall
                  if ( k == 0 ) & ( i > 0 ) :
                    grid_barrier[i-1][j][2] = grid_barrier[i][j][k]
                  if ( k == 1 ) & ( j > 0 ) :
                    grid_barrier[i][j-1][3] = grid_barrier[i][j][k]
                  if ( k == 2 ) & ( i < 3 ) :
                    grid_barrier[i+1][j][0] = grid_barrier[i][j][k]
                  if ( k == 3 ) & ( j < 3 ) :
                    grid_barrier[i][j+1][1] = grid_barrier[i][j][k]
                else :
                  print("nothing")
                  
    #we process adjacensy matrix                
    for i in range (0,len(grid_barrier)):
        for j in range (0,len(grid_barrier[0])):
             for k in range (0,len(grid_barrier[0][0])):
                
                if  ( (grid_barrier[i][j][0] == 0) & ( 4 * (i) + j -4 > 0 ) & (abs( 4* i + j - (4 * (i) + j -4) ) < 6 ) & ( i > 0) ) : # no line between i and i-1
                    adjacence[4* i + j] [ 4 * (i) + j -4] = 1 # these 2 case are possibly linked
                    adjacence[ 4 * (i) + j -4][4* i + j]  = 1 # these 2 case are possibly linked
                
                if ( (grid_barrier[i][j][1] == 0) &  ( 4 * (i) + j -1 > 0 ) & (abs( 4* i + j - ( 4 * i-1 + j  )) < 6 ) & ( j > 0) ): # no line between i and j+1
                    adjacence[4* i + j] [ 4 * (i) + j -1 ] = 1 # these 2 case are possibly linked
                    adjacence[ 4 * i-1  + j ][4* i + j]  = 1 # these 2 case are possibly linked
                
                if ( (grid_barrier[i][j][2] == 0) & ( 4 * (i) + j + 4 < 16 ) & (abs( 4* i + j - ( 4 * (i) + j + 4 ) ) < 6 ) & ( j < 3 )) : # no line between i and i-1
                    adjacence[4* i + j] [ 4 * (i) + j + 4] = 1 # these 2 case are possibly linked
                    adjacence[ 4 * (i) + j + 4][4* i + j]  = 1 # these 2 case are possibly linked
                
                if ( (grid_barrier[i][j][3] == 0) & ( 4 * i+1 + j < 16 ) & (abs( 4* i + j - ( 4 * (i) + j + 1 ) ) < 6  ) & (i < 3) ): # no line between i and i-1
                    adjacence[4* i + j] [ 4 * i+1 + j] = 1 # these 2 case are possibly linked
                    adjacence[ 4 *i + j + 1] [4* i + j]  = 1



                if ( (grid_barrier[i][j][0] == 1) & (grid_barrier[i][j][1] == 1) & ( 4 * i+ j -5 > 0 )  ) : # no line between i and i-1
                    adjacence[4* i + j] [ 4 * i+ j -5] = 0 # these 2 case are possibly linked
                    adjacence[ 4 * i+ j -5] [4* i + j]  = 0 # these 2 case are possibly linked
                
                    
                if ( (grid_barrier[i][j][1] == 1) & (grid_barrier[i][j][2] == 1) & ( 4 * i + j + 3 < 16 ) ) : # no line between i and j+1
                    adjacence[4* i + j] [ 4 * i + j + 3] = 0 # these 2 case are possibly linked
                    adjacence[ 4 * i + j + 3] [4* i + j]  = 0
                
                    

                if ( (grid_barrier[i][j][2] == 1) & (grid_barrier[i][j][3] == 1)  &  ( 4 * i + j + 5 < 16 ) ) : # no line between i and i-1
                    adjacence[4* i + j] [ 4 * i + j + 5] = 0 # these 2 case are possibly linked
                    adjacence[ 4 * i + j + 5 ][4* i + j]  = 0
                
                    
                if ( (grid_barrier[i][j][3] == 1) & (grid_barrier[i][j][0] == 1) & ( 4 *i + j -3 > 0 )  ) : # no line between i and i-1
                    adjacence[4* i + j] [ 4 *i + j -3 ] = 0 # these 2 case are possibly linked
                    adjacence[4 *i + j -3 ][4* i + j]  = 0 
                


                #refilter diag 
                 #diag sup right
                    if ( (4 * (i) + j +3 < 16) & (i < 3) & (j > 0) ):
                         if  ( ( (grid_barrier[i+1][j-1][0] == 1) & ( grid_barrier[i+1][j-1][3] == 1  ) ) | ( (grid_barrier[i][j][2] == 1) & ( grid_barrier[i][j][1] == 1  ) )  |  ( (grid_barrier[i][j][1] == 1) & ( grid_barrier[i+1][j][1] == 1  ) )  |  ( (grid_barrier[i][j][2] == 1) & ( grid_barrier[i+1][j-1][2] == 1  ) ) ):
                            adjacence[4* i + j] [ 4 * i + j +3]  = 0 # these 2 case are possibly linked
                            adjacence[ 4 * i + j +3] [4* i + j]  = 0 # these 2 case are possibly linked

                 #diag infer right
                    if ( 4 * i + j + 5 < 15  ) & (i < 3) & (j < 3) :
                        if  ( (grid_barrier[i][j][2] == 1) & (grid_barrier[i][j][3] == 1 ) ) | ( (grid_barrier[i][j][3] == 1) & (grid_barrier[i+1][j][3] == 1 ) ) | ( (grid_barrier[i][j][2] == 1) & (grid_barrier[i][j+1][2] == 1 )) | ( (grid_barrier[i+1][j+1][0] == 1) & (grid_barrier[i+1][j+1][1] == 1 ) ) :
                            adjacence[4* i + j] [ 4 * i + j + 5]  = 0 # these 2 case are possibly linked
                            adjacence[ 4 * i + j +5] [4* i + j]  = 0 # these 2 case are possibly linked

                 #diag sup left
                    if ( (4 * (i) + j -5)  >  0 )  & (i > 0) & (j > 0) :
                         if  ( (grid_barrier[i][j][0] == 1) & (grid_barrier[i][j][1] == 1) ) | ( (grid_barrier[i-1][j-1][3] == 1) & (grid_barrier[i][j-1][3] == 1) )  | ( (grid_barrier[i][j][0] == 1) & (grid_barrier[i][j-1][0] == 1) ) |  ( (grid_barrier[i-1][j-1][3] == 1) & (grid_barrier[i-1][j-1][2] == 1) )  :
                            adjacence[4* i + j] [ 4 * (i) + j -5]  = 0 # these 2 case are possibly linked
                            adjacence[ 4 * (i) + j -5] [4* i + j]  = 0 # these 2 case are possibly linked

                 #diag inf left
                    if ( (4 * (i) + j -3)  >  0  ) & (i > 0) & (j  < 3):
                        if ( (grid_barrier[i][j][0] == 1) & (grid_barrier[i][j][3] == 1 ) ) | ( (grid_barrier[i][j][3] == 1) & (grid_barrier[i-1][j +1][3] == 1 ) ) | ( (grid_barrier[i][j][0] == 1) & (grid_barrier[i][j+1][0] == 1 ) ) | ( (grid_barrier[i-1][j+1][0] == 1) & (grid_barrier[i][j][3] == 1 )) | ( (grid_barrier[i][j][0] == 1) & (grid_barrier[i][j][3] == 1 ) ) :
                            adjacence[4* i + j] [ 4 * (i-1) + j +1]  = 0 # these 2 case are possibly linked
                            adjacence[ 4 * (i-1) + j +1] [4* i + j]  = 0 # these 2 case are possibly linked
    print("Display grid")            
    print(grid_barrier)
    print("Display Agjacence")
    print(adjacence) 
                        

"""
This function will solve the problem of maze.
The kpi process is number of path which could solve the problem.
So we introduce basically the following "loss" ;
more the grid is difficult : less the number of path to solve the issue is large.
"""
def resolve_maze_process_kpi(start, end, maze_grid):
    print("Resolve maze")
    maze = adjacence + adjacence.dot(adjacence)
    # we process all the paths of different length
    for i in range (2,15):
        puissance = adjacence.dot(adjacence)
        maze = maze + adjacence.dot(puissance)
    print(maze)   
    # With a starting point a maze point and an exit point we process our KPI 'difficulty'
    print("search" , maze[start][maze_grid])
    print("exit" , maze[maze_grid][end] )
    if ( (maze[start][maze_grid] > 0) & (maze[maze_grid][end] > 0 ) ) :
        print("Loss/difficulty of generated grid" , maze[start][maze_grid]+maze[maze_grid][end] )
    else :
        print("Impossible to solve")

"""
Start program
"""
def main():
    generate_grid_and_adjacence()
    resolve_maze_process_kpi(0,10,4)

if __name__ == "__main__":
    main()
