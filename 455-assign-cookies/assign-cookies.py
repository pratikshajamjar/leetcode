class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        child = 0
        cookie = 0
        
        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                # Cookie can satisfy the child
                child += 1
            # Move to the next cookie
            cookie += 1
        
        return child
