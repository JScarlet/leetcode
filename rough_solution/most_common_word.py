class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        comma_list = ['!', '?', "'", ',', ';', '.']
        paragraph = paragraph.lower()
        for each in comma_list:
            paragraph = paragraph.replace(each, ' ')
        word_list = paragraph.split()
        word_dict = {}
        for word in word_list:
            if word not in word_dict:
                word_dict[word] = 1
            else:
                word_dict[word] += 1

        sorted_word_list = sorted(word_dict.items(), key=lambda x:x[1], reverse=True)
        print(sorted_word_list)
        for each in sorted_word_list:
            if each[0] not in banned:
                return each[0]
        return None


if __name__ == '__main__':
    solution = Solution()
    paragraph = "a, a, a, a, b,b,b,c, c"

    banned = ["a"]
    print(solution.mostCommonWord(paragraph, banned))
