class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isValid(s):
            return s == s[::-1]
        
        def helper(s,left,right,curr):
            if left < right:
                if isValid(s[left:right]):
                    if right -left > len(curr):
                        curr = s[left:right]
                else:
                    helper(s,left,right-1,curr) 
                    helper(s,left+1,right,curr)
        
        curr = s[0]
        helper(s,0,len(s),curr)
        return curr
                

solution = Solution()

s = 'cbbd'
print(solution.longestPalindrome(s))