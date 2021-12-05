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
	// 6225
	// 24805
	//if line.Start.X != line.End.X && line.Start.Y != line.End.Y {
	//	return m
	//}

	startX := line.Start.X
	startY := line.Start.Y

	endX := line.End.X
	endY := line.End.Y

	dirX := 1
	if startX > endX {
		dirX = -1
	}

	dirY := 1
	if startY > endY {
		dirY = -1
	}

	inc := 1
	for inc != 0 {
		inc = 0
		m[startX][startY]++
		if startX != endX {
			startX += dirX
			inc++
		}
		if startY != endY {
			startY += dirY
			inc++
		}
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

	for _, l := range lines {
		m = updateMap(l, m)
		//fmt.Printf("%d: (%d, %d) -> (%d, %d)\n", k, l.Start.X, l.Start.Y, l.End.X, l.End.Y)
	}

	//`:wfmtfmt.Println("Num lines: ", len(rows))

	// fmt.Println("Map:", m)

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
