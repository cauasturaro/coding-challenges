# Problem: Compare the Triplets
# Platform: HackerRank
# Difficulty: Easy
# Link: https://www.hackerrank.com/challenges/compare-the-triplets/problem
# -----------------------------------------------------
# Time Complexity: O(1)
# Space Complexity: O(1)
# -----------------------------------------------------

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    resultsA = 0
    resultsB = 0
    
    for i in range(3):
        if a[i] > b[i]:
            resultsA = resultsA + 1
        elif a[i] < b[i]:
            resultsB = resultsB + 1
            
    results = [0, 0]
    
    results[0] = resultsA
    results[1] = resultsB
            
    print(results)
    return results