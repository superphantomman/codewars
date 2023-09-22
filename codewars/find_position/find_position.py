from collections import deque
# https://www.codewars.com/kata/582c1092306063791c000c00/train/python


def find_position(string):

    #tracking visited guesses to avoid repetitions in guessing 
    visits : set = set()
    
    length = len(string)
    mv : int = 0    # how much move potentiall value 

    #combinations with potentially solutions
    buff1 : deque = deque()
    buff2 : deque = deque()

    for i in range(length):
        buff1.append(string[i])
        buff2.append(string[:i] + string[i+1::])

    border_max = int(string) if string[0] != "0" else int("1" + string)
    
    #reduce size of the border_max to reduce guesses for larger number
    if border_max > 1000_000:
        i = len(str(border_max))
        border_max //= 10 ** (i //7)
    
    c1 : str = str( ( int(string[-1] ) - 1 ) % 10 )
    c2 : str = str( ( int(string[0] ) + 1) % 10 )

    guess = ""
    min_guess_val = float("inf")
    count_to_close = length  

    while len(buff1) != 0:
        v1 = buff1.pop()
        v2 = buff2.pop()
        
        if int(v1) > border_max:
            continue
        if min_guess_val < int(v1): 
            if count_to_close == 0:  break
            count_to_close -= 1
            continue

        guesses = [v1]

        #adding end for potenial guess with extra digit
        if len(v1) > length - 2:
            if int(v1 + c1) <= border_max:  guesses.append(v1 + c1)
            if int(c1 + v1) <= border_max:  guesses.append(c1 + v1)
            if int(c2 + v1) <= border_max:  guesses.append(c2 + v1 )
            if int(v1 + c2) <= border_max:  guesses.append(v1 + c2)

        if v1 not in visits:

            for x in guesses:
                if x[0] == "0": continue
                v = int(x)
                if min_guess_val < v: continue
                v_copy = v

                left = 0
                neig : list[str] = []    
                i = length 

                while i > 0 and v > 1:
                    v -= 1
                    vl = str(v)
                    left += len(vl)
                    neig.append(vl) 
                    i -= 1

                v = v_copy
                i = length 
                
                neig = neig[::-1] + [x] 

                while i > 0:
                    v += 1
                    neig.append(str(v))
                    i -= 1 

                mv_val = ("".join(neig)).find(string)

                if mv_val != -1:
                    guess = x
                    min_guess_val = v_copy
                    mv = mv_val - left
                    count_to_close = len(buff1) * 3
            else:
                visits.add(v1)
                
        for i in range(len(v2)):
            buff1.append(v1+v2[i])
            buff2.append(v2[:i]+v2[i+1::])
            
    visits.clear()
    buff1.clear()
    buff2.clear()
    
    if guess == "":
        guess = string

    v = int(guess)  #value of guess
    SIZE = len(guess)
    count = SIZE
    decimal = 1
    poz = 0

    while count > 1: 
        poz += 9 * decimal * (SIZE - count + 1) 
        decimal *= 10
        count -= 1
    if v > 9:
        poz += (v- 10**(SIZE-1) ) * (SIZE)
    else:
        poz += v - 1
    return poz + mv


