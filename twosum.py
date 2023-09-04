def two_sum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


tokens = input('Enter a list of numbers (separated by commas): ')
split_tokens = tokens.split(',')
num_tokens = [eval(i) for i in split_tokens]
target_num = int(input('Enter target number: '))

print(two_sum(num_tokens, target_num))
