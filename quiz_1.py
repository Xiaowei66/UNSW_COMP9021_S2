

# written by Xiaowei Zhu Z5102903, The second draft of QUIZ 1 COMP9021

# Firstly, we need to import the basic founction that we need to use in this program.
import sys
from random import seed , randrange
from collections import Counter

# we use try function to avoid the system error

while True:
    try:
        arg_for_seed = int(input('Enter an integer'))
        break
    
    except ValueError:
        print('Incorrect input, giving up.')
        continue

# create a random unmber
# seed() is used to create a permanent(if the input of seed is always the same) random number
seed(arg_for_seed)
x = randrange(10**10)

sum_of_digit_in_x = 0
# peoduce a list (10 elements every elements is produced by randrange(10**8))
L = [randrange(10**8) for _ in range(10)]


# calculate the sum of all digits in x
for each in str(x):
    sum_of_digit_in_x = int(each) + sum_of_digit_in_x


# compare the first and last digit and account them
first_digit_greater_than_last = 0
same_first_and_last_digits = 0
last_digit_greater_than_first = 0

for each in L:
    first = list(str(each))[0]
    last = list(str(each))[len(str(each))-1]
    if first > last:
        first_digit_greater_than_last = first_digit_greater_than_last + 1
    elif first == last:
        same_first_and_last_digits = same_first_and_last_digits + 1
    else:
        last_digit_greater_than_first = last_digit_greater_than_first +1


# calculate the number of distinct digits in one member
# use the
distinct_digits = []
from collections import Counter
for each in L:
    dictionary_L = Counter(str(each))
    length = len(dictionary_L)
    distinct_digits.append(length)



# compare the gap between the first and last difits
gap = []
for each in L:
    first = list(str(each))[0]
    last = list(str(each))[len(str(each))-1]
    gap.append(abs(int(first) - int(last)))
print(gap)
min_gap = sorted(gap)[0]
# Always pay attention on the 'len()-1'
max_gap = sorted(gap)[len(sorted(gap))-1]



first_last = []
# Build a list that contain the first and last digit
for each in L:
    first = list(str(each))[0]
    last = list(str(each))[len(str(each))-1]
    first_last.append((int(first),int(last)))


# Counter(first_last), this is used to buld a Dicitionary that contain the times every distinct element occur
new_forast_last = sorted(Counter(first_last).items(),key=lambda item:item[1])
(key_last,value_last) = new_forast_last[len(new_forast_last)-1]

first_and_last=[]
for key,values in  new_forast_last:
    if values == value_last:
        first_and_last.append(key)


print()
print('x is:', x)
print('L is:', L)
print()
print(f'The sum of all digits in x is equal to {sum_of_digit_in_x}.')
print()
print(f'There are {first_digit_greater_than_last}, {same_first_and_last_digits} '
      f'and {last_digit_greater_than_first} elements in L with a first digit that is\n'
      '  greater than the last digit, equal to the last digit,\n'
      '  and smaller than the last digit, respectively.'
      )
print()
for  i in set(distinct_digits):
    times = distinct_digits.count(i)
    print(f'The number of members of L with {i} distinct digits is {times}.')


print()
print('The minimal gap (in absolute value) between first and last digits\n'
      f'  of a member of L is {min_gap}.'
      )
print('The maximal gap (in absolute value) between first and last digits\n'
      f'  of a member of L is {max_gap}.')



print()
print('The number of pairs (f, l) such that f and l are the first and last digits\n'
      f'of members of L is maximal for (f, l) one of {sorted(first_and_last)}.'
      # sorted is a function used to sort a list but i doesn't produce a new list!!!!
      )

