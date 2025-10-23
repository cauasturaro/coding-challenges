# Problem: Diagonal Absolute Difference 
# Platform: HackerRank
# Difficulty: Easy
# Link: https://www.hackerrank.com/challenges/diagonal-difference/problem
# -----------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------------------

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    left_diagonal_sum = 0
    right_diagonal_sum = 0
    
    size = len(arr[0])
    
    for i in range(size):
        left_diagonal_sum = left_diagonal_sum + arr[i][i]
    j = -1
    for i in range(size - 1, -1, -1):
        j = j + 1
        right_diagonal_sum = right_diagonal_sum + arr[i][j]
        
    abs_difference = left_diagonal_sum - right_diagonal_sum 
    abs_difference = abs_difference * -1 if abs_difference < 0 else abs_difference

    return abs_difference
    return results