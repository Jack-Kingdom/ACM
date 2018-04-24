# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if l1 and not l2:
            return l1
        if l2 and not l1:
            return l2
        if not l1 and not l2:
            return None

        if l1.val > l2.val:
            l1, l2 = l2, l1

        head = l1
        opt = head
        l1 = l1.next

        while l1 and l2:
            if l1.val < l2.val:
                opt.next = l1
                l1 = l1.next
            else:
                opt.next = l2
                l2 = l2.next
            opt = opt.next
        else:
            if l1:
                opt.next = l1
            if l2:
                opt.next = l2

        return head

    def array2lst(self, array: list):
        if array:
            head = None
            opt = None

            for x in array:
                if not head:
                    head = ListNode(x)
                    opt = head
                else:
                    opt.next = ListNode(x)
                    opt = opt.next
            return head
        else:
            return None

    def lst2array(self, lst: ListNode):

        opt = lst
        result = []
        while opt:
            result.append(opt.val)
            opt = opt.next
        return result

    def test(self):
        l1 = [1, 2, 4, 5]
        l2 = [1, 2, 3, 4]

        result_lst = self.mergeTwoLists(self.array2lst(l1), self.array2lst(l2))
        result_array = self.lst2array(result_lst)
        print(result_array)


if __name__ == '__main__':
    Solution().test()
