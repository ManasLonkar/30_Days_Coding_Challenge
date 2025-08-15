from typing import List
class Problem:
    def sortarray(self, nums: List[int]) -> None:
        zero = []
        one = []
        two = []
        for num in nums:
            if num == 0:
                zero.append(0)
            elif num == 1:
                one.append(1)
            else:
                two.append(2)
        
        sorted_array = zero + one + two
        
        for i in range(len(nums)):
            nums[i] = sorted_array[i]

