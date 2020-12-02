"""Quick analysis

pairs solution is O(N) space and time complexity
triplets solutions is O(N^2) time and O(N) space complexity
"""


def get_nums(path="./input.txt"):
    """Read file for number input

    return: sorted array on numbers
    """
    nums = []
    with open(path, "r") as _f:
        for line in _f.readlines():
            nums.append(int(line.strip()))
    nums.sort()
    return nums


def get_pairs(arr, target_sum=2020):
    """Find a pair of numbers in the array whose sum equals target"""
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:
            return arr[left], arr[right]
        elif current_sum < target_sum:
            # move left pointer rightward since sum is below target
            left += 1
        elif current_sum > target_sum:
            # move right pointer leftward since sum is above target
            right -= 1
    return None


def get_triplets(arr, target_sum=2020):
    """Find three numbers in the array such that they add up to target_sum"""
    for idx, num in enumerate(arr):
        new_target = target_sum - num
        pair = get_pairs(arr[idx+1:], new_target)
        if pair:
            a, b = pair
            return num, a, b
    return None


if __name__ == "__main__":

    nums = get_nums()
    pairs = get_pairs(nums)
    if pairs:
        print(pairs)
        print(pairs[0]*pairs[1])

    triplets = get_triplets(nums)
    if triplets:
        print(triplets)
        print(triplets[0]*triplets[1]*triplets[2])
