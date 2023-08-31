#!/bin/env python3
from huffman_encoding import frequencies, encode, decode
from random_string import generate_random_string
from time import time


if __name__ == "__main__":


    sample_test = [ generate_random_string(100) for _ in range(10000) ] 

    
    start_time = time()
    for sample in sample_test:
        fs : list = frequencies(sample) 
        try:
            assert decode(fs,encode(freqs=fs, s=sample)) == sample     
        except AssertionError as e:
            print("assertion")
            print(f"{decode(fs,encode(freqs=fs, s=sample))} != {sample}")

    end_time = time()

    print(f"Elapsed time: {(end_time-start_time):.6f} seconds")


    s = "aaaabcc"
    fs = frequencies(s)

    execption_test = (
        (encode(fs, []), ''),
        (decode(fs, []), ''),
        (encode([], ""), None),
        ( decode( fs, "" ), ""),
        (encode( [], "" ), None),
        (decode( [], "" ), None),
        (encode( [('a', 1)], "" ), None ),
        (decode( [('a', 1)], "" ), None )

    )

    i = 1
    for val, expected in execption_test:
        try:
            assert val == expected
        except AssertionError as e:
            print(f"{i}. {val} != {expected}")
        i+=1
