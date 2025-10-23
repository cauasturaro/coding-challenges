# Problem: Mini-Max Sum
# Platform: HackerRank
# Difficulty: Easy
# Link: https://www.hackerrank.com/challenges/mini-max-sum/problem
# -----------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------------------

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    largest = arr[0]
    smallest = arr[0]
    total = 0

    for e in arr:
        if e > largest:
            largest = e
        if e < smallest:
            smallest = e
        total = total + e