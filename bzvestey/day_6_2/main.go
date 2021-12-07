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
	var ints []int64
	for _, si := range sints {
		i, err := strconv.Atoi(si)
		if err != nil {
			panic(err)
		}
		ints = append(ints, int64(i))
	}

	var days []int64 = make([]int64, 9)
	for _, i := range ints {
		days[i]++
	}

	for i := 0; i < 256; i++ {
		day0 := days[0]
		days[0] = days[1]
		days[1] = days[2]
		days[2] = days[3]
		days[3] = days[4]
		days[4] = days[5]
		days[5] = days[6]
		days[6] = days[7] + day0
		days[7] = days[8]
		days[8] = day0
	}

	numFish := days[0] + days[1] + days[2] + days[3] + days[4] + days[5] + days[6] + days[7] + days[8]

	fmt.Println("Num Fish: ", numFish)
}
