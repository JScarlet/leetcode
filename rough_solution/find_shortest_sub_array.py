class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_map = {}
        for each in nums:
            if each not in nums_map:
                nums_map[each] = 1
            else:
                nums_map[each] += 1
        sorted_nums = sorted(nums_map.items(), key=lambda x:x[1], reverse=True)
        max_degree = sorted_nums[0][1]

        temp_map = {}
        for each in sorted_nums:
            if each[1] == max_degree:
                temp_map[each[0]] = []

        for i in range(0, len(nums)):
            if nums[i] in temp_map:
                temp_map[nums[i]].append(i)

        # print(temp_map)
        for key in temp_map:
            temp_map[key] = temp_map[key][-1] - temp_map[key][0] + 1
        # print(temp_map)
        return sorted(temp_map.items(), key=lambda x:x[1])[0][1]


if __name__ == '__main__':
    solution = Solution()
    nums = [2]
    print(solution.findShortestSubArray(nums))


# 解题思路：
# 就是找出满足数组的度的数字第一次和最后一次出现的位置，然后相减取最小的。
# 超出时间限制一般是因为循环太多，需要修改成更节约时间的方法，比如这里是把每一个key的迭代转化成了遍历一遍数组然后存到字典里，对字典进行操作
