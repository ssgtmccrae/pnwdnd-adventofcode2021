package main

import (
	"fmt"
	"os"
	"strings"
)

const mag int = 1

func parseImage(input []string) (string, [][]rune) {
	algo := ""
	image := [][]rune{}
	for k, row := range input {
		if k == 0 {
			algo = row
		} else if len(row) > 0 {
			image = append(image, []rune(row))
		}
	}
	return algo, image
}

func printImage(image [][]rune) {
	fmt.Println("================================")
	for _, line := range image {
		fmt.Println(string(line))
	}
	fmt.Println("================================")
}

func getPlacement(x int, y int, image [][]rune, border rune) string {
	if x < 0 || y < 0 || x >= len(image[0]) || y >= len(image) {
		return string(border)
	}
	return string(image[y][x])
}

func stringToIndex(str string) int {
	index := 0
	for _, char := range str {
		index = index << 1
		if char == '#' {
			index++
		}
	}
	return index
}

func updateImage(image [][]rune, algo string, border rune) ([][]rune, rune) {
	ni := make([][]rune, len(image)+(mag*2))
	for y := -mag; y < (len(image) + mag); y++ {
		ni[y+mag] = make([]rune, len(image[0])+(mag*2))
		for x := -mag; x < (len(image[0]) + mag); x++ {
			num := getPlacement(x-1, y-1, image, border) +
				getPlacement(x, y-1, image, border) +
				getPlacement(x+1, y-1, image, border) +
				getPlacement(x-1, y, image, border) +
				getPlacement(x, y, image, border) +
				getPlacement(x+1, y, image, border) +
				getPlacement(x-1, y+1, image, border) +
				getPlacement(x, y+1, image, border) +
				getPlacement(x+1, y+1, image, border)
			ni[y+mag][x+mag] = rune(algo[stringToIndex(num)])
		}
	}

	switch border {
	case '.':
		if algo[0] == '.' {
			border = '.'
		} else {
			border = '#'
		}
	case '#':
		if algo[len(algo)-1] == '#' {
			border = '#'
		} else {
			border = '.'
		}
	}

	return ni, border
}

func main() {
	fileName := "./input"
	if len(os.Args) > 1 {
		fileName = os.Args[1]
	}
	data, err := os.ReadFile(fileName)
	if err != nil {
		panic(err)
	}

	runData(string(data))
}

func runData(data string) {
	rows := strings.Split(string(data), "\n")
	algo, image := parseImage(rows)
	border := '.'

	fmt.Println(algo)
	printImage(image)

	for i := 0; i < 50; i++ {
		image, border = updateImage(image, algo, border)
	}

	lit := 0
	for y := 0; y < len(image); y++ {
		for x := 0; x < len(image[y]); x++ {
			if image[y][x] == '#' {
				lit++
			}
		}
	}
	fmt.Println("Lit 2: ", lit)
}
