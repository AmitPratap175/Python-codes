"""
Author: Amit Pratap

You are given a string of digits from 0-9 as in a keyboard in a line
from start to end with the arrangent as provided by the string. Now we
want to calculate the minimum time in milliseconds to type a sequence 
of given digits. The minimum time is calculated as first starting at the 
zero-th index we have |a-b| milliseconds if the subsequent digits fall on 
a-th to b-th index.
"""
def calc_milli(string, match_string):
    # Precompute index positions for each digit
    index_map = {char: idx for idx, char in enumerate(string)}

    min_time = 0
    startIdx = 0  # Initially at the start of the keyboard

    for char in match_string:
        endIdx = index_map[char]  # Get index in O(1)
        min_time += abs(endIdx - startIdx)
        startIdx = endIdx  # Move to the new position

    return min_time


if __name__ == "__main__":
    string = "0192837465"
    string_out = "21"
    # expected_answer = 3
    print("Calculated:", calc_milli(string, string_out))#, "Expected:", expected_answer)
