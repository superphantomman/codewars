from evaluate import calc

#write more tests and nested part do it and test --
if __name__ == "__main__":
    tests = [
        ("3*4-1",11), 
        ("3*4-12",0),
        ("1*2--3*1",5), 
        ("2+2", 4), ("3*4", 12),
             ("( 24/( 3*4 )*( 2+2 )--1 )+1",10), 
            ("-1*-1--1-1",1)
             ]

    for test in tests:
        try:
            assert calc ( test[0] ) == test[1]
            # print(test[0] + '=' + str (  calc ( test[0] ) ) )
        except AssertionError as e:
            print("------------")
            result = calc ( test[0] )
            print("------------")
            print( 
                f"""!!Assertion!!!\n{test[0]}\n{result} != {test[1]}""" )
            print("------------")


