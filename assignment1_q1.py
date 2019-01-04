# we need to use the sys.exit()
import sys
from collections import Counter

try:
    input_file_name = input('Which data file do you want to use?')
    input_file  = open(f'{input_file_name}')
except FileNotFoundError:
    print('We can\'t find your documents')
    sys.exit()

# read every line in this file
lines = input_file.readlines()

# build a list contain every line
all_list = []
for every_line in lines:
    all_list.extend(every_line.split())

# identify the negative number
for i in all_list:
    if int(i) < 0:
        print('Your land.txt includes negative numbers')
        sys.exit()

# input_the rain
try:
    input_rain = int(input('How many decilitres of water do you want to pour down?'))
    if not type(input_rain) == int:
        print('it should be a positive integer')
    if int(input_rain) < 0:
        print('Incorrect input, it should be a positive integer')
except ValueError:
    print('Incorrect input')
    sys.exit()


# (Counter(sorted(all_list)))  count the times every layer appears
calculate_square = []
for a,b in Counter(sorted(all_list)).items():
    calculate_square.append((a,b))

#print(calculate_square)

# how many spaces each height includes, return it as a list
times_each_square = []
for (a,b) in calculate_square:
    times_each_square.append(b)


# define a function that when the rain is poured to the layer, how many space each_square have
def sum_times_each_square(n):
    sum = 0
    for i in range(n):
        sum = int(times_each_square[i]) + sum
    return sum

# this function is used to calculate when we need to fully fill this floor to next floor
# how much rain we totally need (including every floor)
# return current situation
def all_fill_rain(n):
    
    all_sum = 0
    for i in range(1,n+1):
        all_sum = sum_times_each_square(i) + all_sum
    return all_sum

# this function is used to calculate when we need to fully fill this floor to next floor
# how much rain we totally need (including every floor)
# return it with a list
def all_fill_rain_up_every_floor(n):
    up_every_floor_all_fill_rain = []
    up_floor_all_sum = 0
    for i in range(1,n+1):
        up_floor_all_sum = sum_times_each_square(i) + up_floor_all_sum
        up_every_floor_all_fill_rain.append(up_floor_all_sum)
    return up_every_floor_all_fill_rain

# this function is used to count when the input_rain can fully_fill which floor but not the next floor
# output this floor's index!! Attention it's the index!
# So we need to call the actual value when we want to use the height of this floor
def which_floor_rain_can_full_fill(rain):
    outcome = []
    floors = len(times_each_square)
    count = 0
    for i in all_fill_rain_up_every_floor(floors):
        count = count + 1
        if int(i) < input_rain:
            outcome.append(i)
            continue
        else:
            break
    return count

# calculate when the input_rain can fill this floor but it can't fill next floor
# So use the input_rain minus all the rain that needed to fill this floor
# Then calculate the spare rain, and separate it to the next space (remember when you fill the first follor,
# they all become to the space of next floor)

c_level = (input_rain - all_fill_rain(which_floor_rain_can_full_fill(input_rain)-1)) / sum_times_each_square(which_floor_rain_can_full_fill(input_rain))

#print(c_level)
#print(which_floor_rain_can_full_fill(input_rain))
# at the same time, calculate what's the centiminter of this floor
# we calculate it caaording to the index, Because sometimes these floors will not follow 1,2,3,4,5.
# the may follow 1,3,5,7,8 and so on. However the index will not change!!! we can always assume it's 1,2,3,4,5.
# But we need to call it back when we need the real height!

#print(which_floor_rain_can_full_fill(input_rain))

if int(which_floor_rain_can_full_fill(input_rain)) >= int((calculate_square[-1])[0]):
    final_c_level = c_level + float(calculate_square[-1][0])
else:
    final_c_level = float((calculate_square[which_floor_rain_can_full_fill(input_rain)-1])[0])+ c_level

print(f'The water rises to {final_c_level:.2f} centimetres.')
