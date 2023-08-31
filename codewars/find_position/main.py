from create_sample_data import create_data
from find_position import brute_find_position, find_position
import os

if __name__ == "__main__":
    
    filename = "data.txt"
    local_path = os.path.dirname(os.path.abspath(__file__))
    file_path = f"{local_path}/{filename}"
    
    try:
        if(os.path.getsize(file_path) == 0):
            create_data(file_path)
    except FileNotFoundError as e:
        create_data(file_path)
    

    # with open(file_path, "r") as f:
    #     data = f.read()
        
    #     tests = [
    #         "121","363", "0251", "12345","1112", "1122", "1011", 
    #              "4040", "112", "123456", "3901", "12123", "32324"
    #              , "123114", "123413", "8779", "863", "45674", "356","0404"
                 
    #              ]
        
    #     for test in tests:
    #         brute = brute_find_position(test, data)
    #         print(
    #             (f"""({brute},{"".join(data[brute:brute+len(test)])})""")
    #         )
        

    tests = [
 
        (13034,"53635"),

        # (6957586376885,"555899959741198"),
        # ( 35286, "09991") , 



        #  (1091,"040"), 
        # (0,"123456789"),
        # (0,"1234567891"),
        # (1000000071,"123456798"),
        # (9,"10"),
        # (13,"121"),
        # (61,"363"),
        # (641,"0251"), 
        # (15050, "0404" ),
        # (3, "456"),
        # (11,"11"),
        # (168, "99"), 
        # (0,"12345"),
        # (11,"1112"),
        # (254,"1122"),
        # (9,"1011"),
        # (15049,"4040"),
        # (12,"112"),
        # (0,"123456"),
        # (4450,"3901"),
        # (49504,"12123"),
        # (8184,"32324"),
        # (573630,"123114"),
        # (12539,"123413"),
        # (2225,"8779"),
        # (1048,"863"),
        # (17157,"45674"),
        # (957,"356")
    ]
 

    for test in tests:
        v = find_position(test[1])
        try:
            assert v == test[0]
        except AssertionError as e:
            print(f"for {test[1]}")
            print(f"{v} != {test[0]}") 

            with open( file_path, "r") as f:
                data = f.read()
                print("should be")
                print(
                    data
                    [ ( test[0]-len(test[1]) ) 
                     : ( test[0]+len(test[1]) * 2 ) 
                    ])
                print("not be")

                print(
                    data
                    [ ( v-len(test[1]) ) 
                     : ( v+len(test[1]) * 2 ) 
                    ])



# from itertools import permutations

# string = "5365"
# length = 4
# # 
# numbers = []

# for c in permutations(string, len(string)):
#     print("".join(c))


# print("Generated numbers:")
# for num in numbers:
#     print(num)
# # 