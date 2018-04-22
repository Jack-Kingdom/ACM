class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        num = 0
        char = None

        if not strs:
            return ''

        while True:
            for string in strs:

                if num == len(string):
                    return string

                if char:
                    if char != string[num]:
                        return string[:num]
                else:
                    char = string[num]

            num += 1
            char = None

    def test(self):
        print(self.longestCommonPrefix(["flower", "flow", "flight"]))


if __name__ == '__main__':
    Solution().test()
