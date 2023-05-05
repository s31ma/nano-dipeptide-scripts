import math
import itertools

def calculate_average(column, filename):
    total = 0
    count = 0

    with open(filename, 'r') as f:
  
        lines = itertools.islice(f, 25, None)

        for line in lines:
            value = float(line.split()[column])
            total += value
            count += 1

    average = total / count
    return round(average)


def calculate_standard_deviation(column, filename):
    total = 0
    count = 0
    average = calculate_average(column, filename)

    with open(filename, 'r') as f:
       
        lines = itertools.islice(f, 25, None)

        for line in lines:
            value = float(line.split()[column])
            total += (value - average) ** 2
            count += 1

    variance = total / count
    standard_deviation = round(math.sqrt(variance))

    return standard_deviation


average_of_hydrogen = calculate_average(1, 'hbnum_peptide-water_AA.xvg')
std_dev_of_hydrogen = calculate_standard_deviation(1, 'hbnum_peptide-water_AA.xvg')
print(f'Average: {average_of_hydrogen}')
print(f'Standard Deviation: {std_dev_of_hydrogen}')