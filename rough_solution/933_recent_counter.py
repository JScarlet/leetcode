class RecentCounter:

    def __init__(self):
        self.count_list = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.count_list.append(t)
        while self.count_list[0] < t-3000:
            self.count_list.pop(0)
        return len(self.count_list)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)