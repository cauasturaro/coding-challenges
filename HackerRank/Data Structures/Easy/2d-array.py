# Problem: Find the maximum hourglass sum
# Platform: HackerRank
# Difficulty: Easy
# Link: https://www.hackerrank.com/challenges/2d-array/problem
# -----------------------------------------------------
# Time Complexity: O(n) Because we have a size-fixed matrix (4, 4)
# Space Complexity: O(1)
# -----------------------------------------------------

def hourglassSum(arr):
    sum = -63
    for i in range(4):
        for j in range(4):
            temp_sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            sum = max(temp_sum, sum)
    return sum
