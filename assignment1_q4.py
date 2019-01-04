# import related functions

import os.path
import sys



try:
    filename = input('Please enter the name of the file you want to get data from: ')
    if not os.path.exists(filename):
        print('Sorry, there is no such file.')
        sys.exit()
except ValueError:
    print('Sorry, there is no such file. ')
    sys.exit()

# read the content of this file
with open(filename) as tunnel_input:
    original_tunnel_sequence = tunnel_input.readlines()

# remove the '/n' in the original list
tunnel_sequence = []
for i in original_tunnel_sequence:
    if not i == '\n':
        tunnel_sequence.append(i)

#print(tunnel_sequence)

# identify how many lines this file have
#print('11111')
#print(len(tunnel_sequence))


if not len(tunnel_sequence) == 2:
    print('Sorry, input file does not store valid data.')
    sys.exit()

line1_sequence_tunnel = (tunnel_sequence[0]).split()
line2_sequence_tunnel = (tunnel_sequence[1]).split()

#print(line1_sequence_tunnel)
#print(line2_sequence_tunnel)

# identify the number of integers in two line is the same
# identify at least two integers
if len(line1_sequence_tunnel) != len(line2_sequence_tunnel) or len(line1_sequence_tunnel) < 2 :
    print('Sorry, input file does not store valid data.')
    sys.exit()



# identify the elements are all integers
for i in line2_sequence_tunnel + line2_sequence_tunnel:
    if not i.isdigit():
        print('Sorry, input file does not store valid data.')
        sys.exit()


# identify line1[i] > line2[i]
# connected_sequence_tunnel = line1_sequence_tunnel + line2_sequence_tunnel
# for i in range(len(line2_sequence_tunnel)):
#    if int(connected_sequence_tunnel[i]) < int(connected_sequence_tunnel[i+len(line2_sequence_tunnel)]):
#        print('Sorry, input file does not store valid data.')
#        sys.exit()


s1 = []
for i in line1_sequence_tunnel:
    s1.append(int(i))

s2 = []
for i in line2_sequence_tunnel:
    s2.append(int(i))

#print(s1)
#print(s2)

# identify line1[i] > line2[i]
for i in range(len(s1)):
    if s1[i] <= s2[i]:
        print('Sorry, input file does not store valid data.')
        sys.exit()


def get_gap_list_in_s1s2(x):
    gap = []
    for i in range(s2[x],s1[x]):
        gap.append(i)
    
    return gap

#print('gap')
#print(get_gap_list_in_s1s2(0))

def get_index_when_tunnel_stop(element_in_gap,column):
    for i in range(column + 1,len(s1)):
        if element_in_gap < s1[i] and element_in_gap >= s2[i]:
            if i == len(s1) - 1:
                return len(s1)
            continue
        else:
            return i
#print('i')
#print(get_index_when_tunnel_stop(6,0))
#print('i2')
#print(get_index_when_tunnel_stop(6,1))
#print('i3')
#print(get_index_when_tunnel_stop(6,10))

def all_get_index_when_tunnel_stop(column):
    answer = []
    for x in get_gap_list_in_s1s2(column):
        answer.append(get_index_when_tunnel_stop(x,column))
    return answer

# print(all_get_index_when_tunnel_stop(14))

all_distance = []
for column in range(len(s1)):
    for e in all_get_index_when_tunnel_stop(column):
        if e:
            all_distance.append(str(e-column))

#print(get_gap_list_in_s1s2(2))
#print(all_get_index_when_tunnel_stop(2))
#print(all_distance)
#print(max(all_get_index_when_tunnel_stop(0)))
#print(max(all_distance))


print(f'From the west, one can see into the tunnel over a distance of {max(all_get_index_when_tunnel_stop(0))}.')
print(f'Inside the tunnel, one can see into the tunnel over a maximum distance of {max(all_distance)}.')
