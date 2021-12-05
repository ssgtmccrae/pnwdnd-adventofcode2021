package main

import (
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type Point struct {
	X int
	Y int
}

type Line struct {
	Start *Point
	End   *Point
}

func parsePoint(input string) *Point {
	cords := strings.Split(input, ",")
	if len(cords) != 2 {
		log.Panicf("Bad point input: %s", input)
	}

	x, err := strconv.Atoi(cords[0])
	if err != nil {
		panic(err)
	}

	y, err := strconv.Atoi(cords[1])
	if err != nil {
		panic(err)
	}

	return &Point{X: x, Y: y}
}

func parseLine(input string) *Line {
	points := strings.Split(input, " -> ")
	if len(points) != 2 {
		log.Panicf("Bad line input: %s", input)
	}

	return &Line{
		Start: parsePoint(points[0]),
		End:   parsePoint(points[1]),
	}
}

func parseInput(input []string) []*Line {
	lines := []*Line{}
	for _, l := range input {
		if len(l) == 0 {
			continue
		}
		lines = append(lines, parseLine(l))
	}
	return lines
}

func updateMap(line *Line, m [][]int) [][]int {
	if line.Start.X != line.End.X && line.Start.Y != line.End.Y {
		return m
	}

	isHor := line.Start.X != line.End.X

	start := line.Start.X
	if !isHor {
		start = line.Start.Y
	}

	end := line.End.X
	if !isHor {
		end = line.End.Y
	}

	if start > end {
		temp := start
		start = end
		end = temp
	}

	for start <= end {
		if isHor {
			m[start][line.Start.Y]++
		} else {
			m[line.Start.X][start]++
		}
		start++
	}

	return m
}

func main() {
	data, err := os.ReadFile("./input")
	if err != nil {
		panic(err)
	}

	rows := strings.Split(string(data), "\n")
	//rows = rows[:len(rows)-1]

	lines := parseInput(rows)

	var m [][]int
	for i := 0; i < 1000; i++ {
		m = append(m, make([]int, 1000))
	}

	for k, l := range lines {
		m = updateMap(l, m)
		fmt.Printf("%d: (%d, %d) -> (%d, %d)\n", k, l.Start.X, l.Start.Y, l.End.X, l.End.Y)
	}

	fmt.Println("Num lines: ", len(rows))

	//fmt.Println("Map:", m)

	count := 0
	for _, row := range m {
		for _, col := range row {
			if col > 1 {
				count++
			}
		}
	}

	fmt.Println("Count: ", count)
}
