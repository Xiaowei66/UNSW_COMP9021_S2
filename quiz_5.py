# Prompts the user for a nonnegative integer that codes a set S as follows:
# - Bit 0 codes 0
# - Bit 1 codes -1
# - Bit 2 codes 1
# - Bit 3 codes -2
# - Bit 4 codes 2
# - Bit 5 codes -3
# - Bit 6 codes 3
# ...
# Computes a derived nonnegative number that codes the set of running sums
# of the members of S when those are listed in increasing order.
#
# Computes the ordered list of members of a coded set.
#
# Written by *** and Eric Martin for COMP9021

# import sys, use sys.exit()
import sys

# try,except a very good function to avoid wrong input
try:
    encoded_set = int(input('Input a nonnegative integer: '))
    if encoded_set < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()


# def a function to produce the list 0,-1,1,-2,2,-3,3.....
def bitfunction(x):
    bit_set = []
    for i in range(x+1):
        bit_set.extend([-i,i])
    return (bit_set[1:x+1])


# convert the D to binary, bin() or f...
bin_code = f'{encoded_set:b}'

# convert the string to a list
list_bin_code = list(bin_code)
# reverse this list
list_bin_code.reverse()

# print(list_bin_code)

# create a empty list and use index to map the element in list_bin_code and bitfunction
# if the value in list_bin_code is '1' then output the number in bitfunction

# we need to consider the empty situation
encoded = []
if encoded_set == 0:
    final_set_ecoded = {}
else:
    for i in range(len(list_bin_code)):
        if int(list_bin_code[i]):
            encoded.append(bitfunction(len(list_bin_code))[i])
    final_set_ecoded = sorted(encoded)


# create a function to count the sum
# also consider th 0 index situation
# sum(only one figure) is not vailable
def sum_list(alist,i):
    if i == 0:
        return alist[0]
    else:
        return sum(alist[:i+1])

# we can use a for loop to get the derived_set,consider every index value
# however we need to consider the empty situation
derived_set = []
if not final_set_ecoded:
    derived_set = []
else:
    
    for i in range(len(final_set_ecoded)):
        derived_set.append(sum_list(final_set_ecoded,i))


# because we may get some duplicated elements in the list,so we need to set it and list it again
final_derived_set = list(set(derived_set))


# consider the empty situation
# calculate the length of the bitfunction
if not final_set_ecoded:
    x = 1
else:
    x = max(abs(max(final_derived_set)),abs(min(final_derived_set)))


# get the bitfunction
# be careful of the length
derived_bin_set = bitfunction(2*x+1)[:]

derived_bin_set.reverse()

#print('--------------')
#print(derived_bin_set)
#print(derived_set)

# consider the empty situation
if derived_bin_set == []:
    derived_bin_set = [0]
# if the element can be found in the list convert it to 1,otherwise convert it to 0
else:
    for i in range(len(derived_bin_set)):
        if derived_bin_set[i] in derived_set:
            derived_bin_set[i] = 1
        else:
            derived_bin_set[i] = 0

#print(derived_bin_set)

#print(''.join(str(i) for i in derived_bin_set))

# trun the list to string(elements are connected to become a binary value)
str_derived_bin_set = ''.join(str(i) for i in derived_bin_set)


# display the output
def display(L):
    print('{', end='')
    print(', '.join(str(e) for e in L), end='')
    print('}')




print('The encoded set is: ', end='')
display(sorted(final_set_ecoded))

print('The derived set is encoded as:', int(str_derived_bin_set,2))
print('It is: ', end='')
display(sorted(final_derived_set))


