# Problem: Insert a node at a specific position in a linked list
# Platform: HackerRank
# Difficulty: Easy
# Link: https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem
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

def insertNodeAtPosition(llist, data, position):
    counter = 0 
    node = llist
    
    while counter < position - 1:
        node = node.next
        counter = counter + 1
        
    nextNode = node.next
    newNode = SinglyLinkedListNode(data) 
    node.next = newNode
    newNode.next = nextNode
    
    return llist
    
     