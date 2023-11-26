class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        strs = sorted(strs)

        f = strs[0]
        l = strs[-1]

        for i in range(min(len(f), len(l))):
            if f[i]!=l[i]:
                return ans
            ans += f[i]
        return ans


'''
Alternate solution

ans = ""
for i in range(len(strs[0])):
    for s in strs:
        if i == len(s) or s[i] != strs[0][i]:
            return ans
    ans+=strs[0][i]

return ans
'''
