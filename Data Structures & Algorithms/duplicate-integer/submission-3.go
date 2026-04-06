func hasDuplicate(nums []int) bool {
	duplicate := make(map[int]bool)
	for _, num := range nums {
		if duplicate[num] {
			return true
		}
		duplicate[num] = true
	}
	return false
}
