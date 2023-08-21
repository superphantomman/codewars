# Evaluate mathematical expression
# https://www.codewars.com/kata/52a78825cdfc2cfc87000005/train/python

#1+2*3*4-1


#change the way that -1 is treated as normal decimal

def calc(expression):
    

    inf : float = float("inf")
    ex : str = expression.replace(" ", "") 
    ex = ex.replace("--", "+")
    ex = ex.replace("++", "+")
    ex = ex.replace("+-", "-")
    ex = ex.replace("-+", "-")


    buff1 : float = inf; buff2 : float = inf
    result : float = 0

    i = 0 
    n: int = len( ex )
    op : str = '+'
    op2 = ""
    ops : set = set(['+', '/', '*', '-'])
    


    while i <  n:


        
        if buff1 != inf and buff2 != inf:
            if op2 != '':
                match op2:
                    case '*': buff1 *= buff2
                    case '/': buff1 /= buff2

                buff2 = inf
                op2 = ''
            else:
                result+= buff1
                buff1=buff2
                buff2=inf

            

        if ex[i] == '/' or ex[i] == '*':
            op2 = ex[i]
        





        if ex[i] not in ops or ex[i] == '-':

            
            #dealing with number less than 0
            neg : int = 1
            if ex[i] == '-':
                neg=-1
                i+=1
            
            #dealing with brackets in string
            if(ex[i] == '('):
                sub_ex : str=""
                depth : int = 1
                i+=1
                while depth != 0:

                    if ex[i] == '(': depth+=1
                    elif ex[i] == ')': depth-=1
                    sub_ex += ex[i] 
                    i+=1
                

                d=calc(sub_ex[:-1])
            #dealing with numbers from string
            else:    
                d = ""
                while i < n and ex[i] not in ops: 
                    d+=ex[i] 
                    i+=1

                if d == "": continue



            if buff1 == inf: buff1 = float( d ) * neg
            else: buff2 = float( d ) * neg


            
            continue
        


        i+=1
        

    if op2 != "":
        match op2:
            case "*": buff1*=buff2
            case "/": buff1/=buff2
        buff2 = inf

    if buff2 != inf:
        buff1+=buff2

    return result+buff1 