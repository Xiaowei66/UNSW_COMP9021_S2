# final beta
from copy import deepcopy
import sys
sys.setrecursionlimit(100000)

# area object
class Path_area:
    def __init__(self,point):
        self.point = point
        x,y = self.point
        
        self.upper = True
        self.left  = True
        self.right = True
        self.down  = True
        
        #directions = {'u':(x-1, y), 'd':(x+1, y), 'l':(x, y-1), 'r':(x, y+1)}
        #path_area_value
        
        if x-1 >= 0:
            if path_area_value[x-1][y] < 2:
                self.upper = False
        if x+1 < path_height_x:
            if path_area_value[x+1][y] < 2:
                self.down = False
        if y-1 >= 0:
            if path_area_value[x][y-1] < 2:
                self.left = False
        if y+1 < path_width_y:
            if path_area_value[x][y+1] < 2:
                self.right = False

# define a signle point boject
class Single_Pillor:
    def __init__(self,point):
        self.point = point
        x,y = self.point
        
        self.upper = False
        self.left  = False
        self.right = False
        self.down  = False
        global list_for_single_pillor
        directions = {'u':(x-1, y), 'd':(x+1, y), 'l':(x, y-1), 'r':(x, y+1)}
        # here we need a copy list
        if x-1 >= 0:
            if list_for_single_pillor[directions['u'][0]][directions['u'][1]] in [2,3]:
                self.upper = True
        if y-1 >= 0:
            if list_for_single_pillor[directions['l'][0]][directions['l'][1]] in [1,3]:
                self.left  = True
        if list_for_single_pillor[x][y] == 1:
            self.right = True
        if list_for_single_pillor[x][y] == 2:
            self.down  = True
        if list_for_single_pillor[x][y] == 3:
            self.right = True
            self.down  = True

        self.arrived = False
        self.horizontal_print = False
        self.vertical_print = False

# define a signle point boject
class Single_Point:
    def __init__(self,point):
        self.point = point
        x,y = self.point
        
        self.upper = False
        self.left  = False
        self.right = False
        self.down  = False
        
        directions = {'u':(x-1, y), 'd':(x+1, y), 'l':(x, y-1), 'r':(x, y+1)}
        # here we need a copy list
        if x-1 >=0:
            
            if list_for_single_point[directions['u'][0]][directions['u'][1]] in [2,3]:
                self.upper = True
        if y-1 >=0:
            if list_for_single_point[directions['l'][0]][directions['l'][1]] in [1,3]:
                self.left  = True
        if list_for_single_point[x][y] == 1:
            self.right = True
        if list_for_single_point[x][y] == 2:
            self.down  = True
        if list_for_single_point[x][y] == 3:
            self.right = True
            self.down  = True


# area object
class Single_area:
    def __init__(self,point):
        self.point = point
        x,y = self.point
        
        self.upper = True
        self.left  = True
        self.right = True
        self.down  = True
        
        self.arrived = False
        self.row_arrived = False
        self.column_arrived = False
        
        if list_for_area[x][y] == 1:
            self.upper = False
        if list_for_area[x][y] == 2:
            self.left = False
        if list_for_area[x][y] == 3:
            self.upper = False
            self.left = False
        if list_for_area[x][y+1] in [2,3]:
            self.right = False
        if list_for_area[x+1][y] in [1,3]:
            self.down = False

class MazeError(Exception):
    def __init__(self,error_message):
        self.error_message = error_message




class Maze(MazeError):
    
    def __init__(self,file_name):
        self.file_name = file_name
        
        
        filename = self.file_name
        # open the file
        with open(filename) as ready_maze_file:
            readed_maze_file = ready_maze_file.readlines()
        
        # eliminate ' ' and '\n'
        
        #print(readed_maze_file)
        second_maze_file = [[int(each) for each in line if each != '\n' and each != ' ']\
                            for line in readed_maze_file if line != '\n']
                            first_maze_file = [each_row for each_row in second_maze_file if each_row != []]
                            
                            list_maze_file = first_maze_file
                            
                            #print(list_maze_file)
                            # identify the legth of every line
                            stand_length = len(list_maze_file[0])
                            for each in list_maze_file:
                                if len(each) != stand_length:
                                    raise MazeError('Incorrect input.')

# identify the least ,most Xdim
if stand_length < 2 or stand_length > 31:
    raise MazeError('Incorrect input.')
        
        # identify the least,most Ydim
        if len(list_maze_file) < 2 or len(list_maze_file) > 41:
            raise MazeError('Incorrect input.')

    # identify the list that only contain 0,1,2,3
    for line in list_maze_file:
        for each in line:
            if each not in [0,1,2,3]:
                raise MazeError('Incorrect input.')

# identify the last digit of every line
column_maze_list = list(zip(*list_maze_file))
#print(column_maze_list)
for each in column_maze_list[-1]:
    if each not in [0,2]:
        raise MazeError('Input does not represent a maze.')
        
        # identify the last line
        for each in list_maze_file[-1]:
            if each not in [0,1]:
                raise MazeError('Input does not represent a maze.')

    self.column_maze_list = column_maze_list
        self.maze_list = first_maze_file
        #print(self.maze_list)
        self.point_height_x = len(first_maze_file)
        self.point_width_y = len(first_maze_file[0])
        self.area_height_x = len(first_maze_file) - 1
        self.area_width_y = len(first_maze_file[0]) - 1
        
        
        # display() should execy=ute independently so we need to put these programming in __init__
        ########################################################################################
        
        # 1.find the gates the way without build areas object
        # retrieve the first row
        first_row_gate = 0
        # we don't need the last digit of the first line
        first_row_list = self.maze_list[0][:-1]
        for i in first_row_list:
            if i in [0,2]:
                first_row_gate = first_row_gate + 1

# retrieve the last row
last_row_gate = 0
    # we don't need the last digit of the first line
    last_row_list = self.maze_list[-1][:-1]
    for i in last_row_list:
        if i in [0,2]:
            last_row_gate = last_row_gate + 1
        
        
        # retrieve the first column
        first_column_gate = 0
        # we don,t need the last digit of the first row
        first_column_list = self.column_maze_list[0][:-1]
        for i in first_column_list:
            if i in [0,1]:
                first_column_gate = first_column_gate + 1
        
        # retrieve the first column
        last_column_gate = 0
        # we don,t need the last digit of the first row
        last_column_list = self.column_maze_list[-1][:-1]
        for i in last_column_list:
            if i in [0,1]:
                last_column_gate = last_column_gate + 1
        # add all the gates
        global total_gate_number
        total_gate_number = first_row_gate + last_row_gate +\
            first_column_gate + last_column_gate
        
        #print(total_gate_number)
        
        ########################################################################################
        # point out the single point, 4 direction are None
        global list_for_single_pillor
        list_for_single_pillor = deepcopy(self.maze_list)
        
        point_height_x = self.point_height_x
        point_width_y  = self.point_width_y
        
        global single_pillor_point
        single_pillor_point =\
        [(x,y) for x in range(0,point_height_x) for y in range(0,point_width_y) \
         if sum([Single_Pillor((x,y)).upper,Single_Pillor((x,y)).down, Single_Pillor((x,y)).left,Single_Pillor((x,y)).right])==0 ]
         #print('*****single_pillor_point*****')
         
         #print(single_pillor_point)
         ########################################################################################
         
         # copy the list for single point
         
         # ???
         global list_for_single_point
         list_for_single_point = deepcopy(self.maze_list)
         #print(self.maze_list)
         # in this function list_for_single_point in Single_point() turn to 0
         def rec_four_directions_point(inital_point):
             
             x,y = inital_point
                 directions = {'u':(x-1, y), 'd':(x+1, y), 'l':(x, y-1), 'r':(x, y+1)}
             
                 point_directions_boolean = Single_Point(inital_point)

                 if point_directions_boolean.upper:
                     list_for_single_point[x][y] = 0
                     rec_four_directions_point(directions['u'])
                         
                         if point_directions_boolean.down:
                             list_for_single_point[x][y] = 0
                             rec_four_directions_point(directions['d'])
                                 
                                 if point_directions_boolean.left:
                                     list_for_single_point[x][y] = 0
                                     rec_four_directions_point(directions['l'])
                                         
                                         if point_directions_boolean.right:
                                             list_for_single_point[x][y] = 0
                                             rec_four_directions_point(directions['r'])
                                                 
                                                 return


point_height_x = self.point_height_x
    point_width_y  = self.point_width_y
        
        def find_point_notequal_1():
            for x in range(0,point_height_x):
                for y in range(0,point_width_y):
                    if list_for_single_point[x][y] != 0:
                        return (x,y)
        global connected_wall_count
        connected_wall_count = 0
        while any([i for row in list_for_single_point for i in row]):
            rec_four_directions_point(find_point_notequal_1())
            connected_wall_count += 1

    #print(connected_wall_count)
    #print(self.maze_list)
    ########################################################################################

    # count the accessible areas
    global list_for_area
        list_for_area = deepcopy(self.maze_list)
        #print(list_for_area)
        
        # store the Single_area() in a new list for recall
        # this new list height-1 width-1 due to the are
        area_height_x = self.area_height_x
        area_width_y  = self.area_width_y
        
        stored_single_area_list = []
        for x in range(0,area_height_x):
            area_row = []
            for y in range(0,area_width_y):
                area_row.append(Single_area((x,y)))
            stored_single_area_list.append(area_row)
########################################################################################
# list the area_point of all gates

#gates in the first row
gates_first_row = []
first_row_point = [(0,y) for y in range(0,area_width_y)]
#first_row_point
for i in first_row_point:
    if Single_area(i).upper:
        gates_first_row.append(i)
        
        gates_last_row = []
        last_row_point = [(area_height_x - 1,y) for y in range(0,area_width_y)]
        for i in last_row_point:
            if Single_area(i).down:
                gates_last_row.append(i)
        
        gates_first_column = []
        first_column_point = [(x,0) for x in range(0,area_height_x)]
        for i in first_column_point:
            if Single_area(i).left:
                gates_first_column.append(i)

                    gates_last_column = []
                    last_column_point = [(x,area_width_y - 1) for x in range(0,area_height_x)]
                    for i in last_column_point:
if Single_area(i).right:
    gates_last_column.append(i)
        
        valued_gates = gates_first_row + gates_last_row + gates_first_column + gates_last_column
        
        #print(valued_gates)
        
        ########################################################################################
        #
        area_list_for_inac = [[1 for _ in range(0,area_width_y)]\
                              for _ in range(0,area_height_x)]
            
                              def retrieve_accessible_path(entry_gate):
                                  x,y = entry_gate
                                      if 0<= x <area_height_x and 0<= y < area_width_y:
                                          directions = {'u':(x-1, y), 'd':(x+1, y), 'l':(x, y-1), 'r':(x, y+1)}
                                          area_direction_boolean = Single_area((x,y))
                                      
                                          if area_list_for_inac[x][y]:
                                              area_list_for_inac[x][y] = 0
                                          
                                              if area_direction_boolean.upper:
                                                  retrieve_accessible_path(directions['u'])
                                                      if area_direction_boolean.down:
                                                          retrieve_accessible_path(directions['d'])
                                                              if area_direction_boolean.left:
                                                                  retrieve_accessible_path(directions['l'])
                                                                      if area_direction_boolean.right:
                                                                          retrieve_accessible_path(directions['r'])
                                      
                                                                      retrieve_valued_gates = deepcopy(valued_gates)
                                                                          
                                                                          global accessible_areas_number
                                                                          accessible_areas_number = 0
# retrieve all the accessible areas
while retrieve_valued_gates:
    retrieve_accessible_path(retrieve_valued_gates[0])
    retrieve_valued_gates = [(x,y) for (x,y) in retrieve_valued_gates if area_list_for_inac[x][y]]
    accessible_areas_number += 1
        
        #print(accessible_areas_number)
        global inaccessible_areas_number
        remained_areas_with_1 = [area for row in area_list_for_inac for area in row ]
        inaccessible_areas_number = sum(remained_areas_with_1)
        #print(inaccessible_areas_number)
        
        ########################################################################################
        # record all the inaccessible areas coordinate
        #print(area_height_x,area_width_y)
        inac_area_coordinate =\
        [(x,y) for x in range(0,area_height_x) for y in range(0,area_width_y) if area_list_for_inac[x][y]== 1 ]
        #print(inac_area_coordinate)
        ########################################################################################
        # create a list that store the sumption of the valued directions of all areas
        # the sum of inaccessible areas is 0
        area_valued_directions_sum_list = []
        for x in range(0,area_height_x):
            row = []
            for y in range(0,area_width_y):
                if (x,y) not in inac_area_coordinate:
                    B = Single_area((x,y))
                    Boolean_value = [B.upper, B.down, B.left, B.right]
                    row.append(sum(Boolean_value))
                else:
                    row.append(0)
            area_valued_directions_sum_list.append(row)
        
        #print(area_valued_directions_sum_list)
        
        ########################################################################################
        # eliminate all 1 in area_valued_directions_sum_list
        global D_sum
        D_sum = deepcopy(area_valued_directions_sum_list)
        
        def still_1_exists(D_sum):
            if 1 in [each for row in D_sum for each in row]:
                return False
            return True
        
        while not still_1_exists(D_sum):
            for x in range(0,area_height_x):
                for y in range(0,area_width_y):
                    if D_sum[x][y] == 1:
                        D_sum[x][y] = -1
                        
                        directions = {'u':(x-1, y), 'd':(x+1, y), 'l':(x, y-1), 'r':(x, y+1)}
                        
                        
                        A = Single_area((x,y))
                        if 0 <= (x-1) <area_height_x and 0<= y <area_width_y:
                            if A.upper:
                                if directions['u'] not in inac_area_coordinate:
                                    D_sum[directions['u'][0]][directions['u'][1]] =\
                                    D_sum[directions['u'][0]][directions['u'][1]] - 1
                        if 0 <= (x+1) <area_height_x and 0<= y <area_width_y:
                            if A.down:
                                if directions['d'] not in inac_area_coordinate:
                                    D_sum[directions['d'][0]][directions['d'][1]] =\
                                    D_sum[directions['d'][0]][directions['d'][1]] - 1
                        if 0 <= x <area_height_x and 0<= (y-1) <area_width_y:
                            if A.left:
                                if directions['l'] not in inac_area_coordinate:
                                    D_sum[directions['l'][0]][directions['l'][1]] =\
                                    D_sum[directions['l'][0]][directions['l'][1]] - 1
                if 0 <= x <area_height_x and 0<= (y+1) <area_width_y:
                    
                    if A.right:
                        if directions['r'] not in inac_area_coordinate:
                            D_sum[directions['r'][0]][directions['r'][1]] =\
                            D_sum[directions['r'][0]][directions['r'][1]] - 1
    
        #print(D_sum)
        ########################################################################################
        #  retrieve all the negative value in D_sum
        #  the times will be the number of cul-de-sacs
        
        def retrieve_cul_de_sacs(start_point):
            x,y = start_point
            if 0 <= x <area_height_x and 0<= y <area_width_y:
                if D_sum[x][y] <= -1:
                    if not stored_single_area_list[x][y].arrived:
                        stored_single_area_list[x][y].arrived = True
                        
                        directions = {'u':(x-1, y), 'd':(x+1, y), 'l':(x, y-1), 'r':(x, y+1)}
                        if stored_single_area_list[x][y].upper:
                            retrieve_cul_de_sacs(directions['u'])
                        
                        if stored_single_area_list[x][y].down:
                            retrieve_cul_de_sacs(directions['d'])
                    
                        if stored_single_area_list[x][y].left:
                            retrieve_cul_de_sacs(directions['l'])
                        
                        if stored_single_area_list[x][y].right:
                            retrieve_cul_de_sacs(directions['r'])
        ########################################################################################
        # record the cul_de_sacs point coordinator
        global cul_de_sacs_coordinator
        cul_de_sacs_coordinator =\
        [(x,y) for x in range(0,area_height_x) for y in range(0,area_width_y) if D_sum[x][y] <= -1 ]
        ########################################################################################

        # bulid a list contain
        for_retrieve_cul=\
        [(x,y) for x in range(0,area_height_x) for y in range(0,area_width_y)\
         if D_sum[x][y] <= -1 and stored_single_area_list[x][y].arrived == False]
         #print(for_retrieve_cul)

         global cul_de_sacs_number
         cul_de_sacs_number = 0
         while for_retrieve_cul:
             #print(for_retrieve_cul)
             retrieve_cul_de_sacs(for_retrieve_cul[0])
             for_retrieve_cul = [(x,y) for x in range(0,area_height_x) for y in range(0,area_width_y)\
                                 if D_sum[x][y] <= -1 and stored_single_area_list[x][y].arrived == False]
             cul_de_sacs_number += 1
         #print(for_retrieve_cul)
         
         #print(cul_de_sacs_number)
         #print(cul_de_sacs_coordinator)


         ########################################################################################
         # get the available gate
         # valued_gates
         available_gate_list = [(x,y) for (x,y) in valued_gates if D_sum[x][y] == 2 ]
        #print(available_gate_list)
        # create a function which is used to get the path of all available path
        
        available_path_coordinator = []
        def get_available_path(available_gate):
            x,y = available_gate
            #print(x,y)
            #available_path_coordinator.append((x,y))
            if 0 <= x <area_height_x and 0<= y <area_width_y:
                if D_sum[x][y] >= 2:
                    if not stored_single_area_list[x][y].arrived:
                        stored_single_area_list[x][y].arrived = True
                        
                        directions = {'u':(x-1, y), 'd':(x+1, y), 'l':(x, y-1), 'r':(x, y+1)}
                        # out of index !!!
                        if stored_single_area_list[x][y].upper:
                            get_available_path(directions['u'])
                        
                        if stored_single_area_list[x][y].down:
                            get_available_path(directions['d'])
                    
                        if stored_single_area_list[x][y].left:
                            get_available_path(directions['l'])
                        
                        if stored_single_area_list[x][y].right:
                            get_available_path(directions['r'])
                            
                available_path_coordinator.append((x,y))
##########################################################################################
# create a function to check the gates in one list over2
#print('***')
#print(available_gate_list)
def check_gate_over2(available_path_coordinator):
    #available_gate_list
    intersect =\
        [each for each in available_path_coordinator if each in available_gate_list]
            if len(intersect) <= 2:
                return True
        return False
        ########################################################################################
        # retrieve all available gates
        final_paths = []
        for (x,y) in available_gate_list:
            get_available_path((x,y))
            #print(available_path_coordinator)
            # eliminate the unsatisfied gates_list [] and gates over 2
            if available_path_coordinator and check_gate_over2(available_path_coordinator):
                final_paths.append(available_path_coordinator)
            available_path_coordinator = []
        
        #entry_exit_paths_number = len(final_paths)
        #global entry_exit_paths
        #entry_exit_paths = final_paths
        #print(entry_exit_paths_number)
        #print('***')
        #print(entry_exit_paths)
        #print(available_path_coordinator)
        
        #print(list_for_single_point)
        #print(stored_single_area_list[1][5].arrived)
        #print(D_sum[1][5])
        
        ########################################################################################
        # check the path that doesn't contain an area with 3 directions
        # store the original direction in this list
        global path_area_value
        path_area_value = deepcopy(D_sum)
        
        global path_height_x
        global path_width_y
        path_height_x = self.area_height_x
        path_width_y  = self.area_width_y
        
        path_area_direction = []
        for x in range(0,path_height_x):
            path_row = []
            for y in range(0,path_width_y):
                path_row.append(Single_area((x,y)))
            path_area_direction.append(path_row)

# eliminate the unavailable direction

individual_entry_exit_paths = [each for row in final_paths for each in row]
for (x,y) in individual_entry_exit_paths:
    if path_area_direction[x][y].upper and Path_area((x,y)).upper:
        path_area_direction[x][y].upper = True
            else:
                path_area_direction[x][y].upper = False
    
        if path_area_direction[x][y].down and Path_area((x,y)).down:
            path_area_direction[x][y].down = True
            else:
                path_area_direction[x][y].down = False
            
            if path_area_direction[x][y].left and Path_area((x,y)).left:
                path_area_direction[x][y].left = True
        else:
            path_area_direction[x][y].left = False
            
            if path_area_direction[x][y].right and Path_area((x,y)).right:
                path_area_direction[x][y].right = True
            else:
                path_area_direction[x][y].right = False

# create a function to check the paths contain s area has 3 directions

def ckeck_3_directions(path):
    for (x,y) in path:
        D = [path_area_direction[x][y].upper, path_area_direction[x][y].down,\
             path_area_direction[x][y].left , path_area_direction[x][y].right]
             #print (sum(D),(x,y))
             if sum(D) != 2:
                 return False
                     return True
                 
                 #print(D_sum)
                 
                 
                 # check the final_paths
                 global entry_exit_paths
                     entry_exit_paths = []

for path in final_paths:
    if ckeck_3_directions(path):
        entry_exit_paths.append(path)
        #
        
        global entry_exit_paths_number
        entry_exit_paths_number = len(entry_exit_paths)

    #print(entry_exit_paths_number)
    #print('*entry_exit_paths*')
    #print(entry_exit_paths)



    ########################################################################################
    def analyse(self):
        # codeing is in __init__ ,here we just call the print
        
        # print these answer none, a unique, n
        if total_gate_number == 0:
            print('The maze has no gate.')
        elif total_gate_number == 1:
            print('The maze has a single gates.')
        else:
            print(f'The maze has {total_gate_number} gates.')
        
        #print(valued_gates)
        
        if connected_wall_count == 0:
            print('The maze has no wall.')
        elif connected_wall_count == 1:
            print('The maze has walls that are all connected.')
        else:
            print(f'The maze has {connected_wall_count} sets of walls that are all connected.')
        
        
        if inaccessible_areas_number == 0:
            print('The maze has no inaccessible inner point.')
        elif inaccessible_areas_number == 1:
            print('The maze has a unique inaccessible inner point.')
        else:
            print(f'The maze has {inaccessible_areas_number} inaccessible inner points.')
        
        #print(inac_area_coordinate)
        
        if accessible_areas_number == 0:
            print('The maze has no accessible area.')
        elif accessible_areas_number == 1:
            print('The maze has a unique accessible area.')
        else:
            print(f'The maze has {accessible_areas_number} accessible areas.')
        
        
        
        if cul_de_sacs_number == 0:
            print('The maze has no accessible cul-de-sac.')
        elif cul_de_sacs_number == 1:
            print('The maze has accessible cul-de-sacs that are all connected.')
        else:
            print(f'The maze has {cul_de_sacs_number} sets of accessible cul-de-sacs that are all connected.')
        
        #print(cul_de_sacs_coordinator)
        
        if entry_exit_paths_number == 0:
            print('The maze has no entry-exit path with no intersection not to cul-de-sacs.')
        elif entry_exit_paths_number == 1:
            print('The maze has a unique entry-exit path with no intersection not to cul-de-sacs.')
        else:
            print(f'The maze has {entry_exit_paths_number} entry-exit paths with no intersections not to cul-de-sacs.')

    #print(entry_exit_paths)
##########################################################################################

def display(self):
    
    point_height_x = self.point_height_x
        point_width_y  = self.point_width_y
        # build a list to store the Single_Pillor Object
        Single_pillor_list = [[ Single_Pillor((x,y)) for y in range(0,point_width_y)] for x in range(0,point_height_x) ]
        #print(Single_pillor_list)
        write_filename = self.file_name[0:-3] + 'tex'
        
        with open(write_filename,'w') as latex_file:
            
            # print the head
            print('\\documentclass[10pt]{article}\n'
                  '\\usepackage{tikz}\n'
                  '\\usetikzlibrary{shapes.misc}\n'
                  '\\usepackage[margin=0cm]{geometry}\n'
                  '\\pagestyle{empty}\n'
                  '\\tikzstyle{every node}=[cross out, draw, red]\n'
                  '\n'
                  '\\begin{document}\n'
                  '\n'
                  '\\vspace*{\\fill}\n'
                  '\\begin{center}\n'
                  '\\begin{tikzpicture}[x=0.5cm, y=-0.5cm, ultra thick, blue]\n'
                  '% Walls' , file = latex_file
                  )
                
                  
                  # draw the horizontal wall from left to right
                  
                  for x in range(point_height_x):
                      for y in range(point_width_y):
                          if Single_pillor_list[x][y].right:
                              if not Single_pillor_list[x][y].horizontal_print:
                                  Single_pillor_list[x][y].horizontal_print = True
                                  p = y
                                      # p means the y position here
                                      while p < point_width_y - 1:
                                          # out of index
                                          #while Single_pillor_list[x][p].right:
                                          p += 1
                                              Single_pillor_list[x][p].horizontal_print = True
                                              if not Single_pillor_list[x][p].right:
                                                  break
                                                      print('    \\draw ('+str(y)+','+str(x)+') '
                                                            '-- ('+str(p)+','+str(x)+');' , file = latex_file
                                                            )
                  
                  for y in range(point_width_y):
                      for x in range(point_height_x):
                          if Single_pillor_list[x][y].down:
                              if not Single_pillor_list[x][y].vertical_print:
                                  Single_pillor_list[x][y].vertical_print = True
                                  p = x
                                      # p means the y position here
                                      while p < point_height_x - 1:
                                          # out of index !!!
                                          #while Single_pillor_list[p][y].down:
                                          p += 1
                                              Single_pillor_list[p][y].vertical_print = True
                                              if not Single_pillor_list[p][y].down:
                                                  break
                                                      print('    \\draw ('+str(y)+','+str(x)+') '
                                                            '-- ('+str(y)+','+str(p)+');' , file = latex_file
                                                            )
                                                          
                                                          # draw the vertical wall from left to right
                                                          
                                                          # draw the pillars
                                                          print('% Pillars',file = latex_file)
                                                          #sort single_pillor_point
                                                          sort_single_pillor_point = sorted(single_pillor_point)
                                                          for (x,y) in sort_single_pillor_point:
                                                              print('    \\fill[green] ('+str(y)+','+str(x)+')'
                                                                    ' circle(0.2);',file = latex_file
                                                                    
                                                                    )
                                                                  
                                                                  # draw the cul_de_sacs_coordinator
                                                                  print('% Inner points in accessible cul-de-sacs',file = latex_file)
                                                                  # sort cul_de_sacs_coordinator:
                                                                  sort_cul_de_sacs_coordinator = sorted(cul_de_sacs_coordinator)
                                                                  for (x,y) in sort_cul_de_sacs_coordinator:
                                                                      print('    \\node at ('+str(y+0.5)+','+str(x+0.5)+')'
                                                                            ' {};',file = latex_file
                                                                            
                                                                            )
                                                                          
                                                                          # draw the Entry-exit paths without intersections
                                                                          print('% Entry-exit paths without intersections',file = latex_file)
                                                                          
                                                                          # get list of all values 2 means it has two directions
                                                                          global path_area_value
                                                                              path_area_value = deepcopy(D_sum)
                                                                              
                                                                              #global path_height_x
                                                                              #global path_width_y
                                                                              path_height_x = self.area_height_x
                                                                                  path_width_y  = self.area_width_y
                                                                                      
                                                                                      # store the original direction in this list
                                                                                      path_area_list = []
                                                                                      for x in range(0,path_height_x):
                                                                                          path_row = []
                                                                                          for y in range(0,path_width_y):
                                                                                              path_row.append(Single_area((x,y)))
                                                                                                  path_area_list.append(path_row)
                                                                                                      
                                                                                                      # eliminate the unavailable direction
                                                                                                      
                                                                                                      all_entry_exit_paths = [each for row in entry_exit_paths for each in row]
                                                                                                      for (x,y) in all_entry_exit_paths:
                                                                                                          if path_area_list[x][y].upper and Path_area((x,y)).upper:
                                                                                                              path_area_list[x][y].upper = True
                                                                                                                  else:
                                                                                                                      path_area_list[x][y].upper = False
                                                                                                                          
                                                                                                                          if path_area_list[x][y].down and Path_area((x,y)).down:
                                                                                                                              path_area_list[x][y].down = True
                                                                                                                                  else:
                                                                                                                                      path_area_list[x][y].down = False
                                                                                                                                          
                                                                                                                                          if path_area_list[x][y].left and Path_area((x,y)).left:
                                                                                                                                              path_area_list[x][y].left = True
                                                                                                                                                  else:
                                                                                                                                                      path_area_list[x][y].left = False
                                                                                                                                                          
                                                                                                                                                          if path_area_list[x][y].right and Path_area((x,y)).right:
                                                                                                                                                              path_area_list[x][y].right = True
                                                                                                                                                                  else:
                                                                                                                                                                      path_area_list[x][y].right = False
                                                                                                                                                                          
                                                                                                                                                                          
                                                                                                                                                                          # collect the horizontal coordinators
                                                                                                                                                                          horizontal_print = []
                                                                                                                                                                          vertical_print = []
                                                                                                                                                                          for (x,y) in all_entry_exit_paths:
                                                                                                                                                                              if path_area_list[x][y].right == True:
                                                                                                                                                                                  horizontal_print.append((x,y))
                                                                                                                                                                                      if path_area_list[x][y].left == True:
                                                                                                                                                                                          horizontal_print.append((x,y))
                                                                                                                                                                                              
                                                                                                                                                                                              if path_area_list[x][y].upper == True:
                                                                                                                                                                                                  vertical_print.append((x,y))
                                                                                                                                                                                                      if path_area_list[x][y].down == True:
                                                                                                                                                                                                          vertical_print.append((x,y))
                                                                                                                                                                                                              #print('********')
                                                                                                                                                                                                              #print(sorted(set(horizontal_print)))
                                                                                                                                                                                                              #print(sorted(set(vertical_print)))
                                                                                                                                                                                                              
                                                                                                                                                                                                              set_horizontal = sorted(set(horizontal_print))
                                                                                                                                                                                                              set_vertical = sorted(set(vertical_print))
                                                                                                                                                                                                              
                                                                                                                                                                                                              
                                                                                                                                                                                                              #self.row_arrived = False
                                                                                                                                                                                                              #self.column_arrived = False
                                                                                                                                                                                                              # connected the point in the same row
                                                                                                                                                                                                              all_row = []
                                                                                                                                                                                                              for (x,y) in set_horizontal:
                                                                                                                                                                                                                  connected_row = []
                                                                                                                                                                                                                  if path_area_list[x][y].right == True and path_area_list[x][y].row_arrived == False:
                                                                                                                                                                                                                      path_area_list[x][y].row_arrived = True
                                                                                                                                                                                                                      n = y
                                                                                                                                                                                                                          while n < path_width_y - 1:
                                                                                                                                                                                                                              n = n + 1
                                                                                                                                                                                                                                  path_area_list[x][n].row_arrived = True
                                                                                                                                                                                                                                  if path_area_list[x][n].right == False:
                                                                                                                                                                                                                                      break
                                                                                                                                                                                                                                          if y != n:
                                                                                                                                                                                                                                              connected_row.append(((x,y),(x,n)))
                                                                                                                                                                                                                                                  else:
                                                                                                                                                                                                                                                      connected_row.append((x,y))
                                                                                                                                                                                                                                                          elif path_area_list[x][y].right == False and path_area_list[x][y].row_arrived == False:
                                                                                                                                                                                                                                                              connected_row.append((x,y))
                                                                                                                                                                                                                                                                  all_row.append(connected_row)
                                                                                                                                                                                                                                                                      #print(all_row)
                                                                                                                                                                                                                                                                      
                                                                                                                                                                                                                                                                      all_column = []
                                                                                                                                                                                                                                                                      for (x,y) in set_vertical:
                                                                                                                                                                                                                                                                          connected_column = []
                                                                                                                                                                                                                                                                          if path_area_list[x][y].down == True and path_area_list[x][y].column_arrived == False:
                                                                                                                                                                                                                                                                              path_area_list[x][y].column_arrived = True
                                                                                                                                                                                                                                                                              n = x
                                                                                                                                                                                                                                                                                  while n < path_height_x - 1:
                                                                                                                                                                                                                                                                                      n = n + 1
                                                                                                                                                                                                                                                                                          path_area_list[n][y].column_arrived = True
                                                                                                                                                                                                                                                                                          if path_area_list[n][y].down == False:
                                                                                                                                                                                                                                                                                              break
                                                                                                                                                                                                                                                                                                  if x != n:
                                                                                                                                                                                                                                                                                                      connected_column.append(((x,y),(n,y)))
                                                                                                                                                                                                                                                                                                          else:
                                                                                                                                                                                                                                                                                                              connected_column.append((x,y))
                                                                                                                                                                                                                                                                                                                  elif path_area_list[x][y].down == False and path_area_list[x][y].column_arrived == False:
                                                                                                                                                                                                                                                                                                                      connected_column.append((x,y))
                                                                                                                                                                                                                                                                                                                          all_column.append(connected_column)
                                                                                                                                                                                                                                                                                                                              #print(all_column)
                                                                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                                                                              # eliminate the [] in these list
                                                                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                                                                              final_all_row = [each for a_list in all_row if a_list for each in a_list]
                                                                                                                                                                                                                                                                                                                              final_all_column = [each for a_list in all_column if a_list for each in a_list]
                                                                                                                                                                                                                                                                                                                              #print(final_all_row)
                                                                                                                                                                                                                                                                                                                              #print(final_all_column)
                                                                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                                                                              # summary the connected line
                                                                                                                                                                                                                                                                                                                              connected_final_all_row = [each for each in final_all_row if type(each[0]) is tuple]
                                                                                                                                                                                                                                                                                                                              connected_final_all_column = [each for each in final_all_column if type(each[0]) is tuple]
                                                                                                                                                                                                                                                                                                                              #summary the dependent line
                                                                                                                                                                                                                                                                                                                              dependent_final_all_row = [each for each in final_all_row if type(each[0]) is int]
                                                                                                                                                                                                                                                                                                                              dependent_final_all_column = [each for each in final_all_column if type(each[0]) is int]
                                                                                                                                                                                                                                                                                                                              #print('connected')
                                                                                                                                                                                                                                                                                                                              #print(path_area_list[0][5].down)
                                                                                                                                                                                                                                                                                                                              #print(path_area_list[0][5].upper)
                                                                                                                                                                                                                                                                                                                              #print(path_area_list[0][5].right)
                                                                                                                                                                                                                                                                                                                              #print(path_area_list[0][5].left)
                                                                                                                                                                                                                                                                                                                              #print(connected_final_all_row)
                                                                                                                                                                                                                                                                                                                              #print(connected_final_all_column)
                                                                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                                                                              #print('dependent')
                                                                                                                                                                                                                                                                                                                              #print(dependent_final_all_row)
                                                                                                                                                                                                                                                                                                                              #print(dependent_final_all_column)
                                                                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                                                                              # out put the print points
                                                                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                                                                              d_horizontal_print = []
                                                                                                                                                                                                                                                                                                                              d_vertical_print = []
                                                                                                                                                                                                                                                                                                                              for (x,y) in dependent_final_all_row:
                                                                                                                                                                                                                                                                                                                                  if path_area_list[x][y].right == True and path_area_list[x][y].left == False:
                                                                                                                                                                                                                                                                                                                                      d_horizontal_print.append(((x+0.5,y+0.5),(x+0.5,y+1.5)))
                                                                                                                                                                                                                                                                                                                                          if path_area_list[x][y].left == True and path_area_list[x][y].right == False:
                                                                                                                                                                                                                                                                                                                                              d_horizontal_print.append(((x+0.5,y-0.5),(x+0.5,y+0.5)))
                                                                                                                                                                                                                                                                                                                                                  if path_area_list[x][y].left == True and path_area_list[x][y].right == True:
                                                                                                                                                                                                                                                                                                                                                      d_horizontal_print.append(((x+0.5,y-0.5),(x+0.5,y+1.5)))
                                                                                                                                                                                                                                                                                                                                                          for (x,y) in dependent_final_all_column:
                                                                                                                                                                                                                                                                                                                                                              if path_area_list[x][y].upper == True and path_area_list[x][y].down == False:
                                                                                                                                                                                                                                                                                                                                                                  d_vertical_print.append(((x-0.5,y+0.5),(x+0.5,y+0.5)))
                                                                                                                                                                                                                                                                                                                                                                      if path_area_list[x][y].down == True and path_area_list[x][y].upper == False:
                                                                                                                                                                                                                                                                                                                                                                          d_vertical_print.append(((x+0.5,y+0.5),(x+1.5,y+0.5)))
                                                                                                                                                                                                                                                                                                                                                                              if path_area_list[x][y].down == True and path_area_list[x][y].upper == True:
                                                                                                                                                                                                                                                                                                                                                                                  d_vertical_print.append(((x-0.5,y+0.5),(x+1.5,y+0.5)))
                                                                                                                                                                                                                                                                                                                                                                                      
                                                                                                                                                                                                                                                                                                                                                                                      c_horizontal_print = []
                                                                                                                                                                                                                                                                                                                                                                                      c_vertical_print = []
                                                                                                                                                                                                                                                                                                                                                                                      for ((x1,y1),(x2,y2)) in connected_final_all_row:
                                                                                                                                                                                                                                                                                                                                                                                          if path_area_list[x1][y1].left == True and path_area_list[x2][y2].right == True:
                                                                                                                                                                                                                                                                                                                                                                                              c_horizontal_print.append(((x1+0.5,y1-0.5),(x2+0.5,y2+1.5)))
                                                                                                                                                                                                                                                                                                                                                                                                  if path_area_list[x1][y1].left == True and path_area_list[x2][y2].right == False:
                                                                                                                                                                                                                                                                                                                                                                                                      c_horizontal_print.append(((x1+0.5,y1-0.5),(x2+0.5,y2+0.5)))
                                                                                                                                                                                                                                                                                                                                                                                                          if path_area_list[x1][y1].left == False and path_area_list[x2][y2].right == True:
                                                                                                                                                                                                                                                                                                                                                                                                              c_horizontal_print.append(((x1+0.5,y1+0.5),(x2+0.5,y2+1.5)))
                                                                                                                                                                                                                                                                                                                                                                                                                  if path_area_list[x1][y1].left == False and path_area_list[x2][y2].right == False:
                                                                                                                                                                                                                                                                                                                                                                                                                      c_horizontal_print.append(((x1+0.5,y1+0.5),(x2+0.5,y2+0.5)))
                                                                                                                                                                                                                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                                                                                                                                                                                          for ((x1,y1),(x2,y2)) in connected_final_all_column:
                                                                                                                                                                                                                                                                                                                                                                                                                              if path_area_list[x1][y1].upper == True and path_area_list[x2][y2].down == True:
                                                                                                                                                                                                                                                                                                                                                                                                                                  c_vertical_print.append(((x1-0.5,y1+0.5),(x2+1.5,y2+0.5)))
                                                                                                                                                                                                                                                                                                                                                                                                                                      if path_area_list[x1][y1].upper == True and path_area_list[x2][y2].down == False:
                                                                                                                                                                                                                                                                                                                                                                                                                                          c_vertical_print.append(((x1-0.5,y1+0.5),(x2+0.5,y2+0.5)))
                                                                                                                                                                                                                                                                                                                                                                                                                                              if path_area_list[x1][y1].upper == False and path_area_list[x2][y2].down == True:
                                                                                                                                                                                                                                                                                                                                                                                                                                                  c_vertical_print.append(((x1+0.5,y1+0.5),(x2+1.5,y2+0.5)))
                                                                                                                                                                                                                                                                                                                                                                                                                                                      if path_area_list[x1][y1].upper == False and path_area_list[x2][y2].down == False:
                                                                                                                                                                                                                                                                                                                                                                                                                                                          c_vertical_print.append(((x1+0.5,y1+0.5),(x2+0.5,y2+0.5)))
                                                                                                                                                                                                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                                                                                                                                                                                                              #print('LINE')
                                                                                                                                                                                                                                                                                                                                                                                                                                                              output_row = d_horizontal_print+c_horizontal_print
                                                                                                                                                                                                                                                                                                                                                                                                                                                                  output_column = d_vertical_print+c_vertical_print
                                                                                                                                                                                                                                                                                                                                                                                                                                                                      #print(d_horizontal_print+c_horizontal_print)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                      #print(d_vertical_print+c_vertical_print)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
                                                                                                                                                                                                                                                                                                                                                                                                                                                                      sort_output_row =\
                                                                                                                                                                                                                                                                                                                                                                                                                                                                          sorted(output_row,key = lambda x:(x[0][0],x[0][1]))
                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
                                                                                                                                                                                                                                                                                                                                                                                                                                                                          sort_output_column=\
                                                                                                                                                                                                                                                                                                                                                                                                                                                                              sorted(output_column, key = lambda x:(x[0][1],x[0][0]))
                                                                                                                                                                                                                                                                                                                                                                                                                                                                              #print('SORTED_LINE')
                                                                                                                                                                                                                                                                                                                                                                                                                                                                              #print(sort_output_row)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                              #print(sort_output_column)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                                                                                                                                                                                                                              # output
                                                                                                                                                                                                                                                                                                                                                                                                                                                                              for (a,b) in sort_output_row:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  print('    \\draw[dashed, yellow] ('+str(a[1])+','+str(a[0])+') '
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        '-- ('+str(b[1])+','+str(b[0])+');' , file = latex_file
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        )
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      for (a,b) in sort_output_column:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          print('    \\draw[dashed, yellow] ('+str(a[1])+','+str(a[0])+') '
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                '-- ('+str(b[1])+','+str(b[0])+');' , file = latex_file
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                )
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              # collect all the point that have only two directions
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              # 2 directions ! the number in the martix is 2
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              # be inclluded in entry_exit_paths list
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              # buld a object with available directions, eliminate the direction that have X
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              # define a function to eliminate (1,2) == (2,1)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              # the end
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              print('\\end{tikzpicture}\n'
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    '\\end{center}\n'
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    '\\vspace*{\\fill}\n'
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    '\n'
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    '\\end{document}'
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    ,file = latex_file
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    )


########################################################################################

















