class Solution:
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        word_index_dict = {}
        for word in words:
            temp = []
            for letter in word:
                temp.append(order.find(letter))
            word_index_dict[word] = temp

        for i in range(0, len(words) - 1):
            left = word_index_dict[words[i]]
            right = word_index_dict[words[i+1]]
            length = min(len(left), len(right))
            m = 0
            while m < length:
                if left[m] < right[m]:
                    break
                elif left[m] == right[m]:
                    m += 1
                else:
                    return False
            if len(left) > len(right) and right == left[:len(right)]:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    words = ["kuvp","q"]

    order = "ngxlkthsjuoqcpavbfdermiywz"
    print(solution.isAlienSorted(words, order))
