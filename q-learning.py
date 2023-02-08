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
    #O is index of possible wall to the left.
    #1 is index of possible wall to the Top.
    #2 is index of possible wall to the right.
    #3 is index of possible wall to the bottom.
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
    
    #All the points of the grid/maze are reshape with the following order
    #  0 | 4 | 8  | 12
    #  1 | 5 | 9  | 13
    #  2 | 6 | 10 | 14
    #  3 | 7 | 11 | 15
    #we process Adjacency matrix: our matrix is symetrical ( non-oriented graph )                
    for i in range (0,len(grid_barrier)):
        for j in range (0,len(grid_barrier[0])):
             for k in range (0,len(grid_barrier[0][0])):
                
                if  ( (grid_barrier[i][j][0] == 0) & ( 4 * (i) + j -4 > 0 ) & (abs( 4* i + j - (4 * (i) + j -4) ) < 6 ) & ( i > 0) ) :
                    adjacence[4* i + j] [ 4 * (i) + j -4] = 1 # these 2 case are linked
                    adjacence[ 4 * (i) + j -4][4* i + j]  = 1 # these 2 case are linked
                
                if ( (grid_barrier[i][j][1] == 0) &  ( 4 * (i) + j -1 > 0 ) & (abs( 4* i + j - ( 4 * i-1 + j  )) < 6 ) & ( j > 0) ): 
                    adjacence[4* i + j] [ 4 * (i) + j -1 ] = 1 # these 2 case are linked
                    adjacence[ 4 * i-1  + j ][4* i + j]  = 1 # these 2 case are linked
                
                if ( (grid_barrier[i][j][2] == 0) & ( 4 * (i) + j + 4 < 16 ) & (abs( 4* i + j - ( 4 * (i) + j + 4 ) ) < 6 ) & ( j < 3 )) : 
                    adjacence[4* i + j] [ 4 * (i) + j + 4] = 1 # these 2 case are linked
                    adjacence[ 4 * (i) + j + 4][4* i + j]  = 1 # these 2 case are linked
                
                if ( (grid_barrier[i][j][3] == 0) & ( 4 * i+1 + j < 16 ) & (abs( 4* i + j - ( 4 * (i) + j + 1 ) ) < 6  ) & (i < 3) ): 
                    adjacence[4* i + j] [ 4 * i+1 + j] = 1 # these 2 case are linked
                    adjacence[ 4 *i + j + 1] [4* i + j]  = 1 # these 2 case are linked



                if ( (grid_barrier[i][j][0] == 1) & (grid_barrier[i][j][1] == 1) & ( 4 * i+ j -5 > 0 )  ) : # no line between i and i-1
                    adjacence[4* i + j] [ 4 * i+ j -5] = 0 # these 2 case are not linked
                    adjacence[ 4 * i+ j -5] [4* i + j]  = 0 # these 2 case are not linked
                
                    
                if ( (grid_barrier[i][j][1] == 1) & (grid_barrier[i][j][2] == 1) & ( 4 * i + j + 3 < 16 ) ) : # no line between i and j+1
                    adjacence[4* i + j] [ 4 * i + j + 3] = 0 # these 2 case are not linked
                    adjacence[ 4 * i + j + 3] [4* i + j]  = 0
                
                    

                if ( (grid_barrier[i][j][2] == 1) & (grid_barrier[i][j][3] == 1)  &  ( 4 * i + j + 5 < 16 ) ) : # no line between i and i-1
                    adjacence[4* i + j] [ 4 * i + j + 5] = 0 # these 2 case are not linked
                    adjacence[ 4 * i + j + 5 ][4* i + j]  = 0
                
                    
                if ( (grid_barrier[i][j][3] == 1) & (grid_barrier[i][j][0] == 1) & ( 4 *i + j -3 > 0 )  ) : # no line between i and i-1
                    adjacence[4* i + j] [ 4 *i + j -3 ] = 0 # these 2 case are not linked
                    adjacence[4 *i + j -3 ][4* i + j]  = 0 
                


                #refilter diag 
                 #diag sup right
                    if ( (4 * (i) + j +3 < 16) & (i < 3) & (j > 0) ):
                         if  ( ( (grid_barrier[i+1][j-1][0] == 1) & ( grid_barrier[i+1][j-1][3] == 1  ) ) | ( (grid_barrier[i][j][2] == 1) & ( grid_barrier[i][j][1] == 1  ) )  |  ( (grid_barrier[i][j][1] == 1) & ( grid_barrier[i+1][j][1] == 1  ) )  |  ( (grid_barrier[i][j][2] == 1) & ( grid_barrier[i+1][j-1][2] == 1  ) ) ):
                            adjacence[4* i + j] [ 4 * i + j +3]  = 0 # these 2 case are not linked
                            adjacence[ 4 * i + j +3] [4* i + j]  = 0 # these 2 case are not linked

                 #diag infer right
                    if ( 4 * i + j + 5 < 15  ) & (i < 3) & (j < 3) :
                        if  ( (grid_barrier[i][j][2] == 1) & (grid_barrier[i][j][3] == 1 ) ) | ( (grid_barrier[i][j][3] == 1) & (grid_barrier[i+1][j][3] == 1 ) ) | ( (grid_barrier[i][j][2] == 1) & (grid_barrier[i][j+1][2] == 1 )) | ( (grid_barrier[i+1][j+1][0] == 1) & (grid_barrier[i+1][j+1][1] == 1 ) ) :
                            adjacence[4* i + j] [ 4 * i + j + 5]  = 0 # these 2 case are not linked
                            adjacence[ 4 * i + j +5] [4* i + j]  = 0 # these 2 case are not linked

                 #diag sup left
                    if ( (4 * (i) + j -5)  >  0 )  & (i > 0) & (j > 0) :
                         if  ( (grid_barrier[i][j][0] == 1) & (grid_barrier[i][j][1] == 1) ) | ( (grid_barrier[i-1][j-1][3] == 1) & (grid_barrier[i][j-1][3] == 1) )  | ( (grid_barrier[i][j][0] == 1) & (grid_barrier[i][j-1][0] == 1) ) |  ( (grid_barrier[i-1][j-1][3] == 1) & (grid_barrier[i-1][j-1][2] == 1) )  :
                            adjacence[4* i + j] [ 4 * (i) + j -5]  = 0 # these 2 case are not linked
                            adjacence[ 4 * (i) + j -5] [4* i + j]  = 0 # these 2 case are not linked

                 #diag inf left
                    if ( (4 * (i) + j -3)  >  0  ) & (i > 0) & (j  < 3):
                        if ( (grid_barrier[i][j][0] == 1) & (grid_barrier[i][j][3] == 1 ) ) | ( (grid_barrier[i][j][3] == 1) & (grid_barrier[i-1][j +1][3] == 1 ) ) | ( (grid_barrier[i][j][0] == 1) & (grid_barrier[i][j+1][0] == 1 ) ) | ( (grid_barrier[i-1][j+1][0] == 1) & (grid_barrier[i][j][3] == 1 )) | ( (grid_barrier[i][j][0] == 1) & (grid_barrier[i][j][3] == 1 ) ) :
                            adjacence[4* i + j] [ 4 * (i-1) + j +1]  = 0 # these 2 case are not linked
                            adjacence[ 4 * (i-1) + j +1] [4* i + j]  = 0 # these 2 case are not linked
    print("Display grid")            
    print(grid_barrier)
    print("Display Adjacence")
    print(adjacence) 
                        

"""
This function will solve the problem of maze.
The kpi process is number of path which could solve the problem.
So we introduce basically the following "loss" ;
more the grid is difficult : less the number of path to solve the issue is large.
"""
def resolve_maze_process_kpi(start, end, treasure_grid):
    print("Resolve maze and find treasure")
    maze = adjacence 
    puissance = adjacence
    # we process all the paths of different length
    for i in range (2,15):
        maze = maze + adjacence.dot(puissance)
        puissance = adjacence.dot(puissance)
    print(maze)   
    # With a starting point a treasure point and an exit point we process our KPI 'difficulty'
    print("search" , maze[start][treasure_grid])
    print("exit" , maze[treasure][end] )
    if ( (maze[start][treasure] > 0) & (maze[treasure][end] > 0 ) ) :
        print("Loss/difficulty of generated grid" , maze[start][treasure]+maze[treasure][end] )
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
