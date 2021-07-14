def quick_sort(nums):
  def partition(nums, low, high):
    pivot = nums[(low + high) //2]
    i = low - 1
    j = high + 1
    while True:
      i += 1
      while nums[i] < pivot:
        i += 1
      j -= 1
      while nums[j] > pivot:
        j -= 1
      if i >= j:
        return j
      nums[i], nums[j] = nums[j], nums[i]
      
  def quick_sorter(nums):
    def _quick_sorter(items, low, high):
      if low < high:
        split_index = partition(items, low, high)
        _quick_sorter(items, low, split_index)
        _quick_sorter(items, split_index + 1, high)
        
    _quick_sorter(nums, 0, len(nums) - 1)
  
  quick_sorter(nums)
  return nums

if __name__ == "__main__":
  print(quick_sort([45,65,23,89,18]))
