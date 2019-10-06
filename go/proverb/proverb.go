// Print proverb for a given list
package proverb

import "fmt"

// print proverb given list of items
func Proverb(rhyme []string) []string {
	if len(rhyme) == 0 {
		return make([]string, 0)
	}
	proverb := make([]string, len(rhyme))
	for i := 0; i < len(rhyme)-1; i++ {
		proverb[i] = fmt.Sprintf("For want of a %s the %s was lost.", rhyme[i], rhyme[i+1])
	}

	proverb[len(rhyme)-1] = fmt.Sprintf("And all for the want of a %s.", rhyme[0])
	return proverb
}
