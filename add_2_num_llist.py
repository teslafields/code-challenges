'''
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    base = 10
    def __init__(self):
        self.summed = ListNode(0)
        self.cur = self.summed

    def addTwoNumbers(self, l1, l2, c = 0):
        val1, val2 = 0, 0
        if l1 is not None:
            val1 = l1.val
            l1 = l1.next
        if l2 is not None:
            val2 = l2.val
            l2 = l2.next

        value = val1 + val2 + c
        if value >= self.base:
            c = int(value/self.base)
            value = value%self.base
        else:
            c = 0
        self.cur.val = value
        if l1 is None and l2 is None and c == 0:
            return self.summed

        self.cur.next = ListNode(0)
        self.cur = self.cur.next
        return self.addTwoNumbers(l1, l2, c)


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

sol = Solution()
result = sol.addTwoNumbers(l1, l2)
while result:
    print(result.val)
    result = result.next
# 7 0 8
