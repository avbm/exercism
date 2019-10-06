package space

type Planet string

func Age(seconds float64, planet Planet) float64 {

	one_year := make(map[Planet]float64)
	one_year["Earth"] = 31557600.0
	one_year["Mercury"] = one_year["Earth"] * 0.2408467
	one_year["Venus"] = one_year["Earth"] * .61519726
	one_year["Mars"] = one_year["Earth"] * 1.8808158
	one_year["Jupiter"] = one_year["Earth"] * 11.862615
	one_year["Saturn"] = one_year["Earth"] * 29.447498
	one_year["Uranus"] = one_year["Earth"] * 84.016846
	one_year["Neptune"] = one_year["Earth"] * 164.79132

	return seconds / one_year[planet]

}
