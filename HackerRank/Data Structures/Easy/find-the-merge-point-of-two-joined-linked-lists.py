# Problem: Find the merge point of two joined linked lists
# Platform: HackerRank
# Difficulty: Easy
# Link: https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists/problem
# -----------------------------------------------------
# Time Complexity: O(n²)
# Space Complexity: O(1)
# -----------------------------------------------------

# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#

def findMergeNode(head1, head2):
    node1 = head1
    
    while node1:
        node2 = head2
        
        while node2:
            if node1 == node2:
                return node1.data 
                
            node2 = node2.next
        node1 = node1.next
    
    return None
        