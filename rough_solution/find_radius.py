class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        j = 0
        minimum = 0
        for i in range(0, len(houses)):
            while j < len(heaters) - 1 and abs(heaters[j] - houses[i]) >= abs(heaters[j+1] - houses[i]):
                j += 1
            minimum = max(minimum, abs(heaters[j] - houses[i]))
        return minimum


if __name__ == '__main__':
    solution = Solution()
    houses = [1, 2, 3]
    heaters = [2]
    print(solution.findRadius(houses, heaters))
