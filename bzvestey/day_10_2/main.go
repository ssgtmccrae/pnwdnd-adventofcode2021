package main

import (
	"fmt"
	"math"
	"os"
	"sort"
	"strings"
)

func getOpener(r rune) rune {
	switch r {
	case ']':
		return '['
	case ')':
		return '('
	case '>':
		return '<'
	case '}':
		return '{'
	default:
		return ' '
	}
}

func checkRow(row string) []rune {
	closeQueue := []rune{}
	for _, cell := range row {
		switch cell {
		case '[':
			fallthrough
		case '(':
			fallthrough
		case '<':
			fallthrough
		case '{':
			closeQueue = append([]rune{cell}, closeQueue...)
		case ']':
			fallthrough
		case ')':
			fallthrough
		case '>':
			fallthrough
		case '}':
			if closeQueue[0] == getOpener(cell) {
				fmt.Println("Closing chunk")
				closeQueue = closeQueue[1:]
			} else {
				return nil
			}
		}
	}
	return closeQueue
}

func main() {
	data, err := os.ReadFile("./input")
	if err != nil {
		panic(err)
	}

	rows := strings.Split(string(data), "\n")
	rows = rows[:len(rows)-1]

	incomplete := []int{}
	for _, row := range rows {
		remainder := checkRow(row)

		if remainder == nil {
			continue
		}

		total := 0
		for _, r := range remainder {
			switch r {
			case '(':
				total = (total * 5) + 1
			case '[':
				total = (total * 5) + 2
			case '{':
				total = (total * 5) + 3
			case '<':
				total = (total * 5) + 4
			}
		}
		incomplete = append(incomplete, total)
	}

	sort.Ints(incomplete)
	mid := int(math.Floor(float64(len(incomplete)) * 0.5))

	fmt.Println("Num Rows: ", len(rows))
	fmt.Println("Incomplete: ", incomplete)
	fmt.Println("Total: ", incomplete[mid])
}
