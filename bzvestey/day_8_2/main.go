package main

import (
	"fmt"
	"math"
	"os"
	"sort"
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

func numMiss(left string, right string) int {
	var miss int = 0
	for _, a := range right {
		if strings.IndexRune(left, a) == -1 {
			miss++
		}
	}
	return miss
}

func figureOutDigits(seg A) map[string]int {
	var output map[string]int = map[string]int{}

	var one string
	var two string
	var three string
	var four string
	var five string
	var six string
	var seven string
	var eight string
	var nine string
	var zero string

	var len5 []string
	var len6 []string
	for _, s := range seg.Ten {
		switch len(s) {
		case 2:
			one = s
		case 3:
			seven = s
		case 4:
			four = s
		case 5:
			len5 = append(len5, s)
		case 6:
			len6 = append(len6, s)
		case 7:
			eight = s
		}
	}

	for _, l6 := range len6 {
		if numMiss(l6, four) == 0 {
			nine = l6
		} else if numMiss(l6, one) == 0 {
			zero = l6
		} else {
			six = l6
		}
	}

	fmt.Println(len5)
	for _, l5 := range len5 {
		if numMiss(l5, seven) == 0 {
			three = l5
		} else if numMiss(l5, four) == 1 {
			five = l5
		} else {
			two = l5
		}
	}

	//  .   _   _   .   _   _   _   _   _   _
	// . | . | . | | | | . | . . | | | | | | |
	//  .   _   _   _   _   _   .   _   _   .
	// . | | . . | . | . | | | . | | | . | | |
	//  .   _   _   .   _   _   .   _   _   _

	output[ss(one)] = 1
	output[ss(two)] = 2
	output[ss(three)] = 3
	output[ss(four)] = 4
	output[ss(five)] = 5
	output[ss(six)] = 6
	output[ss(seven)] = 7
	output[ss(eight)] = 8
	output[ss(nine)] = 9
	output[ss(zero)] = 0

	return output
}

func ss(in string) string {
	var s []string
	for _, i := range in {
		s = append(s, string(i))
	}
	sort.Strings(s)
	out := strings.Join(s, "")

	fmt.Println(out)
	return out
}

func main() {
	data, err := os.ReadFile("./input")
	if err != nil {
		panic(err)
	}

	rows := strings.Split(string(data), "\n")
	rows = rows[:len(rows)-1]

	sections := parseLines(rows)

	var count int = 0
	for _, seg := range sections {
		digits := figureOutDigits(seg)
		var total int = 0
		for i, d := range seg.Four {
			total += digits[ss(d)] * (int(math.Max(math.Pow10(3-i), 1)))
		}
		fmt.Println("total: ", total, " digits: ", digits, " four: ", seg.Four)
		count += total
	}

	// fmt.Println("Sections: ", sections)
	fmt.Println("count: ", count)
}
