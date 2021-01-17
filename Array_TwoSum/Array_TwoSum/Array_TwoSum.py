class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # Approach2 : Two-pass Hash Table (24ms, 13.5MB)
        hashmap={}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target-nums[i]
            if(complement in hashmap and hashmap[complement]!=i):
                return [i, hashmap[complement]]

            
        '''
        # Approach1 : Brute Force (36ms, 13.5MB)
        for pointer1 in range(len(nums)-1):
            for pointer2 in range(pointer1+1,len(nums)):
                if(nums[pointer1]+nums[pointer2]==target):
                   return [pointer1,pointer2]
        '''
                
        '''
        # Approach3 : One-pass Hash Table (32ms, 13.7MB)
        hashmap={}
        for i in range(len(nums)):
            complement=target-nums[i]
            if(complement in hashmap and hashmap[complement]!=i):
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
        '''
        
        '''
        # Accepted (but,692 ms)
        # enumerate 이용해보기
        for pointer1,value1 in enumerate(nums):
            for pointer2,value2 in enumerate(nums):
                if(pointer1<pointer2 and value1+value2==target):
                    targetIndex.append(pointer1)
                    targetIndex.append(pointer2)
                    break
                else:continue
        return targetIndex
        '''