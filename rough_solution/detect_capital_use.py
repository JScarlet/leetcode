class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word[0].isupper():
            length = 0
            for letter in word[1:]:
                if letter.isupper():
                    length += 1
            if length == 0 or length == len(word) - 1:
                return True
            else:
                return False
        else:
            length = 0
            for letter in word:
                if letter.islower():
                    length += 1
            if length == len(word):
                return True
            return False


if __name__ == '__main__':
    solution = Solution()
    word = "USA"
    print(solution.detectCapitalUse(word))
