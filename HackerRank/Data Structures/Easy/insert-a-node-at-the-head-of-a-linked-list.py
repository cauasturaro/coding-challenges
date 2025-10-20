# Problem: Insert a node at the head of a linked list
# Platform: HackerRank
# Difficulty: Easy
# Link: https://www.hackerrank.com/challenges/insert-a-node-at-the-head-of-a-linked-list/problem
# -----------------------------------------------------
# Time Complexity: O(1)
# Space Complexity: O(1)
# -----------------------------------------------------

# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtHead(llist, data):
    node = llist
    llist = SinglyLinkedListNode(data) 
    llist.next = node
    return llist

     