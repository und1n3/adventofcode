
def custom_sort_key(tuple_item,custom_order):
    return [custom_order.index(char) if char in custom_order else ord(char) for char in tuple_item[0]]

def sort_by_value(list_values,custom_order):
    list_values = sorted(list_values,key=lambda x : custom_sort_key(x,custom_order=custom_order),reverse=True)
    return list_values

def puzzle_one():
    file = open('2023/day7_input.txt','r')
    lines = file.readlines()
    custom_order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

    single, pair, double_pair, trio, house, four , five = ([] for i in range(7))
    for line in lines:
        hand, bid = line.strip().split(' ')
        count = {i:hand.count(i) for i in hand}
        values = list(count.values())
        # case pair
        if 3 not in values and values.count(2)==1:
            pair.append((hand,bid))
        # case double pair
        elif values.count(2)==2:
            double_pair.append((hand,bid)) 
        # case trio
        elif 3 in values and 2 not in values:
            trio.append((hand,bid))
        # case full house
        elif 3 in values and 2 in values:
            house.append((hand,bid))
        # case four of a kind
        elif 4 in values:
            four.append((hand,bid))
        # case five of a kind
        elif 5 in values:
            five.append((hand,bid)) 
        # else, higher card
        else:
            single.append((hand,bid))
    final = []
    for l in [single, pair, double_pair,trio, house, four , five]:
        sorted_list = sort_by_value(l,custom_order)
        final.extend(sorted_list)
    result = 0
    for i in range(len(final)):
        result+= int(final[i][1])*(i+1)

    return result
    


def puzzle_two():
    #Now we add jokers
    file = open('2023/day7_input.txt','r')
    lines = file.readlines()
    custom_order2 = ['A', 'K', 'Q',  'T', '9', '8', '7', '6', '5', '4', '3', '2','J']

    single, pair, double_pair, trio, house, four , five = ([] for i in range(7))
    for line in lines:
        hand, bid = line.strip().split(' ')
        count = {i:hand.count(i) for i in hand}
        if 'J' in hand:
            number_J = count['J']
            count.pop('J')
            #afegim les J a la lletra amb recompte més alt
            if count != {}:
                values = list(count.values())
                values.sort()
                values[-1] = values[-1]+number_J
            else:
                values = [5]
        else:
            values = list(count.values())
        # case pair
        if values.count(2)==1 and 3 not in values :
            pair.append((hand,bid))
        # case double pair
        elif values.count(2)==2:
            double_pair.append((hand,bid)) 
        # case trio
        elif 3 in values and 2 not in values:
            trio.append((hand,bid))
        # case full house
        elif 3 in values and 2 in values:
            house.append((hand,bid))
        # case four of a kind
        elif 4 in values:
            four.append((hand,bid))
        # case five of a kind
        elif 5 in values:
            five.append((hand,bid)) 
        # else, higher card
        else:
            single.append((hand,bid))
    final = []
    for l in [single, pair, double_pair,trio, house, four , five]:
        sorted_list = sort_by_value(l,custom_order2)
        final.extend(sorted_list)
    result = 0
    for i in range(len(final)):
        result+= int(final[i][1])*(i+1)

    return result
    

# print(puzzle_one())
print(puzzle_two())