import re
import math

def funcio_2n_grau(a,b,c):
    r1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
    r2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
    return [min([r1,r2]),max([r1,r2])]

def better_options(t, d_record):
    d_max = t**2/4
    r1 , r2 = funcio_2n_grau(1,-t,d_record)
    if r1 != math.ceil(r1):
        o1 = math.ceil(r1)
    else:
        o1 = r1+1
    if r2 != math.floor(r2):
        o2 = math.ceil(r2)
    return o2-o1


def puzzle_one():
    f = open('2023/day6_input.txt','r')
    times = [int(x) for x in re.findall(r'(\d+)',f.readline())]
    distance = [int(x) for x in re.findall(r'(\d+)',f.readline())]
    options = 1
    for t, d in zip(times,distance):
        
        n_opt = better_options(t,d)
        options = n_opt*options

    return options

def puzzle_two():
    f = open('2023/day6_input.txt','r')
    time = int(''.join(re.findall(r'(\d+)',f.readline())))
    distance = int(''.join(re.findall(r'(\d+)',f.readline())))    
    n_opt = better_options(time,distance)

    return n_opt


print(puzzle_one())
print(puzzle_two())
