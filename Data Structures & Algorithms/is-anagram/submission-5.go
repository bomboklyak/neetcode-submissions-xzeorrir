func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}
	map1 := make(map[uint8]int)
	map2 := make(map[uint8]int)
	for i := 0; i < len(s); i++ {
		map1[s[i]] += 1
		map2[t[i]] += 1
	}
	for k, v := range map1 {
		if map2[k] != v {
			return false
		}
	}
	return true
}
