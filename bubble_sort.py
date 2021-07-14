def bubble_sort(nums):
  swapped = True
  while swapped:
    swapped = False
    for i in range(len(nums) - 1):
      if nums[i] > nums[i+1]:
        nums[i], nums[i+1] = nums[i+1], nums[i]
        swapped = True
  return nums

if __name__ == "__main__":
  print(bubble_sort([45,65,23,89,18]))
