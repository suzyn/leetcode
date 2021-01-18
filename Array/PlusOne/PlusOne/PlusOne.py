'''
<배열을 정수로 보고, 1 더하기>
# index 를 1씩 줄이면서 배열의 마지막 값부터 확인 
    # 값 < 9 라면, 1 더하기, break
    # 값 ==9 라면, 해당 index의 값을 0으로 바꾸고 
        # index==0 이라면 배열의 맨 앞에 1 삽입 (insert)
'''
     
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)
        for i in range(length-1,-1,-1):
            if (digits[i]<9) : 
                digits[i]+=1
                break
            else :
                digits[i]=0
                if(i==0):
                    digits.insert(0,1)
                    
        return digits
                
            
        
        
