package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	fileName := "./input"
	if len(os.Args) > 1 {
		fileName = os.Args[1]
	}
	data, err := os.ReadFile(fileName)
	if err != nil {
		panic(err)
	}

	runData("target area: x=20..30, y=-10..-5")
	runData(string(data))
}

func parseSides(in string) (int, int) {
	sides := strings.Split(in, "..")
	l, err := strconv.Atoi(sides[0])
	if err != nil {
		panic(err)
	}
	r, err := strconv.Atoi(sides[1])
	if err != nil {
		panic(err)
	}
	return l, r
}

func runData(data string) {
	p1 := strings.Split(strings.TrimSpace(data), "x=")
	nums := strings.Split(p1[1], ", y=")
	x1, x2 := parseSides(nums[0])
	y1, y2 := parseSides(nums[1])
	fmt.Printf("%d,%d <-> %d,%d\n", x1, y1, x2, y2)

	//yGap := y1 - y2

	pv := map[string]bool{}
	hits := 0
	for xv := 0; xv <= x2; xv++ {
		for yv := -1000; yv < 1000; yv++ {
			sx := xv
			sy := yv
			x := 0
			y := 0
			for (x < x1 || y > y2) && x < x2 && y > y1 {
				x += sx
				y += sy
				if sx > 0 {
					sx--
				}
				sy--
			}
			if x >= x1 && x <= x2 && y >= y1 && y <= y2 {
				pv[fmt.Sprintf("%d,%d", xv, yv)] = true
				hits++
			}
		}
	}
	fmt.Println("Count: ", len(pv), " | ", hits)
	//fmt.Println(pv)
}
