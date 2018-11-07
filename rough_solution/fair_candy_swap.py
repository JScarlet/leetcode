class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        total_A = sum(A)
        total_B = sum(B)
        total = total_A + total_B
        average = total // 2
        diff = average - total_A

        map_A = {}
        for each in A:
            if each not in map_A:
                map_A[each] = 1
            else:
                map_A[each] += 1

        map_B = {}
        for each in B:
            if each not in map_B:
                map_B[each] = 1
            else:
                map_B[each] += 1

        for key in map_A:
            if key + diff in map_B:
                return [key, key+diff]
        return [0, 0]


if __name__ == '__main__':
    solution = Solution()
    A = [2, 1]
    B = [2, 3]
    print(solution.fairCandySwap(A, B))

# 解题思路：
# 求出平均大小，然后用平均大小减去自己拥有糖果的总和，这个差值就是你换回来的和你换出去的差值
