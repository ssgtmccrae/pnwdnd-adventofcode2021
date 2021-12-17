package main

import (
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func rowIncrease(row []int, count int) []int {
	nr := make([]int, len(row))
	for i, r := range row {
		nr[i] = r + count
		if nr[i] > 9 {
			nr[i] = nr[i] - 9
		}
	}
	return nr
}

func mapIncrease(m [][]int, count int) [][]int {
	nm := make([][]int, len(m))
	for i, r := range m {
		nm[i] = rowIncrease(r, count)
	}
	return nm
}

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
		m = append(m, append(row, append(rowIncrease(row, 1), append(rowIncrease(row, 2), append(rowIncrease(row, 3), rowIncrease(row, 4)...)...)...)...))
	}
	return append(m, append(mapIncrease(m, 1), append(mapIncrease(m, 2), append(mapIncrease(m, 3), mapIncrease(m, 4)...)...)...)...)
}

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

	g := current.G + m[y][x]
	h := int(math.Exp2(float64(y-len(m))) + math.Exp2(float64(x-len(m[0]))))

	return &Node{X: x, Y: y, C: current.C + m[y][x], G: g, H: h, F: g + h}
}

func aStar(m [][]int) int {
	openNodes := []*Node{{X: 0, Y: 0, C: 0, F: 0}}
	closedNodes := map[int]*Node{}
	nodesMap := map[int]*Node{0: openNodes[0]}
	xMax := len(m[0]) - 1
	yMax := len(m) - 1

	var current *Node
	for len(openNodes) > 0 {
		current, openNodes = cheapestNode(openNodes)
		closedNodes[calcMapIndex(current.X, current.Y)] = current

		if current.X == xMax && current.Y == yMax {
			return current.C
		}

		if current.X > 0 {
			node := checkNode(current, closedNodes, m, current.X-1, current.Y)
			if node != nil {
				n, ok := nodesMap[calcMapIndex(node.X, node.Y)]
				if ok && node.F < n.F {
					n.F = node.F
					n.G = node.G
					n.C = node.C
				} else if !ok {
					openNodes = append(openNodes, node)
					nodesMap[calcMapIndex(node.X, node.Y)] = node
				}
			}
		}
		if current.Y > 0 {
			node := checkNode(current, closedNodes, m, current.X, current.Y-1)
			if node != nil {
				n, ok := nodesMap[calcMapIndex(node.X, node.Y)]
				if ok && node.F < n.F {
					n.F = node.F
					n.G = node.G
					n.C = node.C
				} else if !ok {
					openNodes = append(openNodes, node)
					nodesMap[calcMapIndex(node.X, node.Y)] = node
				}
			}
		}
		if current.X < xMax {
			node := checkNode(current, closedNodes, m, current.X+1, current.Y)
			if node != nil {
				n, ok := nodesMap[calcMapIndex(node.X, node.Y)]
				if ok && node.F < n.F {
					n.F = node.F
					n.G = node.G
					n.C = node.C
				} else if !ok {
					openNodes = append(openNodes, node)
					nodesMap[calcMapIndex(node.X, node.Y)] = node
				}
			}
		}
		if current.Y < yMax {
			node := checkNode(current, closedNodes, m, current.X, current.Y+1)
			if node != nil {
				n, ok := nodesMap[calcMapIndex(node.X, node.Y)]
				if ok && node.F < n.F {
					n.F = node.F
					n.G = node.G
					n.C = node.C
				} else if !ok {
					openNodes = append(openNodes, node)
					nodesMap[calcMapIndex(node.X, node.Y)] = node
				}
			}
		}
	}

	return 0
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
	m := parseInput(rows)

	fmt.Println("Cost: ", aStar(m))
}
