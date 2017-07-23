class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        fst = 'qwertyuiopQWERTYUIOP'
        snd = 'asdfghjklASDFGHJKL'
        trd = 'zxcvbnmZXCVBNM'
        result =[]
        
        for word in words:
            count = 0
            for alpha in word:
                if alpha in fst: count = count | 1
                if alpha in snd: count = count | 2
                if alpha in trd: count = count | 4
            if count in [1,2,4]:
                result.append(word)
        return result
