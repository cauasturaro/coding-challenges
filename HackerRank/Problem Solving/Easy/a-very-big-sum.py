# Problem: A very big sum (since i made it in python, i didn't have to worry about int size)
# Platform: HackerRank
# Difficulty: Easy
# Link: https://www.hackerrank.com/challenges/a-very-big-sum/problem
# -----------------------------------------------------
# Time Complexity: O(1)
# Space Complexity: O(1)
# -----------------------------------------------------

#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#

def aVeryBigSum(ar):
    total_sum = 0
    for e in ar:
        total_sum = total_sum + e 
    return total_sum
    