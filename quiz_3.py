
import csv
import sys
import os
import re



filename = 'monthly_csv.csv'
if not os.path.exists(filename):
    print(f'There is no file named {filename} in the working directory, giving up...')
    sys.exit()

try:
    input_source = input('Enter the source (GCAG or GISTEMP): ')
except ValueError:
    print('Wrong input, giving up')
    sys.exit()

try:
    input_year = input('Enter a year or a range of years in the form XXXX -- XXXX: ')
except ValueError:
    print('Wrong input, giving up')
    sys.exit()

try:
    input_month = input('Enter a month: ')
except ValueError:
    print('Wrong input, giving up')
    sys.exit()


# open this file from local directory and save it as a new file in python
with open(filename) as whole_file:
    #csv.reader(file) is used to read the content
    csv_whole_file = csv.reader(whole_file)
    whole_source_date_mean = []
    #Through for loop, save this content as a List
    for (source, date, mean) in csv_whole_file:
        whole_source_date_mean.append(((date.split('-')),source,mean))


month_value = ['January','February','March','April','May','June','July','August','September','October','November','December']

# lower_input_month = input_month.lower()


m = 0
# need to define a dictionary firstly!!
dict_month_number = {}
for i in month_value:
    m = m + 1
    dict_month_number[i] = (m)

only_one_year_value = re.compile(r'^[0-9]{4}$')
int_input_year = []
if only_one_year_value.match(input_year):
    int_input_year = [int(input_year)]
else:
    if int((input_year.split('--'))[0]) == int((input_year.split('--'))[1]):
        int_input_year = [int((input_year.split('--'))[0])]
    else:
        for i in (input_year.split('--')):
            int_input_year.append(int(i))


def is_year_in(y):
    # we need to identify 1 year  or 2 year, use regular expression
    #    only_one_year_value = re.compile(r'^[0-9]{4}$')
    if len(int_input_year) <= 1:
        for year in [int(int_input_year[0])]:
            if y == year:
                return True
    else:
        # split the two year, turn to int and sort!! from samll to big
        for year in range((sorted(int_input_year))[0], (sorted(int_input_year))[1]+1):
            if y == year:
                return True



# Under the for loop, identify does the input_year satisfy these three requirement!
# use append to collect them
collect_satisfied_mean = []
collect_satisfied_year_mean = []
for (date, source, mean) in whole_source_date_mean[1:]:
    if int(date[1]) == int(dict_month_number[input_month]) and source == input_source and is_year_in(int(date[0])):
        collect_satisfied_mean.append(float(mean))
        # bulid a list that contains year and mean
        collect_satisfied_year_mean.append((int(date[0]),float(mean)))
avg_collect_satisfied_mean = sum(collect_satisfied_mean)/len(collect_satisfied_mean)
#avg_collect_satisfied_mean = statistics.mean(collect_satisfied_mean)



collect_year_over_mean = []
for (year_check,mean_check) in collect_satisfied_year_mean:
    if mean_check > avg_collect_satisfied_mean:
        collect_year_over_mean.append(year_check)



#print(f'The average anomaly for January in this range of years is:{round(avg_collect_satisfied_mean,2)}')
#print(f'The list of years when the temperature anomaly was above average is:{sorted(collect_year_over_mean)}')

print(f'The average anomaly for {input_month} in this range of years is: {avg_collect_satisfied_mean:.2f}.')
print('The list of years when the temperature anomaly was above average is:')
print(sorted(collect_year_over_mean))

