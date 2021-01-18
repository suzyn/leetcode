# Implement a solution with a linear runtime complexity and without using extra memory.
# extra memory 가 array 안에서의 추가적인 메모리? 아니면 코드 전체에서의 추가적인 메모리를 말하는 것인지?
# linear runtime complexity = O(n)
# 모든 숫자가 두번씩 등장, 하나의 숫자만 한번 등장 => 항상 홀수 길이의 배열 

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Approach : Hash Table 이용 
        # (120 ms, 16.2MB)
        hashmap=defaultdict(int)
        for i in nums:
            hashmap[i]+=1
        for i in hashmap:
            if(hashmap[i]==1):
                return i
        
        '''
        # Approach : 추가적인 메모리를 아예 사용하지 않고, 리스트의 index를 경우의 수를 나누어 비교
        # Accepted (but, 120 ms, 15.5MB)
        nums.sort()
        for i in range(len(nums)):
            if(i==0):
                if(len(nums)==1 or nums[i]!=nums[i+1]):return nums[i]
            elif(i==len(nums)-1):
                if(nums[i]!=nums[i-1]):return nums[i]
            else:
                if(nums[i]!=nums[i+1] and nums[i]!=nums[i-1]):return nums[i]
        '''
        
        '''
        # Approach : 추가적인 메모리를 아예 사용하지 않고, 리스트의 원소를 빼고 넣으면서 비교 
        # Accepted (but, 3892 ms, 15.7MB)
        for i in range(len(nums)):
            val=nums[i]
            nums.remove(val)
            if(val in nums):nums.insert(i,val)
            else:return val
        ''' 