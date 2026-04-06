func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}
	map3 := make([]int, 26)
	for i := 0; i < len(s); i++ {
		map3[s[i]-"a"[0]] += 1
		map3[t[i]-"a"[0]] -= 1
	}
	for k, _ := range map3 {
		if map3[k] != 0 {
			return false
		}
	}
	return true
}
