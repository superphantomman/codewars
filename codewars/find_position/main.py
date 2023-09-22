from create_sample_data import create_data
from find_position import find_position
from time import time
import os

def main():

    filename = "data.txt"
    local_path = os.path.dirname(os.path.abspath(__file__))
    file_path = f"{local_path}/{filename}"
    
    try:
        if(os.path.getsize(file_path) == 0):
            create_data(file_path)
    except FileNotFoundError as e:
        create_data(file_path)
    

    tests = [

        (2228, "978"),
        (909, "340"),
        (6608, "9193"),
        (1017, "376"),
        (957,"356"), 
        (49504,"12123"), 
         (4450,"3901"),
        (573630,"123114"),
        (1048,"863"),
        (382689688, "949225100"),
        # (6957586376885,"555899959741198"),
        (1000000071,"123456798"),
        (190,"00"),
        ( 35286, "09991") ,
        (13034,"53635"),
         (1091,"040"), 
        (0,"123456789"),
        (0,"1234567891"),
        (9,"10"),
        (13,"121"),
        (61,"363"),
        (641,"0251"), 
        (15050, "0404" ),
        (3, "456"),
        (11,"11"),
        (168, "99"), 
        (0,"12345"),
        (11,"1112"),
        (254,"1122"),
        (9,"1011"),
        (15049,"4040"),
        (12,"112"),
        (0,"123456"),
        (8184,"32324"),
        (12539,"123413"),
        (2225,"8779"),
        (17157,"45674"),
        
    ]

  
    for _ in range(5):
        start_time = time()
        for test in tests:
            with open( file_path, "r") as f: data = f.read()
            result = find_position(test[1])
            try:
                assert result == test[0], f"{result} != {test[0]}"
                print(f"Passed\n{test[1]}")
            except AssertionError as e:
                print(f"Assertion failed for test {test[1]}\n{e}") 

                with open( file_path, "r") as f: data = f.read()
                n = len(test[1])
                print("should be located")
                print(
                    data[ (test[0] - n) : (test[0] + n * 2 )]
                )
                print("should not be")
                print(
                    data[ (result - n) : (result + n * 2) ]
                )
            except Exception as e:
                print(e)
            
        end_time = time()
        print(f"Elapsed time: {(end_time-start_time):.6f} seconds")


    return


if __name__ == "__main__":
    main()
