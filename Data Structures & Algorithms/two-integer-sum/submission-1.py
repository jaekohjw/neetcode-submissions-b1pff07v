class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        positions = {}
        for i in range(len(nums)):
            if nums[i] in positions:
                positions[nums[i]].append(i)
            else:
                positions[nums[i]] = [i]
        print(positions)
        for num in positions:
            other_num = target - num
            if other_num in positions:
                if num == other_num:
                    if len(positions[num]) == 2:
                        return positions[num]
                else: 
                    return [positions[num][0], positions[other_num][0]]
        