class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        sort the list nlogn
        output = []
        for i in range(len(nums)):

            target = -nums[i]
            j = i+1
            k = len(nums) - 1

            while j < k:

                here once again we have a few senerios

                current_sum = nums[j] + nums[k]
                if current_sum == target:
                    output.append([nums[i],nums[j],nums[k]])
                elif current_sum < target:
                    j += 1
                else:
                    k -= 1
        return output
        """

        nums.sort()
        output = {}

        for i in range(len(nums)):
            target = -nums[i]
            j = i+1
            k = len(nums) - 1

            while j < k:
                current_sum = nums[j] + nums[k]
                if current_sum == target:
                    
                    if (nums[i], nums[j], nums[k]) not in output:
                        output[(nums[i], nums[j], nums[k])] = True
                    j += 1
                    k -= 1
                    

                elif current_sum < target:
                    j += 1
                else:
                    k -= 1
        return [list(triplets) for triplets in output.keys()]