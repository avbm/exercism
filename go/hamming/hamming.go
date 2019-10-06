// Package hamming calculates the Hamming difference between two DNA strands.
package hamming

import "errors"

// Distance returns the Hamming difference between 2 strings representing DNA strands.
func Distance(a, b string) (int, error) {
	if len(a) != len(b) {
		return 0, errors.New("sequence lengths don't match")
	}

	count := 0
	for i := 0; i < len(a); i++ {
		if a[i] != b[i] {
			count++
		}
	}
	return count, nil
}
