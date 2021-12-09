package main

import (
	"fmt"
	"os"
	"strings"
)

type A struct {
	Ten  []string
	Four []string
}

func parseLines(input []string) []A {
	var a []A
	for _, i := range input {
		parts := strings.Split(i, " | ")
		if len(parts) != 2 {
			panic("Not enough parts")
		}
		a = append(a, A{
			Ten:  strings.Split(parts[0], " "),
			Four: strings.Split(parts[1], " "),
		})
	}
	return a
}

func main() {
	data, err := os.ReadFile("./input")
	if err != nil {
		panic(err)
	}

	rows := strings.Split(string(data), "\n")
	rows = rows[:len(rows)-1]

	sections := parseLines(rows)

	var one int = 0
	var four int = 0
	var seven int = 0
	var eight int = 0

	for _, sec := range sections {
		for _, f := range sec.Four {
			switch len(f) {
			case 2:
				one++
			case 4:
				four++
			case 3:
				seven++
			case 7:
				eight++
			}
		}
	}

	fmt.Println("Sections: ", sections)
	fmt.Println("one: ", one)
	fmt.Println("four: ", four)
	fmt.Println("seven: ", seven)
	fmt.Println("eight: ", eight)
	fmt.Println("Combined: ", one+four+seven+eight)
}
