
from functools import cache 
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m=len(s)
        n=len(p)

        @cache
        def dfs(i,j):
            if j==n:
                return i==m
            
            match=(i<m and (s[i]==p[j] or p[j]=='.'))

            if j+1<n and p[j+1]=='*':
                if dfs(i,j+2):
                    return True
                if match and dfs(i+1,j):
                    return True
                return False

            if match:
                return dfs(i+1,j+1)
            return False
        return dfs(0,0)
        