# Problem: Get The Value of The Node at a Specific position from the tail
# Platform: HackerRank
# Difficulty: Easy
# Link: https://www.hackerrank.com/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail/problem
# -----------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------------------

# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#

def getNode(llist, positionFromTail):
    node = llist
    prev = llist
    
    for _ in range(positionFromTail):
        node = node.next
    
    while node.next:
        prev = prev.next
        node = node.next
    
    return prev.data
        