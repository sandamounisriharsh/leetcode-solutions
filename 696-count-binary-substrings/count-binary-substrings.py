class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev=0
        curr=1
        c=0
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                curr+=1
            else:
                c+=min(prev,curr)
                prev=curr
                curr=1
        c+=min(prev,curr)
        return c