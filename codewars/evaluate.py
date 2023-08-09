# Evaluate mathematical expression
# https://www.codewars.com/kata/52a78825cdfc2cfc87000005/train/python

#1+2*3*4-1

def calc(expression):
    

    inf : float = float("inf")
    ex : str = expression.replace(" ", "") 
    ex = ex.replace("--", "+")
    ex = ex.replace("++", "+")
    ex = ex.replace("+-", "-")
    ex = ex.replace("-+", "-")

    expression+="+"

    buff1 : float = inf; buff2 : float = inf
    result : float = 0

    i = 0 
    n: int = len( ex )
    op : str = '+'
    op2 = ""
    ops : set = set(['+', '-', '/', '*'])
    
#Correct multiplication problem
    print (f"ex={ex}")

    while i <  n:
        if ex[i] not in ops:
            

            
            #dealing with brackets in string
            if(ex[i] == '('):
                sub_ex : str=""
                depth : int = 1
                i+=1
                while depth != 0:


                    print(f"{depth}->{sub_ex}")
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




            if buff1 == inf: buff1 = float( d )
            else: buff2 = float( d )
            continue
        
        if op2 != "":
            match op2:
                case "*":
                    # print(f"{buff1}*={buff2}") 
                    buff1*=buff2
                case "/": 
                    # print(f"{buff1}/={buff2}") 
                    buff1/=buff2
                    
            op2=""
            buff2==inf

        if ex[i] == '+' or ex[i] == '-':
            match op:
                case '+':
                    # print(f"{result}+={buff1}")
                    result += buff1
                    
                case '-':
                    # print(f"{result}-={buff1}")
                    result -= buff1
            buff1 = inf
            buff2 = inf
            op = ex[i]
            op2 = ''
        else:
            op2 = ex[i]
        i+=1
        
            
    if op2 != "":
        match op2:
            case "*": buff1*=buff2
            case "/": buff1/=buff2

    # print(f"buff1={buff1}")
    match op:
        case '+': result+=buff1
        case '-': result-=buff1    

    print(f"result:{result}")

    return result