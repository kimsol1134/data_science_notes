'''
왼쪽전체의 합 = 오른쪽 전체의 합 
을 만족하는 인덱스(=피벗인덱스) 구하기
피벗인덱스 자신은 계산에 포함 안함.
left_sum
right_sum
인덱스 0 부터 차례로 구한다?
num_length 10000 
'''

class Solution:
    def pivotIndex(self, nums) -> int:
        left_sum = 0 
        right_sum = sum(nums[1:])
        i = 0
        if left_sum ==right_sum:
            return 0
        while i < len(nums):
            left_sum += nums[i]
            right_sum -= nums[i+1]
            if left_sum ==right_sum:
                return i+1
            else :
                i +=1
        return -1

