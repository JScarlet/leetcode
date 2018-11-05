class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        empty_place = []
        temp = 0
        for i in range(0, len(flowerbed)):
            if flowerbed[i] == 0:
                temp += 1
            else:
                empty_place.append(temp)
                temp = 0
        empty_place.append(temp)

        if flowerbed[0] == 0:
            empty_place[0] += 1
        if flowerbed[-1] == 0:
            empty_place[-1] += 1

        result = 0
        for i in range(0, len(empty_place)):
            if empty_place[i] > 2:
                result += (empty_place[i] - 1) // 2
        if result >= n:
            return True
        return False


if __name__ == "__main__":
    solution = Solution()
    flowerbed = [0]
    n = 1
    print(solution.canPlaceFlowers(flowerbed, n))
    

# 解题思路：
# 统计每两个1之间的0的个数，每两个1之间能种花的数量就是0的数量减1除以2
# 注意如果两端不是1开始的话两端的0的数量要+1
