class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        # Approach1: Two-Pointer방식 (pt1보다 상대적으로 더 빠르게 이동하는 pt2를 기준으로 반복문이 실행됨)
        # (64ms, 15.2MB)
        pt1=0
        pt2=0
    
        while(pt2<len(nums)):
            if(nums[pt1]!=nums[pt2]):
                nums[pt1+1], nums[pt2] = nums[pt2], nums[pt1+1]
                pt1+=1
                pt2+=1
            else:pt2+=1
        
        return pt1+1
        '''
        
        # Approach2: Approach1에서 while문 대신 for문 이용 (56ms, 15.2MB)
        pt1=0
        pt2=0
        for pt2 in range(len(nums)):
            if(nums[pt1]!=nums[pt2]):
                nums[pt1+1], nums[pt2] = nums[pt2], nums[pt1+1]
                pt1+=1                
        return pt1+1
