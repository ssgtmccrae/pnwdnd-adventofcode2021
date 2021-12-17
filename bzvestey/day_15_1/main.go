package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

// type Path struct {
// 	Cost      int
// 	Locations map[int]bool
// 	lastX     int
// 	lastY     int
// }

func parseInput(input []string) [][]int {
	m := [][]int{}
	for _, line := range input {
		if len(line) == 0 {
			continue
		}
		row := make([]int, len(line))
		for x, r := range line {
			i, err := strconv.Atoi(string(r))
			if err != nil {
				panic(err)
			}
			row[x] = i
		}
		m = append(m, row)
	}
	return m
}

// func getShortedPath(paths []*Path) (*Path, int) {
// 	shortest := paths[0]
// 	index := 0
// 	for i, path := range paths {
// 		if path.Cost < shortest.Cost {
// 			shortest = path
// 			index = i
// 		}
// 	}
// 	return shortest, index
// }

// func checkPosition(path *Path, newX int, newY int) bool {
// 	check := calcMapIndex(newX, newY)
// 	_, ok := path.Locations[check]
// 	return !ok
// }

// func copyMap(loc map[int]bool, np int) map[int]bool {
// 	nloc := map[int]bool{np: true}
// 	for k, v := range loc {
// 		nloc[k] = v
// 	}
// 	return nloc
// }

func calcMapIndex(x int, y int) int {
	return y*1000 + x
}

type Node struct {
	X int
	Y int
	C int
	F int
	G int
	H int
}

func cheapestNode(nodes []*Node) (*Node, []*Node) {
	cheapest := nodes[0]
	index := 0
	for i, n := range nodes {
		if n.F < cheapest.F {
			cheapest = n
			index = i
		}
	}

	return cheapest, append(nodes[:index], nodes[index+1:]...)
}

func checkNode(current *Node, closed map[int]*Node, m [][]int, x int, y int) *Node {
	if _, ok := closed[calcMapIndex(x, y)]; ok {
		return nil
	}

	g := current.G + (m[y][x] * 30) // Kind of a hack... need better g and h generation
	h := (len(m) - y) * (len(m[0]) - x)

	return &Node{X: x, Y: y, C: current.C + m[y][x], G: g, H: h, F: g + h}
}

func aStar(m [][]int) int {
	openNodes := []*Node{{X: 0, Y: 0, C: 0, F: 0}}
	closedNodes := map[int]*Node{}
	xMax := len(m[0]) - 1
	yMax := len(m) - 1

	var current *Node
	for len(openNodes) > 0 {
		current, openNodes = cheapestNode(openNodes)
		closedNodes[calcMapIndex(current.X, current.Y)] = current

		if current.X == xMax && current.Y == yMax {
			for _, n := range openNodes {
				fmt.Println(n)
			}
			fmt.Println(closedNodes[calcMapIndex(8, 9)])
			fmt.Println(closedNodes[calcMapIndex(9, 8)])
			return current.C
		}

		if current.X > 0 {
			node := checkNode(current, closedNodes, m, current.X-1, current.Y)
			if node != nil {
				openNodes = append(openNodes, node)
			}
		}
		if current.Y > 0 {
			node := checkNode(current, closedNodes, m, current.X, current.Y-1)
			if node != nil {
				openNodes = append(openNodes, node)
			}
		}
		if current.X < xMax {
			node := checkNode(current, closedNodes, m, current.X+1, current.Y)
			if node != nil {
				openNodes = append(openNodes, node)
			}
		}
		if current.Y < yMax {
			node := checkNode(current, closedNodes, m, current.X, current.Y+1)
			if node != nil {
				openNodes = append(openNodes, node)
			}
		}
	}

	return 0
}

// func newPath(path *Path, m [][]int, newX int, newY int) *Path {
// 	// fmt.Printf("%d,%d\n", newX, newY)
// 	return &Path{
// 		Cost:      path.Cost + m[newY][newX],
// 		lastX:     newX,
// 		lastY:     newY,
// 		Locations: copyMap(path.Locations, calcMapIndex(newX, newY)),
// 	}
// }

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
	m := parseInput(rows)

	// paths := []*Path{{Cost: 0, Locations: map[int]bool{0: true}, lastX: 0, lastY: 0}}
	// xMax := len(m[0]) - 1
	// yMax := len(m) - 1
	// fmt.Printf("Max: %d,%d\n", xMax, yMax)
	// var finish *Path
	// for finish == nil {
	// 	current, index := getShortedPath(paths)
	// 	paths = append(paths[:index], paths[index+1:]...)

	// 	if current.lastX == xMax && current.lastY == yMax {
	// 		finish = current
	// 		continue
	// 	}

	// 	if current.lastX > 0 {
	// 		if checkPosition(current, current.lastX-1, current.lastY) {
	// 			paths = append(paths, newPath(current, m, current.lastX-1, current.lastY))
	// 		}
	// 	}
	// 	if current.lastY > 0 {
	// 		if checkPosition(current, current.lastX, current.lastY-1) {
	// 			paths = append(paths, newPath(current, m, current.lastX, current.lastY-1))
	// 		}
	// 	}
	// 	if current.lastX < xMax {
	// 		if checkPosition(current, current.lastX+1, current.lastY) {
	// 			paths = append(paths, newPath(current, m, current.lastX+1, current.lastY))
	// 		}
	// 	}
	// 	if current.lastY < yMax {
	// 		if checkPosition(current, current.lastX, current.lastY+1) {
	// 			paths = append(paths, newPath(current, m, current.lastX, current.lastY+1))
	// 		}
	// 	}
	// }

	fmt.Println("Cost: ", aStar(m))
}
