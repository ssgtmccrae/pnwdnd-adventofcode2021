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

	one, err := strconv.Atoi(rows[0])
	two, err := strconv.Atoi(rows[1])
	var last int = -1
	var larger int = 0
	var lower int = 0
	for k, v := range rows {
		if len(v) == 0 || k <= 1 {
			continue
		}
		three, err := strconv.Atoi(v)
		if err != nil {
			panic(err)
		}
		cur := one + two + three
		one = two
		two = three
		if last >= 0 {
			if last < cur {
				larger = larger + 1
			} else {
				lower = lower + 1
			}
		}
		last = cur
	}

	fmt.Println("larger:", larger)
	fmt.Println("Lower:", lower)
}
