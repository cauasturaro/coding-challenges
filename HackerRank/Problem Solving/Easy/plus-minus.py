# Problem: Plus Minus
# Platform: HackerRank
# Difficulty: Easy
# Link: https://www.hackerrank.com/challenges/plus-minus/problem
# -----------------------------------------------------
# Time Complexity: O(1)
# Space Complexity: O(1)
# -----------------------------------------------------
#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    positives = 0 
    negatives = 0
    zeros = 0
    
    for e in arr:
        if e == 0:
            zeros = zeros + 1
        elif e > 0:
            positives = positives + 1
        else:
            negatives = negatives + 1
    
    positives = round(positives/n, 6)
    negatives = round(negatives/n, 6)
    zeros = round(zeros/n, 6)
    
    print(f"{positives:.6f}\n{negatives:.6f}\n{zeros:.6f}")