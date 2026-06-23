class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        at each step we need a way to check
            - in this entire array does there exist some value that is exactly my current number + 1
        if we set it we just get single values.
            sorting would cause an nlogn solution so no....
        
        if we set(nums): we will get {1,2,3,4,10}:
        we can turn it into a list: [1,2,3,4, 4, 10]
        output = []
        iterate through list
        for i in range(len(list)):
            if len(output < 1):
                output.append(list[i])
            if len(output) > 1 and i == output[i-1] in set:
                output.append(list[i])
            else:
                pass
        return len(output)
        '''
        '''
        [1,2,3,4, 4, 10]
        {1,2,3,4,10}
        set(nums)
        streak = 0 tracks max streak
        for i in range(len(nums):
            if num[i] in set AND num[i] - 1 not in set:
                streak += 1
                while streak < len(nums) or 
        '''
        num_set = set(nums)
        max_streak = 0

        if len(nums) == 0:
            return 0
        elif len(num_set) == 1:
            return 1

        for num in num_set:
            if num-1 not in num_set:
                current = num
                current_streak = 1
                while current + 1 in num_set:
                    current += 1
                    current_streak += 1
                max_streak = max(max_streak, current_streak)
        return max_streak


                
