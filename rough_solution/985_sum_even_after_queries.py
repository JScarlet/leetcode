class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        initial = 0
        for i in range(0, len(A)):
            if A[i] % 2 == 0:
                initial += A[i]

        result = []
        for i in range(len(queries)):
            val = queries[i][0]
            index = queries[i][1]
            mod_a = A[index] % 2
            mod_val = val % 2
            if mod_a == 0 and mod_val == 0:
                initial += val
            elif mod_a == 0 and mod_val == 1:
                initial -= A[index]
            elif mod_a == 1 and mod_val == 1:
                initial += A[index] + val
            A[index] += val
            result.append(initial)
        return result


if __name__ == '__main__':
    solution = Solution()
    A = [1, 2, 3, 4]
    queries = [[1, 0], [-3, 1], [-4, 0], [2, 3]]
    print(solution.sumEvenAfterQueries(A, queries))
