class Solution:
    def removeDuplicates(self, nums: list):
        """
        :type nums: List[int]
        :rtype: int
        """

        base = None
        rm_lst = []
        for n in nums:
            if isinstance(base, int):
                if n == base:
                    rm_lst.append(n)
            base = n

        for n in rm_lst:
            nums.remove(n)

        return len(nums)

    def test(self):
        result = self.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
        print(result)


if __name__ == '__main__':
    Solution().test()
