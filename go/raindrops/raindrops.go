package raindrops

import "strconv"

/*
Convert - funtion to:
if number is divisible by 3 print Pling
if number is divisible by 5 print Plang
if number is divisible by 7 print Plong
*/
func Convert(num int) string {
	retVal := ""
	if num%3 == 0 {
		retVal += "Pling"
	}
	if num%5 == 0 {
		retVal += "Plang"
	}
	if num%7 == 0 {
		retVal += "Plong"
	}
	if retVal == "" {
		retVal = strconv.Itoa(num)
	}
	return retVal
}
