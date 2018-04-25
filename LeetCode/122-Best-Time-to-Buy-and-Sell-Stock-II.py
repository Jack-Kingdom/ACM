class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        base = None
        expect = 0
        for p in prices:
            if isinstance(base, int):
                if p > base:
                    expect += p - base

            base = p

        return expect

    def test(self):
        result = self.maxProfit([2, 1, 2, 0, 1])
        print(result)


if __name__ == '__main__':
    Solution().test()
