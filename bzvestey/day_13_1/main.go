package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Fold struct {
	Line       int
	IsVertical bool
}

type Point struct {
	X int
	Y int
}

type Page struct {
	Points []*Point
	Folds  []*Fold
}

func parseMap(lines []string) *Page {
	p := &Page{}
	for _, l := range lines {
		if len(l) == 0 {
			continue
		} else if strings.Index(l, "fold") == 0 {
			parts := strings.Split(l, " ")
			sides := strings.Split(parts[2], "=")
			i, err := strconv.Atoi(sides[1])
			if err != nil {
				panic(err)
			}
			p.Folds = append(p.Folds, &Fold{
				Line:       i,
				IsVertical: sides[0] == "x",
			})
		} else {
			sides := strings.Split(l, ",")
			x, err := strconv.Atoi(sides[0])
			if err != nil {
				panic(err)
			}
			y, err := strconv.Atoi(sides[1])
			if err != nil {
				panic(err)
			}
			p.Points = append(p.Points, &Point{X: x, Y: y})
		}
	}
	return p
}

func foldPage(points []*Point, f *Fold) {
	for _, p := range points {
		if f.IsVertical {
			if p.X > f.Line {
				p.X = p.X - ((p.X - f.Line) * 2)
			}
		} else if p.Y > f.Line {
			//fmt.Println("Old Y: ", p.Y)
			p.Y = p.Y - ((p.Y - f.Line) * 2)
			//fmt.Println("New Y: ", p.Y)
		}
	}
}

func makeUnique(points []*Point) []*Point {
	m := map[string]*Point{}
	for _, p := range points {
		m[fmt.Sprintf("%d,%d", p.X, p.Y)] = p
	}

	np := []*Point{}
	for _, p := range m {
		np = append(np, p)
	}
	return np
}

func main() {
	data, err := os.ReadFile("./input")
	//data, err := os.ReadFile("./example1")
	if err != nil {
		panic(err)
	}

	rows := strings.Split(string(data), "\n")
	rows = rows[:len(rows)-1]

	p := parseMap(rows)
	fmt.Println("Starting Num Points: ", len(p.Points))
	for k, f := range p.Folds {
		foldPage(p.Points, f)
		p.Points = makeUnique(p.Points)
		fmt.Println("Fold ", k+1, " Num Points ", len(p.Points))
	}
}
