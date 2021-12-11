package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	data, err := os.ReadFile("./input")
	if err != nil {
		panic(err)
	}

	rows := strings.Split(string(data), "\n")
	rows = rows[:len(rows)-1]

	m := make([][]int, 10)
	for i, row := range rows {
		m[i] = make([]int, 10)
		for j, cell := range row {
			c, err := strconv.Atoi(string(cell))
			if err != nil {
				panic(err)
			}
			m[i][j] = c
		}
	}

	numFlashes := 0
	for step := 0; step < 100; step++ {
		isFirstRound := true
		hasFlash := false
		flashed := map[int]bool{}
		for hasFlash || isFirstRound {
			hasFlash = false
			for y := 0; y < 10; y++ {
				for x := 0; x < 10; x++ {
					if isFirstRound {
						m[y][x]++
					}

					if m[y][x] > 9 && flashed[y*10+x] != true {
						flashed[y*10+x] = true
						hasFlash = true
						numFlashes++

						if x > 0 {
							if y > 0 {
								m[y-1][x-1]++
							}
							if y < 9 {
								m[y+1][x-1]++
							}
							m[y][x-1]++
						}
						if x < 9 {
							if y > 0 {
								m[y-1][x+1]++
							}
							if y < 9 {
								m[y+1][x+1]++
							}
							m[y][x+1]++
						}
						if y > 0 {
							m[y-1][x]++
						}
						if y < 9 {
							m[y+1][x]++
						}
					}
				}
			}
			isFirstRound = false
		}

		for y := 0; y < 10; y++ {
			for x := 0; x < 10; x++ {
				if m[y][x] > 9 {
					m[y][x] = 0
				}
			}
		}
	}

	fmt.Println("Num Flashes: ", numFlashes)
}
