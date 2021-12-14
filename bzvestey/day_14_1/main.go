package main

import (
	"fmt"
	"os"
	"strings"
)

type Update struct {
	Combo  string
	Insert string
}

type Input struct {
	Base string
	//Updates []*Update
	Updates map[string]string
}

func parseInput(rows []string) *Input {
	i := &Input{
		Updates: map[string]string{},
	}
	for k, r := range rows {
		switch k {
		case 0:
			i.Base = r
		case 1:
			// Do nothing, blank line.
		default:
			pieces := strings.Split(r, " -> ")
			i.Updates[pieces[0]] = pieces[1]
			//i.Updates = append(i.Updates, &Update{Combo: pieces[0], Insert: pieces[1]})
		}
	}
	return i
}

func main() {
	fileName := "./input"
	if len(os.Args) >= 2 {
		fileName = os.Args[1]
	}

	data, err := os.ReadFile(fileName)
	if err != nil {
		panic(err)
	}

	rows := strings.Split(string(data), "\n")
	rows = rows[:len(rows)-1]

	input := parseInput(rows)

	current := "" + input.Base
	for step := 0; step < 10; step++ {
		start := current
		current = string(start[0])
		for i := 1; i < len(start); i++ {
			current += input.Updates[string(start[i-1])+string(start[i])]
			current += string(start[i])
		}
		fmt.Printf("Step %d with len(%d)\n", step+1, len(current))
	}

	elements := map[rune]int{}
	for _, r := range current {
		elements[r]++
	}

	largest := elements['N']
	smallest := elements['B']
	for _, count := range elements {
		if count < smallest {
			smallest = count
		}
		if count > largest {
			largest = count
		}
	}

	fmt.Printf("Largest(%d) - Smallest(%d) = %d\n", largest, smallest, largest-smallest)
}
