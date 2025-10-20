# Problem: Rotate array elments to the left
# Platform: HackerRank
# Difficulty: Easy
# Link: https://www.hackerrank.com/challenges/array-left-rotation/problem
# -----------------------------------------------------
# Time Complexity: O(n) 
# Space Complexity: O(1)
# -----------------------------------------------------

def rotateLeft(d, arr):
    n = len(arr)
    rotate = d % n
    temp_arr = []
    for i in range(rotate):
        temp_arr.append(arr[i])
        
    for i in range(rotate, n):
        arr[i-rotate] = arr[i]
    
    for i in range(n - rotate, n):
        arr[i] = temp_arr[i - (n-rotate)]
    
    return arr
    