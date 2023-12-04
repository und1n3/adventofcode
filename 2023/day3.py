import numpy as np

def puzzle_one():
    file = open('2023/day3_input.txt','r')
    lines = file.readlines()
    arr = np.array([list(line.strip()) for line in lines])
    rows , cols = arr.shape
    nums_list = []
    r = 0
    while r<rows:
        c =0
        while c<cols:
            if arr[r,c].isnumeric():
                n=0
                while  c+n+1 <cols and arr[r,c+n+1].isnumeric():
                    n+=1
                n+=1
                if r!=0:
                    if r+1<rows:
                        if c-1>=0:
                            if c+n+1<cols:
                                #aquest es el numero no esta al límit del document per cap banda
                                symbols = arr[r-1,c-1:c+n+1].tolist() + arr[r+1,c-1:c+n+1].tolist()+list(arr[r,c-1])+list(arr[r,c+n])
                            else:
                                #aquí el número es al final del document per la dreta
                                symbols = arr[r-1,c-1:c+n].tolist() + arr[r+1,c-1:c+n].tolist()+list(arr[r,c-1])
                        else:
                            #aquí el número és al final del document per l'esquerra
                            symbols = arr[r-1,c:c+n+1].tolist() + arr[r+1,c:c+n+1].tolist()+list(arr[r,c+n])
                    else:
                        #aqui estem a l'última línia del document
                        if c-1>=0:
                            if c+n+1<cols:
                                #aquest es el numero no esta al límit del document per cap banda
                                symbols = arr[r-1,c-1:c+n+1].tolist() +list(arr[r,c-1])+list(arr[r,c+n])
                            else:
                                #aquí el número es al final del document per la dreta
                                symbols = arr[r-1,c-1:c+n].tolist() +list(arr[r,c-1])
                        else:
                            #aquí el número és al final del document per l'esquerra
                            symbols = arr[r-1,c:c+n+1].tolist() +list(arr[r,c+n])
                else:
                    #aquí estem a la primera línia del document
                    if c-1>=0:
                        if c+n+1<cols:
                            #aquest es el numero no esta al límit del document per cap banda
                            symbols = arr[r+1,c-1:c+n+1].tolist()+list(arr[r,c-1])+list(arr[r,c+n])
                        else:
                            #aquí el número es al final del document per la dreta
                            symbols = arr[r+1,c-1:c+n].tolist()+list(arr[r,c-1])
                    else:
                        #aquí el número és al final del document per l'esquerra
                        symbols = arr[r+1,c:c+n+1].tolist()+list(arr[r,c+n])
                symbols = [x for x in symbols if x!='.']

                if len(symbols)>0:
                    nums_list.append(int(''.join(arr[r,c:c+n])))
                c = c+n
            c+=1
        r+=1
    return sum(nums_list)





def look_left(r,c,arr):
    n=0
    while True:
        if c-n-1 >= 0 and arr[r,c-n-1].isnumeric():
            n+=1
        else:
            break
    return ''.join(arr[r,c-n:c])

def look_right(r,c,arr,cols):
    n=0
    while True:
        if c+n+1 < cols and arr[r,c+n+1].isnumeric():
            n+=1
        else:
            break
    return ''.join(arr[r,c+1:c+n+1])
    
def puzzle_two():
    file = open('2023/day3_input.txt','r')
    lines = file.readlines()
    arr = np.array([list(line.strip()) for line in lines])
    rows , cols = arr.shape
    nums_list = []
    r = 0
    while r<rows:
        c =0
        while c<cols:
            if arr[r,c]=='*':

                i = 0 if c==0 else 1
                j = 0 if c==cols-1 else 1
                right = [x for x in arr[r,c+j] if x.isnumeric()]
                left = [x for x in arr[r,c-i] if x.isnumeric()]
                if r==0:
                    print(arr[r:r+2,c-i:c+j+1])

                    up_r = 0
                    up_m = 0
                    up_l = 0
                    down_r = 1 if arr[r+1,c+j].isnumeric() and arr[r+1,c]=='.' and j!=0 else 0
                    down_l = 1 if arr[r+1,c-i].isnumeric() and arr[r+1,c]=='.' and i!=0 else 0
                    down_m = 1 if arr[r+1,c].isnumeric() else 0
                elif r==rows-1:
                    print(arr[r-1:,c-i:c+j+1])

                    up_r = 1 if arr[r-1,c+j].isnumeric() and arr[r-1,c]=='.' and j!=0 else 0 
                    up_l = 1 if arr[r-1,c-i].isnumeric() and arr[r-1,c]=='.' and i!=0 else 0 
                    up_m = 1 if arr[r-1,c].isnumeric() else 0                    
                    down_r = 0 
                    down_l = 0
                    down_m = 0                
                else:
                    print(arr[r-1:r+2,c-i:c+j+1])

                    up_r = 1 if arr[r-1,c+j].isnumeric() and arr[r-1,c]=='.' and j!=0 else 0
                    up_l = 1 if arr[r-1,c-i].isnumeric() and arr[r-1,c]=='.' and i!=0 else 0 
                    up_m = 1 if arr[r-1,c].isnumeric() else 0                    
                    down_r = 1 if arr[r+1,c+j].isnumeric() and arr[r+1,c]=='.' and j!=0 else 0
                    down_l = 1 if arr[r+1,c-i].isnumeric() and arr[r+1,c]=='.' and i!=0 else 0 
                    down_m = 1 if arr[r+1,c].isnumeric() else 0
                r1 = 1 if len(right)>0 else 0
                l1 = 1 if len(left)>0 else 0

                if r1+l1+up_r+up_m+up_l+down_l+down_m+down_r == 2:                    

                    nums = []

                    if r1 ==1: 
                        nums.append(int(look_right(r,c,arr,cols)))
                        
                    if l1 == 1:
                        nums.append(int(look_left(r,c,arr)))
                    if up_r == 1:
                        nums.append(int(look_right(r-1,c,arr,cols)))
                    if up_m == 1:
                        nums.append(int(look_left(r-1,c,arr) + arr[r-1,c] +look_right(r-1,c,arr,cols)))
                    if up_l == 1:
                        nums.append(int(look_left(r-1,c,arr)))
                    if down_r == 1:
                        nums.append(int(look_right(r+1,c,arr,cols)))
                    if down_m == 1:
                        nums.append(int(look_left(r+1,c,arr) + arr[r+1,c] +look_right(r+1,c,arr,cols)))

                    if down_l == 1:
                        nums.append(int(look_left(r+1,c,arr)))
                    print(nums)
                    nums_list.append(nums[0]*nums[1])
            c+=1
        r+=1
    return sum(nums_list)


                


print(puzzle_one())
print(puzzle_two())