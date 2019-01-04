# Randomly fills an array of size 10x10 True and False, displayed as 1 and 0,
# and outputs the number chess knights needed to jump from 1s to 1s
# and visit all 1s (they can jump back to locations previously visited).
#
# Written by Xiaowei Zhu Z5102903 COMP9021


from random import seed, randrange
import sys


dim = 10


def display_grid():
    for i in range(dim):
        print('     ', end = '')
        print(' '.join(grid[i][j] and '1' or '0' for j in range(dim)))
    print()




#
#def horse_retrive_1(point):
#    x,y = point
#
#    if (0<= x < 10) and (0<= y < 10):
#
#
#
#        if X[x][y] == 0:
#            return X
#
#
#        else:
#            X[x][y] = 0
#
#
#            A = (x-2,y+1)
#            B = (x-1,y+2)
#            C = (x+1,y+2)
#            D = (x+2,y+1)
#            E = (x+2,y-1)
#            F = (x+1,y-2)
#            G = (x-1,y-2)
#            H = (x-2,y-1)
#
#            horse_steps = [A,B,C,D,E,F,G,H]
#            for step in horse_steps:
#                horse_retrive_1(step)

# coordinate = [(x,y) for x in range(10) for y in range(10) if X[x][y] == 1]




# we define a function to clear a matrix to the situation with all 0
def horse_clear_matrix(X):
    
    
    
    # We define a function that will collect any coordinates the horse can arrive
    # every time we give a start point to this horse
    
    # we can not write a tuple or list style here, we need to use a paramater to relace them
    def horse_retrive_1(point):
        # --- Then we convert it back here
        x,y = point
        
        # Firstly we need to limit the range of our point
        # we need to avoid the 'index out of range'
        if (0<= x < 10) and (0<= y < 10):
            # under this situation we can execute the program below
            
            
            # identify that is this value of this point equal to 0
            # if it is , this could be a exit of the recrusion!!!!
            # every recursived function will end up when the value of coordinate is 0
            if X[x][y] == 0:
                # if this situation is satisfied
                # we can use pass here, because we don't need any return in this recursion
                # we are just using this recursion to change the list X
                pass
        
            #****** when we don't need a return in a recursion or function
            #****** we can use pass the replace the return
            #                return X
            
            
            
            
            # if the value of this point is 1
            # that means the horse can jump out from this point
            # as a normal logic, we have 8 different wany (8 different next points)
            else:
                
                # if it is this situation, we will change the value from 1 to 0
                X[x][y] = 0
                
                # 8 ways, we use the index value to locate them
                A = (x-2,y+1)
                B = (x-1,y+2)
                C = (x+1,y+2)
                D = (x+2,y+1)
                E = (x+2,y-1)
                F = (x+1,y-2)
                G = (x-1,y-2)
                H = (x-2,y-1)
                
                
                # Here we store these 8 points into a list
                #
                horse_steps = [A,B,C,D,E,F,G,H]
                # we can traverse all these 8 coordinates
                # with the function that we define
                # so we will know the situations of these 8 points
                # and it will traverse the deep 8 points until trigger X[x][y]==0
                for step in horse_steps:
                    # execute the defined function
                    horse_retrive_1(step)
    
    

    #  we can traverse all the points that the value is 1
    #  and then these points are stored in a list
    coordinate = [(x,y) for x in range(10) for y in range(10) if X[x][y] == 1]

    ABC = []
    
    # then we use horse_retrived_1 to traverse all these points
    for i in coordinate:
        horse_retrive_1(i)
        
        # every time when we finish the traverse we will get a new list
        coordinate = [(x,y) for x in range(10) for y in range(10) if X[x][y] == 1]
        # some times these new list will be a duplicated list
        # because some points wil be eliminated to 0 at onece
        if coordinate not in ABC:
            
            # we can record the unique list
            # that means how many different horses we need to use to clear this whole matrix
            ABC.append(coordinate)


# at the end the coordinate list will be a empty list
# becausethere is no 1 in this matrix

if coordinate == []:
    # so at this situation, we can return the length of ABC
    # because we record all the unique lists in the list
    # the length is the numbers of horses
    return len(ABC)




try:
    for_seed, n = (int(i) for i in input('Enter two integers: ').split())
    if not n:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
if n > 0:
    grid = [[randrange(n) > 0 for _ in range(dim)] for _ in range(dim)]
else:
    grid = [[randrange(-n) == 0 for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()




nb_of_knights = horse_clear_matrix(grid)



if not nb_of_knights:
    print('No chess knight has explored this board.')
elif nb_of_knights == 1:
    print(f'At least 1 chess knight has explored this board.')
else:
    print(f'At least {nb_of_knights} chess knights have explored this board')

