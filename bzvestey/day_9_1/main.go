package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func parseMap(input []string) [][]int {
	var m [][]int = make([][]int, len(input))
	for ri, row := range input {
		var r []int = make([]int, len(row))
		for ci, cell := range row {
			c, err := strconv.Atoi(string(cell))
			if err != nil {
				panic(err)
			}
			r[ci] = c
		}
		m[ri] = r
	}
	return m
}

func main() {
	data, err := os.ReadFile("./input")
	if err != nil {
		panic(err)
	}

	rows := strings.Split(string(data), "\n")
	rows = rows[:len(rows)-1]

	m := parseMap(rows)

	var sum int = 0

	xend := len(m[0]) - 1
	yend := len(m) - 1

	for y, row := range m {
		for x, cell := range row {
			if x > 0 && row[x-1] <= cell {
				continue
			}
			if x < xend && row[x+1] <= cell {
				continue
			}
			if y > 0 && m[y-1][x] <= cell {
				continue
			}
			if y < yend && m[y+1][x] <= cell {
				continue
			}
			sum += cell + 1
		}
	}

	fmt.Println("Sum:", sum)
}
