class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        base = 0
        cmp = []

        for p in prices:
            cmp.append(p - base)
            base = p

        cmp = cmp[1:]
        if not cmp:
            return 0

        result = []
        tmp = 0
        for n in cmp:
            tmp += n
            if tmp < 0:
                tmp = 0
            result.append(tmp)

        return max(result)

    def test(self):
        result = self.maxProfit([1])
        print(result)


if __name__ == '__main__':
    Solution().test()
