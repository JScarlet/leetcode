class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        result = 0
        for each in zip(*A):
            for i in range(0, len(each) - 1):
                if each[i] > each[i+1]:
                    result += 1
                    break
        return result


if __name__ == '__main__':
    solution = Solution()
    A = ["a", "b"]
    print(solution.minDeletionSize(A))