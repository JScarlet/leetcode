class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        while i < m + j and j < n:
            if nums1[i] > nums2[j]:
                nums1.pop(-1)
                nums1.insert(i, nums2[j])
                j += 1
            else:
                i += 1
        if i == m + j:
            for a in range(m+j, m+n):
                nums1[a] = nums2[a - m]
        print(nums1)


if __name__ == '__main__':
    solution = Solution()
    nums1 = [-1, 0, 0, 3, 3, 3, 0, 0, 0]
    m = 6
    nums2 = [1, 2, 2]
    n = 3
    solution.merge(nums1, m, nums2, n)


# 解题思路：
# 同时遍历nums1和nums2，如果nums1的元素比nums2大，删去nums1的最后一位，将nums2的元素插入nums1中，
# 最后将nums2中剩余元素插入nums1的最后，这里对nums2中的元素已经全部插入nums1同样适用