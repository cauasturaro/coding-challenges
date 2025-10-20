# Problem: Insert a node at the tail of a linked list
# Platform: HackerRank
# Difficulty: Easy
# Link: https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/problem
# -----------------------------------------------------
# Time Complexity: O(n) q: 
# Space Complexity: O(1)
# -----------------------------------------------------

# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#

def insertNodeAtTail(head, data):
    node = head
    if not node:
        node = SinglyLinkedListNode(data)
        head = node
        return head
    
    while node.next:
        node = node.next
    newNode = SinglyLinkedListNode(data)
    node.next = newNode
    
    return head
     