from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right: return head
        
        dummy = head
        # get left pointer before part to reverse
        for _ in range (1,left-1):
            dummy = dummy.next
        
        before = dummy
        print(f"before val {before.val}")
        end = dummy.next
        print(f"end val {end.val}")
        
        start = before
        for i in range (left-1,right):
            start = start.next
        if start:
            print(f"start val {start.val}")
            after = start.next
            if after:
                print(f"after val {after.val}")
        else:
            after = None
            print("after val None")
            print("after val None")

        
        before.next = start
        i = left -1
        while end and i <right:
            next_node = end.next
            end.next = after
            after = end
            end = next_node
            i+=1
        return head


s = Solution()

head = ListNode(3,ListNode(5))
left =1
right = 2
ans = s.reverseBetween(head,left,right)
while ans:
    print(ans.val)
    ans = ans.next