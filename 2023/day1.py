import re 

def puzzle_one():
    
    file = open('2023/day1_input.txt','r')
    lines = file.readlines()

    numbers = []
    for line in lines:
        text = line.strip()
        numbers_in_text = re.findall(r'\d',text)
        first_number = str(numbers_in_text[0])
        last_number = str(numbers_in_text[-1])

        numbers.append(int(first_number+last_number))
    return sum(numbers)

def puzzle_two():
    file = open('2023/day1_input.txt','r')
    lines = file.readlines()
    numbers_dict = {'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9','zero':'0'}
    numbers=[]
    for line in lines:
        text = line.strip()
        numbers_in_text = re.findall(r'(?:one|two|three|four|five|six|seven|eight|nine|\d)', text, re.IGNORECASE)
        
        first = numbers_in_text[0] 
        last = numbers_in_text[-1] 
        first_number = first if first not in numbers_dict.keys() else numbers_dict[first]
        last_number = last if last not in numbers_dict.keys() else numbers_dict[last]
        numbers.append(int(first_number+last_number))
    return sum(numbers)

# print(puzzle_one())
print(puzzle_two())

