class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs :
            return ""
        
        else :
            short = min(strs, key=len)
            strs.remove(short)
            
            for i in range(len(strs)):
                for j in range(len(short)):
                    if(short[j]!=strs[i][j]):
                        short=short[:j]
                        break

        return short
