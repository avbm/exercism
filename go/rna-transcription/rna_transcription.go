package strand

// ToRNA Convert DNA string to RNA
func ToRNA(dna string) string {
	lookup := make(map[rune]rune)
	lookup['G'] = 'C'
	lookup['C'] = 'G'
	lookup['T'] = 'A'
	lookup['A'] = 'U'

	rna := make([]rune, len(dna))
	for index, char := range dna {
		//rna[index] = lookup[char]  // Using lookup vs switch case seems to same performance
		//fmt.Println(char)
		switch char {
		case 'G':
			rna[index] = 'C'
		case 'C':
			rna[index] = 'G'
		case 'T':
			rna[index] = 'A'
		case 'A':
			rna[index] = 'U'
		}

	}
	return string(rna)
}
