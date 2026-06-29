class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        this is a two pointers problem
        pointer1 will start at begining of array
        pointer2 = pointer1+1 

            while pointer1 < pointer2:
                current_sum = number[pointer1] + number[pointer2]
                if current_sum == target
                    return numbers[pointer1 + 1], numbers[pointenr2 + 1]
                else:
                    pointer2 += 1 moving pointer2 alonmg
                
                pointer1 += 1 move pounter1 along
                pointer2 = pointer1 + 1
        """
# [1,2,3,4] looking for 7
        left = 0
        right = left + 1
        while left < right:
            right = left + 1
            while right != len(numbers):
                current_sum = numbers[left] + numbers[right]
                if current_sum == target:
                    return [left + 1, right + 1]
                else:
                    right += 1
            left += 1


        