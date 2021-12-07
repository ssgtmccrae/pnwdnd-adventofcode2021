package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	data, err := os.ReadFile("./input")
	if err != nil {
		panic(err)
	}

	sints := strings.Split(strings.TrimSpace(string(data)), ",")
	var ints []int
	for _, si := range sints {
		i, err := strconv.Atoi(si)
		if err != nil {
			panic(err)
		}
		ints = append(ints, i)
	}

	for i := 0; i < 80; i++ {
		nf := 0
		for key, fish := range ints {
			if fish == 0 {
				nf++
				ints[key] = 6
			} else {
				ints[key]--
			}
		}
		for c := 0; c < nf; c++ {
			ints = append(ints, 8)
		}
	}

	fmt.Println("Num Fish: ", len(ints))

	// rows = rows[:len(rows)-1]

	// var last int = 0

	// for _, v := range rows {
	// 	cur, err := strconv.Atoi(v)
	// 	if err != nil {
	// 		panic(err)
	// 	}

	// 	if last != 0 {
	// 		// do Something
	// 	}

	// 	last = cur
	// }

	// fmt.Println("Last:", last)
}
