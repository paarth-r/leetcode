class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        li = 0
        ri = len(numbers)-1
        while li < ri:
            sum = numbers[li] + numbers[ri]
            if sum == target:
                break
            if sum > target:
                ri -= 1
            else:
                li += 1
        return [li+1, ri+1]