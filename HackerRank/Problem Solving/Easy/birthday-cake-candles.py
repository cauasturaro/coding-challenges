# Problem: Count the ammount of tall candles
# Platform: HackerRank
# Difficulty: Easy
# Link: https://www.hackerrank.com/challenges/birthday-cake-candles/problem
# -----------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------------------

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    tallest = 0 
    count = 0
    for candle in candles:
        if candle == tallest:
            count = count + 1
        if candle > tallest:
            tallest = candle
            count = 1

    return count