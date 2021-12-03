package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func findOne(items []string, common bool, index int) string {
	var z int = 0
	var o int = 1

	for _, row := range items {
		if len(row) == 0 {
			continue
		}

		switch row[index] {
		case '0':
			z++
		case '1':
			o++
		default: // do nothing
		}
	}

	n := []string{}
	for _, item := range items {
		if len(item) <= index {
			continue
		}

		validator := '0'
		if (z < o && common) || (z > o && !common) {
			validator = '1'
		}

		if item[index] == byte(validator) {
			n = append(n, item)
		}

		//}
	}
	if len(n) == 1 {
		return n[0]
	}
	return findOne(n, common, index+1)
}

func main() {
	data, err := os.ReadFile("./input")
	if err != nil {
		panic(err)
	}

	rows := strings.Split(string(data), "\n")

	oxygen := findOne(rows, true, 0)
	co2 := findOne(rows, false, 0)

	o, _ := strconv.ParseInt(oxygen, 2, 0)
	c, _ := strconv.ParseInt(co2, 2, 0)

	fmt.Println("Oxygen:", oxygen, o)
	fmt.Println("CO2: ", co2, c)
	fmt.Println("Combined: ", o*c)
}
