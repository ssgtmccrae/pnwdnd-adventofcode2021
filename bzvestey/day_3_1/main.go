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

	rows := strings.Split(string(data), "\n")

	var zero []int = make([]int, len(rows[0]))
	var one []int = make([]int, len(rows[0]))

	fmt.Println("Initial Zero: ", zero)
	fmt.Println("Initial One:  ", one)

	for _, row := range rows {
		if len(row) == 0 {
			continue
		}

		for c, v := range row {
			switch v {
			case '0':
				zero[c]++
			case '1':
				one[c]++
			default: // do nothing
			}
		}
	}

	gamma := ""
	epsilon := ""
	for k, z := range zero {
		o := one[k]
		if z > o {
			gamma += "0"
			epsilon += "1"
		} else {
			gamma += "1"
			epsilon += "0"
		}
	}

	g, _ := strconv.ParseInt(gamma, 2, 0)
	e, _ := strconv.ParseInt(epsilon, 2, 0)

	fmt.Println("Gamma:", gamma, g)
	fmt.Println("epsilon: ", epsilon, e)
	fmt.Println("Combined: ", g*e)
}
