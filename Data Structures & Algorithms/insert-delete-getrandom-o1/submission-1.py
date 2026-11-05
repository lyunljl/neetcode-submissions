class RandomizedSet:

    def __init__(self):
        self.numsMap = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.numsMap:
            return False
        else:
            self.nums.append(val)
            self.numsMap[val] = len(self.nums) - 1
            return True

    def remove(self, val: int) -> bool:
        if val not in self.numsMap:
            return False
        else:
            index = self.numsMap[val]
            end_index = len(self.nums) - 1
            self.numsMap[self.nums[end_index]] = index 
            self.nums[index], self.nums[end_index] = self.nums[end_index], self.nums[index]
            
            self.nums.pop()
            del self.numsMap[val]
            return True


    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()