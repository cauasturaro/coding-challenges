# Problem: Simple array sum
# Platform: HackerRank
# Difficulty: Easy
# Link: https://www.hackerrank.com/challenges/simple-array-sum/problem
# -----------------------------------------------------
# Time Complexity: O(1)
# Space Complexity: O(1)
# -----------------------------------------------------

def simpleArraySum(ar):
    total_sum = 0
    for e in ar:
        total_sum = total_sum + e 
    return total_sum