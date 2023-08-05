from evaluate import calc

if __name__ == "__main__":
    tests = ["1+2*3*4-1"]
    for test in tests:
        print(f"{test}->{calc(test)}")



