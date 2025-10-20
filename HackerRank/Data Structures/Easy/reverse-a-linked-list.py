# Problem: Reverse a linked list
# Platform: HackerRank
# Difficulty: Easy
# Link: https://www.hackerrank.com/challenges/reverse-a-linked-list/problem
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

def reverse(llist):
    prev = None
    node = llist 
    while node:
        nextNode = node.next
        node.next = prev
        prev = node
        node = nextNode
    return prev