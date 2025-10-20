# Problem: Print a the elements of a linked list in reverse
# Platform: HackerRank
# Difficulty: Easy
# Link: https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list-in-reverse/problem
# -----------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(n) Because of the recursioon stack
# -----------------------------------------------------


# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#

def reversePrint(llist):
    if not llist.next:
        print(llist.data)
        return
    reversePrint(llist.next)
    print(llist.data)
    