class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        '''
        # Approach1 : Linear Search (Time Limit Exceeded)
        for start in range(len(nums)):
            end=start+1
            while start<end and end<len(nums):
                if(nums[start]==nums[end]):return True
                else:end+=1
        return False
    
    
        # Approach2 : Sorting Algorithm (104ms, 17.1MB)
        nums.sort()
        for i in range(len(nums)-1):
            if(nums[i]==nums[i+1]): return True
        return False
    
    
        # Approach3 : Hash Table (112ms, 19.8MB)
        hashmap=defaultdict(int)
        for i in range(len(nums)):
            hashmap[nums[i]]+=1
            if(hashmap[nums[i]]==2): return True
    
    
	    # Approach4 : Hash Table (108ms, 19.4MB)
        nums.sort()
        hashmap=defaultdict(int)
        for i in range(len(nums)):
            hashmap[nums[i]]+=1
            if(hashmap[nums[i]]==2): return True    
        '''  

        # Approach5 : set() 이용 
        set_list=set(nums)
        for i in range(len(nums)):
            if len(nums)==len(set_list): return False
            else: return True
