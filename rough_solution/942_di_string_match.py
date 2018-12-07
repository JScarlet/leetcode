class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        length = len(S)
        num_list = [i for i in range(0, length+1)]
        result = []
        for letter in S:
            if letter == 'I':
                result.append(num_list.pop(0))
            else:
                result.append(num_list.pop())
        result.append(num_list.pop())
        return result


if __name__ == '__main__':
    solution = Solution()
    S = 'DDI'
    print(solution.diStringMatch(S))
