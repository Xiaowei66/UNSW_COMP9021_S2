# Randomly fills an array of size 10x10 with True and False, and outputs the number of blocks
# in the largest block construction, determined by rows of True's that can be stacked
# on top of each other.
#
# Written by *** and Eric Martin for COMP9021


from random import seed, randrange
import sys

dim = 10
def display_grid():
    for i in range(dim):
        print('     ', end ='  ')
        print(' '.join(f'{int(e)}' for e in grid[i]))
    print()

try:
    for_seed, n = input('Enter two integers, the second one being strictly positive: ').split()
    for_seed = int(for_seed)
    n = int(n)
    if n <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[bool(randrange(n)) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()

# def a function that we can get every stack from each row, then we can use these stack as a bottom of the final stack
# we not noly need too collect the number of each stack but also the index value
def get_every_stack_from_row(row):
    
    count = 0
    i = 0
    collect_count = []
    for e in row[i:]:
        if e:
            count = count + 1
            i = i + 1
            if i == len(row):
                collect_count.append((count, i - 1))
            continue
        
        if count > 0:
            collect_count.append((count, i - 1))
        
        i = i + 1
        count = 0
    return (collect_count)


# here we define a function to collect the continuous 1(True) in every column,
# this is used to find out how many 1(True) are connected with the bottom
def get_initial_stack_from_column(column):
    column_count = 0
    for e in column:
        if e:
            column_count = column_count + 1
            continue
        break
    return (column_count)

# this function is used to  calculate every column(based on the bottom, we identify this attribute with the index value)
# we need to eliminate the row that we collect bottom, and reverse the spare column!!
# list(zip(*List)) can call all the column out and build a new list, after that we can use the 'get_initial_stack_from_column(column)' to calculate the stack
# Then we use for loop to consider each column over the bottom, and calculate the all stacks
def get_stack_over_row_stack(row_index, stack_length, stack_index):
    sum_column_stack = []
    L_reverse = (grid[:row_index])[:: -1]
    left_column = list(zip(*L_reverse))
    
    # consider the first row it has no row over it
    if not left_column:
        sum_column_stack = []
    else:
        for i in range(stack_index - stack_length + 1, stack_index + 1):
            print(get_initial_stack_from_column(left_column[i]))
            sum_column_stack.append(get_initial_stack_from_column(left_column[i]))
    return sum(sum_column_stack)



# we use the first for loop to consider each row in this List
# we used the second for loop to calculate the stacks over each bottom in every row
# plus the original bottom and stacks over this bottom, we get the final stack
# consider the empty [] situation
row_index = 0
collect_all_final_stack = []
for row in grid:
    
    every_stack_from_row = get_every_stack_from_row(row)
    for (stack_length,stack_index) in every_stack_from_row:
        stack_over_row_stack = get_stack_over_row_stack(row_index,stack_length,stack_index)
        final_stack = stack_over_row_stack + stack_length
        collect_all_final_stack.append(final_stack)
    row_index = row_index + 1
if collect_all_final_stack == []:
    largest_block_construction = 0
else:
    largest_block_construction = max(collect_all_final_stack)



if largest_block_construction == 0:
    print('The largest block construction has no block.')

else:
    print(f'The largest block construction has {largest_block_construction} blocks.')
