package main

import (
	"fmt"
	"os"
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

func checkRow(row string, incomplete map[rune]int) {
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
				incomplete[cell]++
				return
			}
		}

	}
}

func main() {
	data, err := os.ReadFile("./input")
	if err != nil {
		panic(err)
	}

	rows := strings.Split(string(data), "\n")
	rows = rows[:len(rows)-1]

	incomplete := map[rune]int{}
	for _, row := range rows {
		checkRow(row, incomplete)
	}

	total := (incomplete[')'] * 3) +
		(incomplete[']'] * 57) +
		(incomplete['}'] * 1197) +
		(incomplete['>'] * 25137)

	fmt.Println("Num Rows: ", len(rows))
	fmt.Println("Incomplete: ", incomplete)
	fmt.Println("Total: ", total)
}
