'''
two-pointer 방식 이용 
start, end : Equi-Directional 

start==0이면
    end==0 이면 continue
    end!=0 start와 교체 
'''

'''
0을 발견하면 가장 뒤에 append, 해당 0삭제
'''
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # Accepted (but 600ms)
        for start in range(len(nums)-1):
            end=start+1
            while(end<len(nums)):
                if(nums[start]==0):
                    if(nums[end]!=0):
                        nums[start], nums[end] = nums[end], nums[start]
                        break
                    else:
                        end+=1
                else : break

            

                
            

            
            
            
            
                
    
