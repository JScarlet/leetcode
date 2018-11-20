class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        A_list = A.split()
        B_list = B.split()
        A_set = set(A_list)
        B_set = set(B_list)
        temp_set = (A_set|B_set) ^ (A_set&B_set)
        extra = set()
        for each in temp_set:
            if A_list.count(each) > 1 or B_list.count(each) > 1:
                extra.add(each)
        return list(temp_set^extra)


if __name__ == '__main__':
    solution = Solution()
    A = "this apple is sweet"
    B = "this apple is sour"
    print(solution.uncommonFromSentences(A, B))
