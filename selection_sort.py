def selection_sort(nums):
  for i in range(len(nums)):
    lowest_value_index = i
    for j in range(i+1, len(nums)):
      if nums[j] < nums[lowest_value_index]:
        lowest_value_index = j
    nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
  return nums

if __name__ == "__main__":
  print(selection_sort([45,65,23,89,18]))
