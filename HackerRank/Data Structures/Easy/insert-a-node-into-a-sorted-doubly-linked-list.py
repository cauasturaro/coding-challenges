# Problem: Insert a node into a sorted doubly linked list
# Platform: HackerRank
# Difficulty: Easy
# Link: https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list/problem
# -----------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------------------

# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#

def sortedInsert(llist, data):
    newNode = DoublyLinkedListNode(data) 
    node = llist
    
    if not node:
        return newNode
    
    if newNode.data <= node.data:
        newNode.next = node 
        node.prev = newNode
        return newNode
        
    while node.next and node.next.data < newNode.data:
        node = node.next
        
    newNode.next = node.next 
    newNode.prev = node
    node.next = newNode
    
    return llist
