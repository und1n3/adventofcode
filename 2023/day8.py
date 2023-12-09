
import math

def puzzle_one():
    f = open('2023/day8_input.txt')
    lines = f.readlines()

    instructions = lines[0].strip()
    nodes = {}
    for line in lines [2:]:
        node , next_tuple = line.strip().split(' = ')
        nodes[node] = (next_tuple[1:4],next_tuple[6:-1])
    
    starting  = 'AAA'
    steps = 0
    while True:
        for instruction in instructions:
            L, R = nodes[starting]
            steps+=1
            if instruction == 'L':
                starting = L
            else:
                starting = R
            
            if starting == 'ZZZ':
                return steps

def puzzle_two():
    f = open('2023/day8_input.txt')
    lines = f.readlines()

    instructions = lines[0].strip()
    nodes = {}
    for line in lines [2:]:
        node , next_tuple = line.strip().split(' = ')
        nodes[node] = (next_tuple[1:4],next_tuple[6:-1])
    
    starting  = [x for x in nodes.keys() if x[-1]=='A']
    numbers = [i for i in range(len(starting))]
    multiples = []
    print(starting)
    steps = 0
    while True:
        for instruction in instructions:
            steps+=1
            for i in range(len(starting)):
                L, R = nodes[starting[i]]
                
                if instruction == 'L':
                    starting[i] = L
                else:
                    starting[i] = R
                
            for i in range(len(starting)):
                if starting[i][-1]=='Z':
                    del(numbers[numbers.index(i)])
                    multiples.append(steps)
        if numbers == []:
            break
    lcm = 1
    for el in multiples:
        lcm = lcm*el//math.gcd(lcm, el)
    return lcm



# print(puzzle_one())
print(puzzle_two())