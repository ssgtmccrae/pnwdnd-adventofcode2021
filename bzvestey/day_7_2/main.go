package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func calcCost(dist int) int {
	var cost int = 0
	for c := 1; c <= dist; c++ {
		cost += c
	}
	return cost
}

func main() {
	data, err := os.ReadFile("./input")
	if err != nil {
		panic(err)
	}

	cols := strings.Split(strings.TrimSpace(string(data)), ",")

	var horzPosition []int = make([]int, len(cols))
	var sum int = 0
	var max int = 0
	for k, c := range cols {
		hp, err := strconv.Atoi(c)
		if err != nil {
			panic(err)
		}
		horzPosition[k] = hp
		sum += hp
		if hp > max {
			max = hp
		}
	}

	fmt.Println("Horizontal Positions: ", horzPosition)
	fmt.Println("Sum: ", sum)
	fmt.Println("Average: ", float64(sum)/float64(len(horzPosition)))

	var bestValue int = -1
	var bestIndex int = 0
	for cur := 0; cur < max; cur++ {
		var value int = 0
		for _, hp := range horzPosition {
			dist := cur - hp
			if hp > cur {
				dist = hp - cur
			}

			value += calcCost(dist)
		}
		if value < bestValue || bestValue == -1 {
			bestValue = value
			bestIndex = cur
		}
	}

	fmt.Println("Best Index: ", bestIndex)
	fmt.Println("Best Value: ", bestValue)
}
