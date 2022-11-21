# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        sbj=head
        track=[]
        if sbj != None:
            while sbj.next != None:
                if sbj.next in track:
                    return True
                else:
                    track.append(sbj)
                    sbj=sbj.next
                    

        return False