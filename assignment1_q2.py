import sys
import re

check_integer = re.compile(r'(.\..)')
try:
    heroes_input = input('Please input the heroes\' powers: ')
    
    for i in heroes_input.split():
        if check_integer.match(i) or int(i) == 0:
            print('Sorry, these are not valid power values.')
            sys.exit()

except ValueError:
    print('Sorry, these are not  valid  power values.')
    sys.exit()

try:
    flips_input = input('Please input the number of power flips: ')
    if int(flips_input) < 0 or int(flips_input) > len(heroes_input.split()) or check_integer.match(flips_input):
        print('Sorry, this is not a valid number of power flips.')
        sys.exit()
except ValueError:
    print('Sorry, this is not a valid number of power flips.')
    sys.exit()


int_heroes_input = []
for i in heroes_input.split():
    int_heroes_input.append(int(i))

sorted_int_heroes_input = sorted(int_heroes_input)

pair_input_heroes = []
for i in sorted_int_heroes_input:
    pair_input_heroes.append((abs(i),i))

sorted_pair_input_heroes = sorted(pair_input_heroes)

reversed_sorted_pair_input_heroes = sorted(pair_input_heroes,reverse = True)




neg_pair_input_heroes = []
for (a,b) in sorted_pair_input_heroes:
    if b < 0:
        neg_pair_input_heroes.append((a,b))


# first question
first_sorted_pair_input_heroes = sorted_pair_input_heroes[:]
if int(flips_input) <= len(neg_pair_input_heroes):
    count = 0
    for i in range(len(sorted_int_heroes_input)):
        
        if (first_sorted_pair_input_heroes[-i-1])[1] < 0:
            first_sorted_pair_input_heroes[-i - 1] = ((first_sorted_pair_input_heroes[-i-1])[0],(first_sorted_pair_input_heroes[-i-1])[0])
            count = count +1
        if count >= int(flips_input):
            break
else:
    i = 0
    for (a,b) in first_sorted_pair_input_heroes:
        first_sorted_pair_input_heroes[i] = (a,a)
        i = i+1
    first_sorted_pair_input_heroes[0] =  ((first_sorted_pair_input_heroes[0])[0] ,(first_sorted_pair_input_heroes[0])[1]*(-1)**(int(flips_input) - len(neg_pair_input_heroes)))



answer = []
for (x,y) in first_sorted_pair_input_heroes:
    answer.append(y)
largest = sum(answer)



# second question

second_sorted_pair_input_heroes = sorted_pair_input_heroes[:]
if int(flips_input) <= len(neg_pair_input_heroes):
    second_sorted_pair_input_heroes = first_sorted_pair_input_heroes
    
    answer_2 = []
    for (x, y) in second_sorted_pair_input_heroes:
        answer_2.append(y)
    largest_2 = sum(answer_2)

else:
    i = 0
    count = 0
    for (a,b) in second_sorted_pair_input_heroes:
        if b > 0:
            count = count + 1
            second_sorted_pair_input_heroes[i] = (-a,b)
            if count >= (int(flips_input) - len(neg_pair_input_heroes)):
                break
        i = i + 1
    
    answer_2 = []
    for (x, y) in second_sorted_pair_input_heroes:
        answer_2.append(x)
    largest_2 = sum(answer_2)


# third question

third_input_heroes = int_heroes_input[:]

n_move = len(third_input_heroes) - int(flips_input) + 1

list_total_sum = []
for i in range(n_move):
    sum_n = third_input_heroes[i:i+int(flips_input)]
    exc_sum_n = [(-L) for L in sum_n]
    
    ori_outcome_sum_n = sum(sum_n)
    
    exc_outcome_sum_n = sum(exc_sum_n)
    
    total_sum = sum(third_input_heroes) - ori_outcome_sum_n + exc_outcome_sum_n
    list_total_sum.append(total_sum)




# fourth question

fourth_input_heroes = int_heroes_input[:]

move_step = len(fourth_input_heroes)

def collect_list(n):
    list_f_total_sum = []
    for i in range(n):
        f_sum_n = fourth_input_heroes[i:i+(1+(move_step-n))]
        f_total_sum = sum(fourth_input_heroes) - 2*sum(f_sum_n)
        list_f_total_sum.append(f_total_sum)
    return list_f_total_sum

all_collect_list = []
for i in range(move_step):
    all_collect_list.extend(collect_list(i+1))

all_collect_list.append(sum(fourth_input_heroes))


print(f'Possibly flipping the power of the same hero many times, the greatest achievable power is {largest}.')
print(f'Flipping the power of the same hero at most once, the greatest achievable power is {largest_2}.')
print(f'Flipping the power of nb_of_flips many consecutive heroes, the greatest achievable power is {max(list_total_sum)}.')
print(f'Flipping the power of arbitrarily many consecutive heroes, the greatest achievable power is {max(all_collect_list)}.')
