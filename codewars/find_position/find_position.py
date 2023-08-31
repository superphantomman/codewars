# https://www.codewars.com/kata/582c1092306063791c000c00/train/python

def find_position(string):

    guesses : set = set()
    mv : int = 0    # how much moves potentiall value 

    #combinations with potentially solutions
    buff = [""]
    buff_index = [0]

    while len(buff) != 0:
        v = buff.pop()
        i = buff_index.pop()

        if i != len(string) - 1:
            buff.append(v)
            buff_index.append(i+1)
            buff.append(v+string[i])
            buff_index.append(i+1)
        else: 
            guesses.add(v+string[i])

    #adding end for potenial guess
    c : str
    if string[-1] == "0":
        c = "9"
    else:
        c = str( int(string[-1]) - 1 )


    for i in range(len(string)):
        v = string[i]
        for j in range(i+1, len(string)):
            guesses.add(v)
            v += string[j]
        for j in range(0, i):
            v += string[j]
            guesses.add(v)

        guesses.add(c + string[0:i])

    guesses = list(guesses)
    print(guesses)

    #filter to only good guess
    guess = ""
    min_guess_val = float("inf")

    for x in guesses:

        if x[0] == "0":  continue

        v = int(x)
        l,r = 0,0
        neig : list[str] = []    #neighbors of x including x
        i = len(string)

        while i > 0 and v > 1:
            v -= 1
            vl = str(v)
            l += len(vl)
            neig.insert(0,vl)
            i -= 1

        v = int(x)
        i = len(string)

        neig.append(x)

        while i > 0:
            
            v += 1
            vr = str(v)
            r += len(vr)
            neig.append(vr)
            i -= 1

        val = "".join(neig)
        
        if string in val and min_guess_val > int(x):   
            guess = x
            min_guess_val = int(x)
            mv = val.find(string) - l 

    #calculate position in string

    v = int(guess)  #value of guess
    count = len(guess)
    decimal = 1
    poz = 0
    i = 1

    while count > 1: 
        poz += 9 * decimal * i 
        i += 1
        decimal *= 10
        count -= 1

    if v > 9:
        poz += (v- 10**(len(guess)-1) ) * (len(guess))
    else:
        poz += v - 1
    return poz + mv


def brute_find_position(string : str, data : str) -> int:
    buff : str = [str(i) for i in range(0, len(string))]
    i : int = len(string) - 1
    
    while buff != string:
        
        buff.pop(0)
        buff.append(data[i])

        if "".join(buff) == string:
            break
        i += 1

    if i == len(data):
            return -1

    return i - len(string) + 1