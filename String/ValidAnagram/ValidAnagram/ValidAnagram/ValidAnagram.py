# anagram : 알파벳의 순서를 바꿔서 다른 알파벳 만들기

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        '''
        # Approach1: (44ms, 14.8 MB)
        s=sorted(s)
        t=sorted(t)
        
        if(s==t):return True
        else:return False
        '''
        
        # Approach2: (44ms, 14.8 MB)
        return sorted(s)==sorted(t)
        
