func twoSum(nums []int, target int) []int {
	myMap := make(map[int]int)
	for i := 1; i <= len(nums); i++ {
		a := myMap[target-nums[i-1]]
		if a != 0 {
			return []int{a - 1, i - 1}
		}
		myMap[nums[i-1]] = i
	}
	return nil
}
