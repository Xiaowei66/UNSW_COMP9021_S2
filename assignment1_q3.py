import os
import sys
import re
from collections import defaultdict, Counter


# check: does this file exit
try:
    filename = input('Please enter the name of the file you want to get data from: ')
    if not os.path.exists(filename):
        print('Sorry, there is no such file. ')
        sys.exit()

except ValueError:
    print('Sorry, there is no such file. ')
    sys.exit()


# check there is at least two numbers
with open(filename) as whole_file:
    content_whole_file = whole_file.read()

if len(content_whole_file.split()) < 2:
    print('Sorry, input file does not store valid data. ')
    sys.exit()

# check there is not negative,zero,float numbers
#print(content_whole_file)
check_integer = re.compile(r'(.\..)|(\-.)|(0.)|(^0$)')
for i in content_whole_file.split():
    if check_integer.match(i):
        print('Sorry, input file does not store valid data. ')
        sys.exit()
    if not i.isdigit():
        print('Sorry, input file does not store valid data. ')
        sys.exit()
#print(content_whole_file.split())
#print(sorted(content_whole_file.split()))
#print('1up is ok')
#print(content_whole_file.split())
# check it is be a strictly increasing sequence, if the result of using sorted(small - big) is not the same as the original sequence
if content_whole_file.split() != sorted(content_whole_file.split(),key = int):
    print('Sorry, input file does not store valid data. ')
    sys.exit()
#print('1-2 up is ok')
# turn the element from string to integer
int_content_whole_file = []
for i in content_whole_file.split():
    int_content_whole_file.append(int(i))

#print('2up is ok')
#print(int_content_whole_file)
# check is there duplicate numbers
ckeck_duplicate_list = [i for i in set(int_content_whole_file)]
#print(ckeck_duplicate_list)
if len(ckeck_duplicate_list) != len(int_content_whole_file):
    print('Sorry, input file does not store valid data. ')
    sys.exit()

#print(int_content_whole_file)

gap_pillars = int_content_whole_file[1] - int_content_whole_file[0]

def check_perfect(input_list):
    for i in range(1,len(input_list)):
        if (int(input_list[i]) - int(input_list[i-1])) != gap_pillars:
            return False

return True



if check_perfect(int_content_whole_file):
    print('The ride is perfect!')
else:
    print('The ride could be better...')


# started to collect the gap
c_gap = []
for i in range(1,len(int_content_whole_file)):
    c_gap.append((int(int_content_whole_file[i]) - int(int_content_whole_file[i-1])))

#print(c_gap)



counts = defaultdict(lambda: 0)
for i in c_gap:
    counts[i] += 1
#print(counts)

tuple_counts = sorted(counts.items(), key = lambda item:item[1])

#print(tuple_counts)
#print((tuple_counts[-1])[1])

# find the longest same gap

best_gap = (tuple_counts[-1])[0]
answer_times = []
collect_times = 0

for i in c_gap:
    if i == best_gap:
        collect_times = 1 + collect_times
        answer_times.append(collect_times)
    else:
        collect_times = 0
        continue

#print(max(answer_times))

print(f'The longest good ride has a length of: {max(answer_times)}')


# calculate THE gap and times it occur

def input_x(x):
    all_count = []
    for y in range(x+1, len(int_content_whole_file)):
        gap = int_content_whole_file[y] - int_content_whole_file[x]
        count = 0
        for n in range(1,len(int_content_whole_file)):
            if (int_content_whole_file[y]+gap*n) in int_content_whole_file[x+1 :]:
                count = count +1
            else:
                break
        all_count.append((count,(int_content_whole_file[y] - int_content_whole_file[x])))
    
    return(all_count)


alllist = []
for i in range(len(int_content_whole_file)):
    alllist.extend(input_x(i))

#print(alllist)

#print(max(alllist))


#print(len(int_content_whole_file) - (max(alllist)[0]+2))

print(f'The minimal number of pillars to remove to build a perfect ride from the rest is: {len(int_content_whole_file) - (max(alllist)[0]+2)}')
