# Problem: Merge Two Sorted Linked Lists
# Platform: HackerRank
# Difficulty: Easy
# Link: https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists/problem
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

def mergeLists(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1 
        
    if  head1.data <= head2.data:        
        head3 = head1 
        node1 = head1.next
        node2 = head2
    else:
        head3 = head2
        node1 = head1
        node2 = head2.next

    node3 = head3
            
    while node1 and node2:
        if node1.data <= node2.data:
            node3.next = node1 
            node1 = node1.next
        else:
            node3.next = node2
            node2 = node2.next
        
        node3 = node3.next 
        
    node3.next = node1 if node1 else node2
    
    return head3
    
    