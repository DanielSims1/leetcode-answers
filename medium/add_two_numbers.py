"""

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Constraints:

    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.

    
"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# try recursion
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ret_node = ListNode()
        left_val = 0
        right_val = 0

        if not (l1) and not (l2):
            return None
        if not l1:
            left_val = 0
            left_node = None
        else:
            left_val = l1.val
            left_node = l1.next
        if not l2:
            right_val = 0
            right_node = None
        else:
            right_val = l2.val
            right_node = l2.next

        total = right_val + left_val
        # if we ran out of values to add (end of linked list)
        if total == 0:
            return ret_node
        elif total < 10:
            ret_node.val = total
        else:
            ret_node.val = total - 10
            if left_node:
                left_node.val += 1

            elif right_node:
                right_node.val += 1
            else:
                left_node = ListNode(val=1)
        ret_node.next = self.addTwoNumbers(l1=left_node, l2=right_node)
        return ret_node


if __name__ == "__main__":
    s = Solution()

    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    # l1= ListNode(0)
    # l2 = ListNode(0)

    # l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    # l2 = ListNode(9, ListNode(9, ListNode(
    #     9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
    # solution [8,9,9,9,0,0,0,1]

    ans = s.addTwoNumbers(l1=l1, l2=l2)

    while ans != None:
        print(ans.val)
        ans = ans.next
