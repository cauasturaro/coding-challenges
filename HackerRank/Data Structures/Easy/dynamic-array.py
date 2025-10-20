# Problem: Dynamic Array using queries
# Platform: HackerRank
# Difficulty: Easy
# Link: https://www.hackerrank.com/challenges/dynamic-array/problem
# -----------------------------------------------------
# Time Complexity: O(n + q) q: query ammount
# Space Complexity: O(n + e)  e: ammount of elements (when we get into type 1 queries)
# -----------------------------------------------------

def dynamicArray(n, queries):
    lastAnswer = 0
    arr = [[] for _ in range(n)]
    answers = []
    
    for q in queries:
        idx = (q[1] ^ lastAnswer) % n
        if q[0] == 1:
            arr[idx].append(q[2])
        if q[0] == 2:
            arr_size = len(arr[idx])
            eidx = q[2] % arr_size
            
            lastAnswer = arr[idx][eidx]            
            answers.append(lastAnswer)
            
    return answers