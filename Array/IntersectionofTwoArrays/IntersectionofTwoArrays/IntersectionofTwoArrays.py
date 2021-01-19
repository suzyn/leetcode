'''
Given two integer arrays A[] and B[] of size m and n, respectively.
The intersection of two arrays is a list of distinct numbers which are present in both the arrays. 
'''

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Approach1: Hash Table
        hashmap1=defaultdict(int)
        hashmap2=defaultdict(int)
        intersection=[]

        for i in range(len(nums1)):
            hashmap1[nums1[i]]+=1
        for i in range(len(nums2)):
            hashmap2[nums2[i]]+=1

        if(len(nums1)>=len(nums2)):
            for i in range(len(nums2)):
                if(hashmap1[nums2[i]] and hashmap1[nums2[i]]>0):
                    intersection.append(nums2[i])
                    hashmap1[nums2[i]]-=1
        else:
            for i in range(len(nums1)):
                if(hashmap2[nums1[i]] and hashmap2[nums1[i]]>0):
                    intersection.append(nums1[i])
                    hashmap2[nums1[i]]-=1
        return intersection

        '''
        # Approach2: 단순 비교 , num1 & num2 의 길이로 경우의 수를 나눔
        intersection=[]
        if(len(nums1)>=len(nums2)):
            for i in range(len(nums2)):
                if nums2[i] in nums1:
                    intersection.append(nums2[i])
                    nums1.remove(nums2[i])
        else:
            for i in range(len(nums1)):
                if nums1[i] in nums2:
                    intersection.append(nums1[i])
                    nums2.remove(nums1[i])
        return intersection
    
        # Approach3: 단순 비교,길이에 따른 경우의 수를 나누지 않음 
        intersection=[]
        for i in range(len(nums2)):
            if nums2[i] in nums1:
                intersection.append(nums2[i])
                nums1.remove(nums2[i])
        return intersection
        '''