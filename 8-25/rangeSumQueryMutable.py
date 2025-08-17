class NumArray:

    def __init__(self, nums: List[int]):
        self.dynamic = [None for i in range(len(nums))]
        self.nums = nums

        soFar = 0
        for i in range(len(nums)):
            soFar += nums[i]
            self.dynamic[i] = soFar

    def update(self, index: int, val: int) -> None:
        difference = val - self.nums[index]
        for i in range(index, len(self.nums), 1):
            self.dynamic[i] += difference
        self.nums[index] = val


    def sumRange(self, left: int, right: int) -> int:
        # print("dynamic : ", self.dynamic)
        leftSum = 0

        if(left != 0):
            leftSum = self.dynamic[left - 1]
        
        return self.dynamic[right] - leftSum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)