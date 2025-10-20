# Problem: Compare Two Linked Lists
# Platform: HackerRank
# Difficulty: Easy
# Link:https://www.hackerrank.com/challenges/compare-two-linked-lists/problem
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

def compare_lists(llist1, llist2):
    while llist1 and llist2:
        if llist1.data != llist2.data:
            return 0
        llist1 = llist1.next
        llist2 = llist2.next
        
    if not llist1 and not llist2:
        return 1
    
    return 0
    