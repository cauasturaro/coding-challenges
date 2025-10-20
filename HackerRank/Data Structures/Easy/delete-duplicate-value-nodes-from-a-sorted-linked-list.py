# Problem: Delete a duplicated value from nodes in a linked list
# Platform: HackerRank
# Difficulty: Easy
# Link: https://www.hackerrank.com/challenges/delete-duplicate-value-nodes-from-a-sorted-linked-list/problem
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
#

def removeDuplicates(llist):
    node = llist
    while node and node.next:
        if node.data == node.next.data:
            node.next = node.next.next if node.next.next else None
        else:
            node = node.next
    return llist
