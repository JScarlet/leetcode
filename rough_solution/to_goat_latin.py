class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowel_list = ['a', 'e', 'i', 'o', 'u']
        word_list = S.split()
        new_word_list = []
        for i in range(0, len(word_list)):
            temp = ''
            if word_list[i][0].lower() in vowel_list:
                temp += (word_list[i] + 'ma')
            else:
                temp += (word_list[i][1:] + word_list[i][0] + 'ma')
            for j in range(0, i+1):
                temp += 'a'
            new_word_list.append(temp)
        return ' '.join(new_word_list)


if __name__ == '__main__':
    solution = Solution()
    S = "I speak Goat Latin"
    print(solution.toGoatLatin(S))
