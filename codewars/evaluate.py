# Evaluate mathematical expression
# https://www.codewars.com/kata/52a78825cdfc2cfc87000005/train/python

#1+2*3*4-1

def calc(expression):
    

    inf : float = float("inf")
    expression.replace(" ", "") 
    expression+="+"

    a : float = inf
    result : float = 0

    i = 0 
    n: int = len( expression )
    op : str = '+'
    ops : set = set(['+', '-', '/', '*'])
    
#Correct multiplication problem

    while i <  n:
        if expression[i] in ops:
            match op:
                case "+":
                    print(f"{result}+={a}")
                    if a != inf: result += a
                    a = inf
                case "-":
                    print(f"{result}-={a}")
                    if a != inf: result -= a
                    a = inf
                case '/':
                    a /= float(d_str)
                case '*':
                    a *= float(d_str)
            i+=1
  

        d_str = ""
        while i < n and expression[i] not in ops:
            d_str += expression[i]
            i+=1
        if a == inf and d_str!="": 
            a = float(d_str)
 
            



         





    return result