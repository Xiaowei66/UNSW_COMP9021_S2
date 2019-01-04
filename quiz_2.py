


# In[3]:


import sys
from random import seed, randint
from math import gcd
from fractions import Fraction


# In[4]:


try:
    arg_for_seed, length, max_value = input('Enter three strictly positive integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, length, max_value = int(arg_for_seed), int(length), int(max_value)
    if arg_for_seed < 1 or length < 1 or max_value < 1:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randint(1, max_value) for _ in range(length)]

print('Here is L:')
print(L)
print()
len(L)


# In[5]:


all_fractions = []

for i in range(len(L)):
    n = L[i]
    L2 = L[:]
    for m in L2:
        if n/m <= 1:
            f = Fraction(n,m)
            all_fractions.append(f)


# In[8]:


tuple_all_fractions = []
for i in set(all_fractions):
    tuple_all_fractions.append((i.numerator, i.denominator))


# In[9]:


all_fractions_float = []
length = len(set(tuple_all_fractions))
for i in set(tuple_all_fractions):
    all_fractions_float.append((i, i[0]/i[1]))



# In[10]:


sort_all_fractions_float = sorted(all_fractions_float, key= lambda item:item[1])


# In[12]:


finished_sort_all_fractions_float = []
for i in sort_all_fractions_float:
    finished_sort_all_fractions_float.append(i[0])


# In[20]:


simplest_fractions = []
complex_fractions = []
for i in finished_sort_all_fractions_float:
    if int(max(i)) < 10:
        simplest_fractions.append(i)
    else:
        complex_fractions.append(i)

if  not complex_fractions:
    complex_fractions = simplest_fractions


complex_fractions.reverse()


# In[21]:


max_len = 2
for i in complex_fractions:
    if len(str(i[0])+ str(i[1])) >= max_len:
        max_len = len(str(i[0])+ str(i[1]))


# In[22]:


most_complex_fractions = []
for i in complex_fractions:
    if len(str(i[0]) + str(i[1])) == max_len:
        most_complex_fractions.append(i)


# In[23]:


size_of_simplest_fraction = len(str((simplest_fractions[0])[0]) + str((simplest_fractions[0])[1]))


# In[24]:


size_of_most_complex_fraction = len(str((most_complex_fractions[0])[0]) + str((most_complex_fractions[0])[1]))


# In[25]:


denominators = []
for (a,b) in most_complex_fractions:
    denominators.append(b)


# In[26]:


def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    for i in range(2,num):
        if num%i == 0:
            return False
    return True

# the function for looking for prime_factors of any integers
def prime_factors(n):
    i = 2
    factors = []
    while i <= n:
        if n % i == 0:
            if is_prime(i):
                factors.append(i)
            n = n//i
            i = 2
            continue
        i += 1
    
    return factors

# Counter is a very useful function, which needs to be imported
from collections import Counter
all = []
sum = []
for m in denominators:
    # figure out the list of prime_factors,and fiugre out the times vevry prime_factors occur, and use Counter() and sorted() to sort them
    order_prime_factor_multi = sorted(Counter(prime_factors(int(m))).items(),key=lambda item:item[1])
    # collect all the prime_factors and time, use extend ranther than append
    all.extend(order_prime_factor_multi)
    for (a,b) in order_prime_factor_multi:
        # collect the times every prime_factors coour
        sum.append(b)


try:
    answer2 = []
    
    for (n,m) in all:
        if m == max(sum):
            
            answer2.append(n)
    largest_prime_factors = sorted(set(answer2))
    multiplicity_of_largest_prime_factor = max(sum)
except ValueError:
    multiplicity_of_largest_prime_factor = 0


# In[27]:


print('The size of the simplest fraction <= 1 built from members of L is:',
      size_of_simplest_fraction
      )
print('From smallest to largest, those simplest fractions are:')
print('\n'.join(f'    {x}/{y}' for (x,y) in simplest_fractions))
print('The size of the most complex fraction <= 1 built from members of L is:',
      size_of_most_complex_fraction
      )
print('From largest to smallest, those most complex fractions are:')
print('\n'.join(f'    {x}/{y}' for (x,y) in most_complex_fractions))


# In[28]:


print("The highest multiplicity of prime factors of the latter's denominators is:",
      multiplicity_of_largest_prime_factor
      )
print('These prime factors of highest multiplicity are, from smallest to largest:')
print('   ', largest_prime_factors)

