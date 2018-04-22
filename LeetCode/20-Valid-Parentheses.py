LEFT = ['(', '[', '{']
MAP = {
    '(': ')',
    '[': ']',
    '{': '}'
}


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        for char in s:
            if char in LEFT:
                stack.append(char)
            else:
                if stack:
                    if char == MAP[stack[-1]]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False  # stack lack left

        return len(stack) == 0

    def test(self):
        print(self.isValid("["))


if __name__ == '__main__':
    Solution().test()
