# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return '[' + str(self.start) + ', ' + str(self.end) + ']'

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 1:
            return intervals
        sorted_intevals = sorted(intervals, key=lambda x:x.start)

        result = []
        old = sorted_intevals[0]
        right = 1
        while right < len(sorted_intevals):
            if old.end >= sorted_intevals[right].start:
                old.start = min(old.start, sorted_intevals[right].start)
                old.end = max(old.end, sorted_intevals[right].end)
            else:
                result.append(old)
                old = sorted_intevals[right]
            right += 1
        result.append(old)
        return result


if __name__ == '__main__':
    solution = Solution()
    input = [[1,3],[2,6],[8,10],[15,18]]
    intervals = []
    for i in range(len(input)):
        intervals.append(Interval(input[i][0], input[i][1]))
    result = solution.merge(intervals)
    for each in result:
        print(each)