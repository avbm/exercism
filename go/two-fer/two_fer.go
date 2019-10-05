// print One for you one for me
package twofer

// ShareWith function to accept string name and print
// One for <name> one for me
func ShareWith(name string) string {
	if name == "" {
		name = "you"
	}
	return "One for " + name + ", one for me."
}
