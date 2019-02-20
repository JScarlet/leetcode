class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        result = []
        flag = 0
        K = [int(num) for num in str(K)][::-1]
        A = A[::-1]
        if len(K) > len(A):
            long = K
            short = A
        else:
            long = A
            short = K
        for i in range(0, len(short)):
            temp = short[i] + long[i] + flag
            if temp >= 10:
                result.append(temp - 10)
                flag = 1
            else:
                flag = 0
                result.append(temp)
        for i in range(len(short), len(long)):
            temp = long[i] + flag
            if temp >= 10:
                result.append(temp - 10)
                flag = 1
            else:
                flag = 0
                result.append(temp)
        if flag == 1:
            result.append(flag)
        return result[::-1]


if __name__ == '__main__':
    solution = Solution()
    A = [1, 2, 0, 0]
    K = 34
    print(solution.addToArrayForm(A, K))
