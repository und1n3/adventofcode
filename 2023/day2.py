import re

def puzzle_one():
    restrictions = {'red':12,'green':13,'blue':14}

    file = open('2023/day2_input.txt','r')
    lines = file.readlines()
    
    ids_list = []

    for line in lines:
        max_red = max(list(map(int,re.findall(r'(\d+) red',line))))
        max_blue =  max(list(map(int,re.findall(r'(\d+) blue',line))))
        max_green =  max(list(map(int,re.findall(r'(\d+) green',line))))
       
        if max_red<=restrictions['red'] and max_blue<=restrictions['blue'] and max_green<=restrictions['green']:
            game_num = int(re.findall(r'Game (\d+)',line)[0])
            ids_list.append(game_num)

    return sum(ids_list)
    

def puzzle_two():

    file = open('2023/day2_input.txt','r')
    lines = file.readlines()
    
    ids_list = []

    for line in lines:
        max_red = max(list(map(int,re.findall(r'(\d+) red',line))))
        max_blue =  max(list(map(int,re.findall(r'(\d+) blue',line))))
        max_green =  max(list(map(int,re.findall(r'(\d+) green',line))))
       
        power = max_blue*max_red*max_green
        ids_list.append(power)

    return sum(ids_list)

    
    
print(puzzle_one())
print(puzzle_two())