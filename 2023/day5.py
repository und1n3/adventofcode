import re

def puzzle_one():
    file = open('2023/day5_input.txt','r')
    lines = file.readlines()
    map_names = []
    map_dict = {}
    for line in lines:
        if "seeds" in line:
            seeds =[int(x) for x in line.replace('seeds: ','').split(' ')]
        elif line[0].isalpha():
            map_names.append(line.split(' ')[0])
        elif line[0].isnumeric():
            if map_names[-1] not in map_dict.keys():
                map_dict[map_names[-1]] = {'origin':[],'destination':[]}
            destination , origin, ranges = [int(x) for x in line.split(' ')]
            map_dict[map_names[-1]]['origin'].append([origin, origin+ranges-1])
            map_dict[map_names[-1]]['destination'].append([destination, destination+ranges-1])
    locations = []
    for s in seeds: 
        start = s
        for name in map_names:
            for origin, destination in zip(map_dict[name]['origin'],map_dict[name]['destination']):
                if start>= origin[0] and start<=origin[1]:
                    start = destination[0] + start - origin[0]
                    
                    break
        locations.append(start)
    return min(locations)

# print(puzzle_one())  
    

def puzzle_two():
    file = open('2023/day5_input.txt','r')
    lines = file.readlines()

    map_names = []
    map_dict = {}
    for line in lines:
        if "seeds" in line:
            seeds =[int(x) for x in line.replace('seeds: ','').split(' ')]
        elif line[0].isalpha():
            map_names.append(line.split(' ')[0])
        elif line[0].isnumeric():
            if map_names[-1] not in map_dict.keys():
                map_dict[map_names[-1]] = {'origin':[],'destination':[]}
            destination , origin, ranges = [int(x) for x in line.split(' ')]
            map_dict[map_names[-1]]['origin'].append([origin, origin+ranges-1])
            map_dict[map_names[-1]]['destination'].append([destination, destination+ranges-1])
    location = 100000000000000000
    i = 0
    while i<len(seeds):
        for s in range(seeds[i],seeds[i]+seeds[i+1]): 
            # print(s)
            start = s
            for name in map_names:
                for origin, destination in zip(map_dict[name]['origin'],map_dict[name]['destination']):
                    if start>= origin[0] and start<=origin[1]:
                        start = destination[0] + start - origin[0]
                        
                        break
            if location > start:
                location = start
        i+=2
    return location
print(puzzle_two())