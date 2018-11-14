class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine = list(magazine)
        for i in range(0, len(magazine)):
            word = magazine.pop()
            if word in ransomNote:
                ransomNote = ransomNote.replace(word, '', 1)
        if ransomNote == '':
            return True
        return False


if __name__ == '__main__':
    solution = Solution()
    ransomNote = 'aa'
    magazine = 'aab'
    print(solution.canConstruct(ransomNote, magazine))
