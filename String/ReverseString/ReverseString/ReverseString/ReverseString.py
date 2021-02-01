class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Approach1 : (248 ms, 18.7MB)
        pt1=0
        pt2=len(s)-1
        
        for i in range(len(s)//2):      # 몫 구하기 - Python : /, Python3 : //
            s[pt1],s[pt2]=s[pt2],s[pt1]
            pt1+=1
            pt2-=1
                