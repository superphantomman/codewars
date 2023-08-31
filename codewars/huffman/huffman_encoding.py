""" takes: str; 
    returns: [ (str, int) ] 
    (Strings in return value are single characters)
"""
def frequencies(s: str) -> list:

    d : dict = {} #dictionary storing count of each character

    for c in s:
        if c in d: d[c] += 1
        else: d[c] = 1

    return [(key, val) for key, val in d.items()]
"""
    takes: list[tuple[str, int]]
    returns: dict[str,str]
    (Dictionary with contains code and value)
"""
def build_dict(freqs : list[tuple[str, int]]) -> dict[str,str]:
    #Building huffman tree 
    class Node:
        def __init__(
                self, data : str , count : int, 
                left, right
                ) -> None: 
            self.data: str = data 
            self.count : int = count # count of repetition of each character or combine characters

            self.left = left
            self.right = right
        def __add__(self, other):
            return Node(
                self.data + other.data,
                self.count + other.count, 
                self, other
                )
        def __repr__(self) -> str:
            return f"{self.data} -> {self.count}"
        
    nodes : list = [ Node(x, y, None, None) for x, y in sorted(freqs, key=lambda e : e[1] ,reverse=True) ]

    while len(nodes) > 1 :

        #two smallest frequence nodes 
        n1 : Node = nodes.pop()
        n2 : Node = nodes.pop()
        node : Node = n1 + n2
        

        #index of place where should new node be located to be nodes in order
        index = next( 
            (i for i, v in enumerate(nodes) if v.count < node.count ), 
            None) 
        
        if index == None: index = -1
        

        nodes.insert(
            index,
            node)

    d = {}
    codes = [""]    #list holding incomplete codes    
    
    while len(nodes) > 0:
        n : Node = nodes.pop()
        c = codes.pop()
        
        l : Node = n.left
        r : Node = n.right

        if l != None:
            
            if len(l.data) == 1: d[l.data] = c + "0" 
            else: 
                nodes.append(l)
                codes.append(c + "0")
            
        if r != None:
            
            if len(r.data) == 1: d[r.data] = c + "1" 
            else: 
                nodes.append(r)
                codes.append(c + "1")
                
    return d


""" 
    takes: [ (str, int) ], str; 
    returns: String (with "0" and "1")
"""
def encode(freqs : list, s : str) -> str:

    if len(freqs) < 2: return None
    if len(s) == 0: return ""
    if len(freqs) < len(s): "" 

    d = build_dict(freqs)

    return "".join([d[c] for c in s ])      
                
"""
    takes [ [str, int] ], str (with "0" and "1"); 
    returns: str
"""
# 
def decode(freqs : list ,bits : str):

    if len(freqs) < 2: return None
    if bits == "": return ""
    
    
    result = [""]
    
    d = {}
    for key, val in build_dict(freqs).items(): d[val] = key

    buff : str = ""
    for bit in bits:
        buff += bit
        if buff in d: 
            result.append( d[buff] ) 
            buff = ""
    
    
    return "".join(result)