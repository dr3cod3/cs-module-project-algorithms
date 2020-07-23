#!/usr/bin/env python3
'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    no_duplicate = set()
    for elem in arr:
        if arr[elem] in no_duplicate:
            no_duplicate.remove(arr[elem])
        else:
            no_duplicate.add(arr[elem])
            only_num = list(no_duplicate)[0]
    return only_num
    # Your code here


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
