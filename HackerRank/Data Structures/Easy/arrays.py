# Problem: Reverse Array
# Platform: HackerRank
# Difficulty: Easy
# Link: https://www.hackerrank.com/challenges/arrays-ds/problem
# -----------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------------------

def reverseArray(a):
    current_left = 0
    current_right = len(a)-1
    while current_left < current_right:
        # swap
        temp = a[current_right]
        a[current_right] = a[current_left]
        a[current_left] = temp
        
        current_left = current_left + 1
        current_right = current_right - 1
        
    return a

