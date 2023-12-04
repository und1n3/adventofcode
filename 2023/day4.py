import re

def puzzle_one():
    file = open('2023/day4_input.txt','r')
    lines = file.readlines()
    points = []
    for line in lines:
        winning_numbers = [int(x) for x in re.findall(r'\b(\d+)\b',line.split('|')[0].split(':')[1])]
        opting_numbers = [int(x) for x in re.findall(r'\b(\d+)\b',line.split('|')[1]) ]
        card_value = 0        
        for x in opting_numbers:
            if x in winning_numbers:
                if card_value==0:
                    card_value=1
                else:
                    card_value = card_value*2
        points.append(card_value)
    return sum(points)

    

def puzzle_two():
    file = open('2023/day4_input.txt','r')
    lines = file.readlines()
    cards = [1 for x in range(len(lines))]
    i = 0
    for line in lines:
        winning_numbers = [int(x) for x in re.findall(r'\b(\d+)\b',line.split('|')[0].split(':')[1])]
        opting_numbers = [int(x) for x in re.findall(r'\b(\d+)\b',line.split('|')[1]) ]
        repetitions = cards[i]
        n=0        
        for x in opting_numbers:
            if x in winning_numbers:
                n+=1
                cards[i+n] = cards[i+n] + repetitions
        i+=1
    return sum(cards)

print(puzzle_one())
print(puzzle_two())