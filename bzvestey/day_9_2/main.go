package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Point struct {
	X   int
	Y   int
	Num int
}

func (p Point) String() string {
	//fmt.Println(p.X, " | ", p.Y, " | |, )
	return fmt.Sprintf("%d,%d", p.X, p.Y)
}

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

func checkMap(p Point, m [][]int) []Point {
	list := []Point{}

	if p.X > 0 && m[p.Y][p.X-1] != 9 {
		list = append(list, Point{X: p.X - 1, Y: p.Y, Num: m[p.Y][p.X-1]})
	}
	if p.X < (len(m[p.Y])-1) && m[p.Y][p.X+1] != 9 {
		list = append(list, Point{X: p.X + 1, Y: p.Y, Num: m[p.Y][p.X+1]})
	}
	if p.Y > 0 && m[p.Y-1][p.X] != 9 {
		list = append(list, Point{X: p.X, Y: p.Y - 1, Num: m[p.Y-1][p.X]})
	}
	if p.Y < (len(m)-1) && m[p.Y+1][p.X] != 9 {
		list = append(list, Point{X: p.X, Y: p.Y + 1, Num: m[p.Y+1][p.X]})
	}

	return list
}

func main() {
	data, err := os.ReadFile("./input")
	if err != nil {
		panic(err)
	}

	rows := strings.Split(string(data), "\n")
	rows = rows[:len(rows)-1]

	m := parseMap(rows)

	var lowSpots []Point

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
			lowSpots = append(lowSpots, Point{X: x, Y: y, Num: cell})
		}
	}

	fmt.Println(lowSpots)

	used := map[string]*int{}
	var sizes []int = make([]int, len(lowSpots))
	for i, point := range lowSpots {
		list := map[string]*int{}
		queue := []Point{point}

		for len(queue) > 0 {
			p := queue[0]
			queue = queue[1:]
			s := p.String()

			if list[s] != nil || used[s] != nil {
				continue
			}

			list[s] = &p.Num
			used[s] = &p.Num
			queue = append(queue, checkMap(p, m)...)
		}

		sizes[i] = len(list)
	}

	var max1 int = 0
	var max2 int = 0
	var max3 int = 0

	for _, size := range sizes {
		if max1 >= size {
			continue
		}

		if size > max3 {
			max1 = max2
			max2 = max3
			max3 = size
		} else if size > max2 {
			max1 = max2
			max2 = size
		} else {
			max1 = size
		}
	}

	var sum int = max1 * max2 * max3

	fmt.Println("Sum:", sum)
}
