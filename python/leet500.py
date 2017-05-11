firstrow = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
secondrow = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
thirdrow = ['z', 'x', 'c', 'v', 'b', 'n', 'm']
allrows = [firstrow, secondrow, thirdrow]
testCase = ["Hello","Alaska","Dad","Peace"]
class Solution(object):
    def ifInRow(self, word, row):
        for w in word:
            
            if w.lower() not in row:
                return False
        return True
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rList = list()
        if words is None:
            return None
        for word in words:
            for row in allrows:
                if self.ifInRow(word, row):
                    rList.append(word)
            
        return rList

sol = Solution()
output = sol.findWords(testCase)

print(output)
