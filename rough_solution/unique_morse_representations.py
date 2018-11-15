class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse_list = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        result = set()
        for word in words:
            morse = ''
            for letter in word:
                morse += morse_list[ord(letter) - ord('a')]
            result.add(morse)
        return len(result)


if __name__ == '__main__':
    solution = Solution()
    words = ["gin", "zen", "gig", "msg"]
    print(solution.uniqueMorseRepresentations(words))
