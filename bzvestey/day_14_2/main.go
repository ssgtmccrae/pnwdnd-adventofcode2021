package main

import (
	"fmt"
	"os"
	"strings"
)

type Update struct {
	Combo  string
	Insert rune
}

type Input struct {
	Current  map[string]int
	Elements map[rune]int
	Updates  map[string]rune
}

type Node struct {
	Next  *Node
	Value rune
	Count int8
}

func parseInput(rows []string) *Input {
	i := &Input{
		Current:  map[string]int{},
		Elements: map[rune]int{},
		Updates:  map[string]rune{},
	}
	for k, r := range rows {
		switch k {
		case 0:
			var last rune
			for _, ru := range r {
				i.Elements[ru]++
				if string(last) != "" {
					i.Current[string(last)+string(ru)]++
				}
				last = ru
			}
		case 1:
			// Do nothing, blank line.
		default:
			pieces := strings.Split(r, " -> ")
			i.Updates[pieces[0]] = rune(pieces[1][0])
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

	current := input.Current
	for i := 0; i < 40; i++ {
		next := map[string]int{}
		for cs, count := range current {
			//next[cs] += count

			r := input.Updates[cs]
			input.Elements[r] += count

			left := string(cs[0]) + string(r)
			right := string(r) + string(cs[1])
			next[left] += count
			next[right] += count

		}
		current = next
	}

	largest := input.Elements['N']
	smallest := input.Elements['B']
	for _, count := range input.Elements {
		if count < smallest {
			smallest = count
		}
		if count > largest {
			largest = count
		}
	}

	fmt.Printf("Largest(%d) - Smallest(%d) = %d\n", largest, smallest, largest-smallest)
}
