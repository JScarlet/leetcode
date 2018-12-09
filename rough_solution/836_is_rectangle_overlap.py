class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        center1 = [(rec1[0] + rec1[2])/2, (rec1[1] + rec1[3])/2]
        center2 = [(rec2[0] + rec2[2])/2, (rec2[1] + rec2[3])/2]
        if abs(center1[0] - center2[0]) < (abs(rec1[0] - rec1[2])/2 + abs(rec2[0] - rec2[2])/2) and abs(center1[1] - center2[1]) < (abs(rec1[1] - rec1[3])/2 + abs(rec2[1] - rec2[3])/2):
            return True
        return False


if __name__ == '__main__':
    solution = Solution()
    rec1 = [0, 0, 1, 1]
    rec2 = [1, 0, 2, 1]
    print(solution.isRectangleOverlap(rec1, rec2))
