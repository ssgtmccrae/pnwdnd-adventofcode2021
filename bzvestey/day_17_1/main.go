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

	runData(string(data))
	runData("target area: x=20..30, y=-10..-5")
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

	xv := 1
	yv := 1000

	xf := -1
	for xf < 0 && xv < x1 {
		xp := 0
		sv := xv
		for sv > 0 && xp < x2 {
			xp += sv
			sv--
		}
		if sv == 0 && xp >= x1 && xp <= x2 {
			xf = xp
		} else {
			xv++
		}
	}

	ym := -1
	yf := -1
	for ym < 0 {
		yp := 0
		sv := yv
		top := 0
		for yp > y2 {
			yp += sv
			if yp > top {
				top = yp
			}
			sv--
		}
		if yp >= y1 && yp <= y1 {
			ym = top
			yf = yp
		} else {
			yv--
		}
	}

	fmt.Printf("X V=%d P=%d\n", xv, xf)
	fmt.Printf("Y V=%d P=%d M=%d\n", yv, yf, ym)
}
