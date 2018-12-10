class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image
        image[sr][sc] = newColor
        dimension = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        queue = [(sr, sc)]
        while len(queue) > 0:
            center_r, center_c = queue.pop(0)
            for i in range(0, len(dimension)):
                new_r = center_r + dimension[i][0]
                new_c = center_c + dimension[i][1]
                if 0 <= new_r < len(image) and 0 <= new_c < len(image[0]):
                    if image[new_r][new_c] == oldColor:
                        queue.append((new_r, new_c))
                        image[new_r][new_c] = newColor
        return image


if __name__ == '__main__':
    solution = Solution()
    image = [[0,0,0],[0,1,1]]
    sr = 1
    sc = 1
    newColor = 1
    print(solution.floodFill(image, sr, sc, newColor))
