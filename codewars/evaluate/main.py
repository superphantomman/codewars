from evaluate import calc

if __name__ == "__main__":
    
    #each tuple contains sample expression with answer to it 
    tests = [
        ("3*4-1",11),("3*4-12",0),
        ("1*2--3*1",5),("2+2", 4), 
        ("3*4", 12),("( 24/( 3*4 )*( 2+2 )--1 )+1",10), 
        ("-1*-1--1-1",1)
    ]

    for test in tests:
        try:
            assert calc(test[0])==test[1]

        except AssertionError as e:
            result = calc(test[0])
            print("------------")
            print( 
                f"""!!Assertion Exception!!!\n{test[0]}\n{result} != {test[1]}""" )
            print("------------")


