class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == [""]:
            return ""
        base = strs[0]
        result = ""
        for i in range(0,len(base)):
            for word in strs[1:]:
                if i==len(word) or word[i] != base[i]:
                    return result
            result += base[i]
        return result