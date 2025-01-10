from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    @staticmethod
    def create_node_from_list(nums: List[int]):
        head = ListNode(nums[0])

        next_head = head
        for value in nums[1:]:
            next_head.next = ListNode(value)
            next_head = next_head.next

        return head

    def __str__(self) -> str:
        return str(self.val)

    def __repr__(self) -> str:
        return str(self.val)

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        pass
    
    def reverseFirstK(self, head, k):
        if k <= 1:
            return head

        if head.next == None:
            return head

        new_tail = head.next
        new_head = self.reverseFirstK(head.next, k-1)

        next_head = new_tail.next
        head.next = next_head
        new_tail.next = head
        return new_head

def main():
    head = ListNode.create_node_from_list([1,2,3,4,5])

    solution = Solution()
    head = solution.reverseFirstK(head, 1)
    import ipdb;ipdb.set_trace()
    
# python 算法/算法题/链表/25.K组反转.py
 
if __name__ == "__main__":
    main()

