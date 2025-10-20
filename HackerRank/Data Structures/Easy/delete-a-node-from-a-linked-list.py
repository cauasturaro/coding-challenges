# Problem: Delete a node in a linked list
# Platform: HackerRank
# Difficulty: Easy
# Link: https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list/problem
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

def deleteNode(llist, position):
    if position == 0:
        return llist.next
        
    node = llist
        
    counter = 0
    while counter < position - 1:
        node = node.next
        counter = counter + 1
    
    if node.next.next is not None:
        node.next = node.next.next
    else:
        node.next = None
        
    return llist