#https://leetcode.com/problems/friend-circles/submissions/
# https://www.educative.io/edpresso/the-friend-circle-problem
import numpy as np
class Solution(object):
    def DFS(self, friends, n, visited, v):
        for x in range(n):
          if friends[v][x] and visited[x] == 0:
            if x != v:
              visited[x] = 1
              self.DFS(friends, n, visited, x)

    def findCircleNum(self, friends):
        """
        :type friends: List[List[int]] :[[1,1,0],[1,1,0],[0,0,1]]
        :rtype: int
        """
        n = len(friends[0])
        if n==0:
          return 0

        numCircles = 0    # Number of friend circles
        visited = np.zeros((n))
        for i in range(n):
            if (visited[i] == 0):
                visited[i] = 1
                self.DFS(friends, n, visited, i) # Recursive step to find all friends
                numCircles = numCircles + 1

        return numCircles
