from evaluate import calc

#write more tests and nested part do it and test --
if __name__ == "__main__":
    tests = [("3*4-1",11), ("3*4-12",0),("1*2--3*1",5), ("2+2", 4), ("3*4", 12),
             ("( 24/( 3*4 )*( 2+2 )--1 )+1",10)
             ]

    for test in tests:
        assert calc ( test[0] ) == test[1]



