# Problem: Print all elements of a linked list
# Platform: HackerRank
# Difficulty: Easy
# Link: https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list/problem
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

def printLinkedList(head):
    node = head
    while node:
        print(node.data)
        node = node.next
