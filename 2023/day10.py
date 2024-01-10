import numpy as np

directions = {'|':('n','s'),
              '-':('e','w'),
              'L':('n','e'),
              'J':('n','w'),
              '7':('s','w'),
              'F':('s','e'),
              }
def puzzle_one():
    file = open('2023/day10_input.txt','r')
    lines = file.readlines()
    arr = np.array([list(line.strip()) for line in lines])
    x_max,y_max = arr.shape

    start = np.where(arr=='S')
    s_x,s_y = start[0][0],start[1][0]
    path = ['S']
    next = 'n'
    while True:
        if next == 'n' and s_x >0:
            s_x -=1
            value = arr[s_x,s_y]
            if value == 'S':
                path.append(value)
                break
            next = [x for x in directions[value] if x != 's'][0]
        elif next == 's' and s_x+1 <x_max :
            s_x +=1
            value = arr[s_x,s_y]
            if value == 'S':
                path.append(value)
                break
            next = [x for x in directions[value] if x != 'n'][0]
        elif next == 'e' and s_y+1 <y_max :
            s_y +=1
            value = arr[s_x,s_y]
            if value == 'S':
                path.append(value)
                break
            next = [x for x in directions[value] if x != 'w'][0]
        elif next == 'w' and s_y > 0:
            s_y -=1
            value = arr[s_x,s_y]
            if value == 'S':
                path.append(value)
                break
            next = [x for x in directions[value] if x != 'e'][0]
        else:
            ...
        path.append(value)
     
    return int(len(path)/2)
            


def puzzle_two():
    file = open('2023/day10_input.txt','r')
    lines = file.readlines()
    arr = np.array([list(line.strip()) for line in lines])
    x_max,y_max = arr.shape

    start = np.where(arr=='S')
    s_x,s_y = start[0][0],start[1][0]
    print(f'{s_x} {s_y}')    
    boundaries = np.zeros((x_max,y_max)) # {row:[columns]}
    boundaries[s_x,s_y] = 1
    next = 'n'
    while True:
        if next == 'n' and s_x >0:
            s_x -=1
            value = arr[s_x,s_y]
            boundaries[s_x,s_y] = 1
            if value == 'S':
                break
            next = [x for x in directions[value] if x != 's'][0]

        elif next == 's' and s_x+1 <x_max :
            s_x +=1
            value = arr[s_x,s_y]
            boundaries[s_x,s_y] = 1
            if value == 'S':
                break
            next = [x for x in directions[value] if x != 'n'][0]
        elif next == 'e' and s_y+1 <y_max :
            s_y +=1
            value = arr[s_x,s_y]
            boundaries[s_x,s_y] = 1
            if value == 'S':
                break
            next = [x for x in directions[value] if x != 'w'][0]
        elif next == 'w' and s_y > 0:
            s_y -=1
            value = arr[s_x,s_y]
            boundaries[s_x,s_y] = 1
            if value == 'S':
                break
            next = [x for x in directions[value] if x != 'e'][0]
        else:
            ...
    boundaries[s_x,s_y] = 1
    print(boundaries)

    tiles = 0
    for row in range(x_max):
        for column in range(y_max):
            if boundaries[row,column]!=1:
                up = boundaries[row,:column+1].sum()
                down = boundaries[row,column:].sum()
                right = boundaries[row:,column].sum()
                left = boundaries[:row+1,column].sum()
                if up%2== 0 or down%2 == 0 or right%2 ==0 or left%2 == 0:
                    pass                   
                else:
                    
                    tiles+=1 
    return tiles
              

print(puzzle_two())
print(puzzle_one())