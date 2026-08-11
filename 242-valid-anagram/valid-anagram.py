class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict={}
        t_dict={}
        for i in range(0,len(s)):
            if len(s)!=len(t):
                return False
            s_dict[s[i]]=s_dict.get(s[i],0)+1
            t_dict[t[i]]=t_dict.get(t[i],0)+1
        if s_dict==t_dict:
            return True
        return False
