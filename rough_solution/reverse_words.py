class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        word_list = s.split()
        for i in range(0, len(word_list)):
            word_list[i] = word_list[i][::-1]
        return ' '.join(word_list)


if __name__ == '__main__':
    solution = Solution()
    s = "Let's take LeetCode contest"
    print(solution.reverseWords(s))
