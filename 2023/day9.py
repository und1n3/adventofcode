
def extrapolate_number(l):
    """ l = list of given numbers """
    operations = [l]
    zeros = [z for z in l if z != 0]
    while zeros !=[]:
        diff = l.copy()
        l = [diff[i+1]-diff[i] for i in range(len(diff)-1)]
        zeros = [z for z in l if z != 0]
        operations.append(l)

    number = 0
    for line in operations[::-1]:
        number+=line[-1]

    return number

def extrapolate_number_backwards(l):
    operations = [l]
    zeros = [z for z in l if z != 0]
    while zeros !=[]:
        diff = l.copy()
        l = [diff[i+1]-diff[i] for i in range(len(diff)-1)]
        zeros = [z for z in l if z != 0]
        operations.append(l)

    number = 0
    for line in operations[::-1]:
        number = line[0] - number

    return number
def puzzle_one():
    f = open('2023/day9_input.txt')
    lines = f.readlines()

    last_numbers = []
    for line in lines:
        number_list = [int(x) for x in line.strip().split(' ')]

        last = extrapolate_number(number_list)
        last_numbers.append(last)
    
    return sum(last_numbers)


def puzzle_two():
    f = open('2023/day9_input.txt')
    lines = f.readlines()

    last_numbers = []
    for line in lines:
        number_list = [int(x) for x in line.strip().split(' ')]

        last = extrapolate_number_backwards(number_list)
        last_numbers.append(last)
    
    return sum(last_numbers)
    

print(puzzle_one())
print(puzzle_two())