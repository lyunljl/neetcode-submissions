class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        create a hashmap
        create a for loop that tracks the index and it's values by enumeratiing the list of numbers
        set difference to the target minums the item of the list at said index
        check if the differnece exists in hashmap
            if yes we can return the value (which will be the index in this case) and the current index
            if not we insert the current value into the hashmap BACKWARDS so the actual number as the key and its index as the value
        end.

        the genius here is in the way we set up the dictionary. We set it up backwards
        meaning instead of index maps to number (i --> n)
        we do number mapped to it's index (n --> i)
        this allows us to be able to check backwards essentially checking if our difference at the current index exists as a key since keys are easier to check than values
        "its easier to retrive the value of a key than the other way around for a dictionary.:

        time complexity: O(n)
        space complecity: O(n)
        '''
        digitmap = {}
        for i, j in enumerate(nums):
            diff = target - nums[i]
            if diff in digitmap:
                return [digitmap[diff], i]
            digitmap[j] = i
            