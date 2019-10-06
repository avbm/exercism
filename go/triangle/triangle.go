// This is a "stub" file.  It's a little start on your solution.
// It's not a complete solution though; you have to write some code.

// Package triangle should have a package comment that summarizes what it's about.
// https://golang.org/doc/effective_go.html#commentary
package triangle

import "math"

// Notice KindFromSides() returns this type. Pick a suitable data type.
type Kind int

const (
	// Pick values for the following identifiers used by the test program.
	NaT = 0 // not a triangle
	Equ = 1 // equilateral
	Iso = 2 // isosceles
	Sca = 3 // scalene
)

// Sides of a triangle can't be Inf or NaN
func ValidSide(a float64) bool {
	if math.IsInf(a, 0) || math.IsNaN(a) || a < 0 {
		return false
	}
	return true
}

// check for triangle inequality
// zero length triangle not allowed
func ValidTriangle(a, b, c float64) bool {
	if a == b && b == c && a == 0 {
		return false
	}
	if (a+b) >= c && (b+c) >= a && (c+a) >= b {
		return true
	}
	return false
}

// KindFromSides should have a comment documenting it.
func KindFromSides(a, b, c float64) Kind {
	if !ValidSide(a) || !ValidSide(b) || !ValidSide(c) || !ValidTriangle(a, b, c) {
		return NaT
	} else if a == b && b == c {
		return Equ
	} else if a == b || b == c || c == a {
		return Iso
	}
	return Sca
}
