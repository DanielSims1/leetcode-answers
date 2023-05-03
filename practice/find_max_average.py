from typing import List
def findMaxAverage( nums: List[int], k: int) -> float:
        left = 0
        right = k
        
        m = sum(nums[left:right])
        top = m
        while right < len(nums):
            print(f"m={m}")
            print(f"nums[left]={nums[left]} | nums[right]={nums[right]}")
            m = m - nums[left] + nums[right]
            if m > top:
                top = m
            
            left += 1
            right += 1

        return top / k

print(findMaxAverage([0,4,0,3,2],1))