# Xiaowei Zhu Z5102903 COMP9021


# Randomly fills a grid of size 7 x 7 with NE, SE, SW, NW,
# meant to represent North-East, South-East, North-West, South-West,
# respectively, and starting from the cell in the middle of the grid,
# determines, for each of the 4 corners of the grid, the preferred path amongst
# the shortest paths that reach that corner, if any. At a given cell, it is possible to move
# according to any of the 3 directions indicated by the value of the cell;
# e.g., from a cell storing NE, it is possible to move North-East, East, or North.
# At any given point, one prefers to move diagonally, then horizontally,
# and vertically as a last resort.
#
# Written by *** and Eric Martin for COMP9021


import sys
from random import seed, choice
from queue_adt import *

def display_grid():
    for row in grid:
        print('    ', *row)



def find_direction(point):
    p_x, p_y = point
    if 0<= p_x < 7 and 0<= p_y <=7:
        return (grid[p_y][p_x])

def get_path():
    
    Possible_Directions = {'SW':[(1,-1), (0,-1),(1,0)], 'NW':[(-1,-1),(0,-1),(-1,0)],\
        'SE':[(1,1), (0,1), (1,0)], 'NE':[(-1,1), (0,1), (-1,0)]}

    global final_routes
    each_route = []

point_already_visit = []

    all_routes = [[(3,3)]]
    final_routes = []
    
    for each_point in all_routes:
        
        a,b = each_point[-1]
        direction = find_direction((b,a))
        #print(direction)
        for d in Possible_Directions[direction]:
            #print(d)
            x = each_point[-1][0]
            y = each_point[-1][1]
            #            print(x,y)
            add_x,add_y = d
            
            new_x = x + add_x
            new_y = y + add_y
            new_point = (new_x,new_y)
            #print(new_point)
            
            if 0<= new_x < 7 and 0<= new_y < 7 and new_point not in point_already_visit:
                new_route = each_point[::]
                #print(new_route)
                new_route.append(new_point)
                #print(new_route)
                
                if new_point in [(0,0),(0,6),(6,0),(6,6)]:
                    #print(new_route)
                    final_routes.append(new_route)
                    point_already_visit.append(new_point)
                
                else:
                    all_routes.append(new_route)
                    #print(all_routes)
                    point_already_visit.append(new_point)

R_final_routes = [[(b,a) for (a,b) in each] for each in final_routes]

return R_final_routes



def preferred_paths_to_corners():
    
    #    global final_routes
    
    routes_00 = []
    routes_60 = []
    routes_06 = []
    routes_66 = []
    
    for route in get_path():
        
        if route[-1] == (0,0):
            routes_00.append(route)
        if route[-1] == (6,0):
            routes_60.append(route)
        if route[-1] == (0,6):
            routes_06.append(route)
        if route[-1] == (6,6):
            routes_66.append(route)

paths = {}
    
    if routes_00:
        paths[(0,0)]= min(routes_00)
    if routes_60:
        paths[(6,0)]= min(routes_60)
if routes_06:
    paths[(0,6)]= min(routes_06)
    if routes_66:
        paths[(6,6)]= min(routes_66)

    return paths


try:
    seed_arg = int(input('Enter an integer: '))
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(seed_arg)
size = 3
dim = 2 * size + 1
grid = [[0] * dim for _ in range(dim)]
directions = 'NE', 'SE', 'SW', 'NW'

grid = [[choice(directions) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()

corners = (0, 0), (dim - 1, 0), (dim - 1, dim - 1), (0, dim - 1)
paths = preferred_paths_to_corners()
if not paths:
    print('There is no path to any corner')
    sys.exit()
for corner in corners:
    if corner not in paths:
        print(f'There is no path to {corner}')
    else:
        print(f'The preferred path to {corner} is:')
        print('  ', paths[corner])
