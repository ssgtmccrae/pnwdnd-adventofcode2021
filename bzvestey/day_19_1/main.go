package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Point struct {
	X int
	Y int
	Z int
}

type Scanner struct {
	IsPositioned bool

	Position Point
	Rotation Point

	Beacons []*Point
}

func parseMan(input []string) []*Scanner {
	var scanners []*Scanner
	var cur *Scanner
	for k, i := range input {
		if strings.Index(i, "--- ") == 0 {
			if cur != nil {
				scanners = append(scanners, cur)
			}
			cur = &Scanner{IsPositioned: k == 0}
		} else if len(i) > 0 {
			nums := strings.Split(i, ",")
			x, err := strconv.Atoi(nums[0])
			if err != nil {
				panic(err)
			}
			y, err := strconv.Atoi(nums[1])
			if err != nil {
				panic(err)
			}
			z, err := strconv.Atoi(nums[2])
			if err != nil {
				panic(err)
			}
			cur.Beacons = append(cur.Beacons, &Point{X: x, Y: y, Z: z})
		}
	}
	scanners = append(scanners, cur)
	return scanners
}

func pointToString(p *Point) string {
	return fmt.Sprintf("%d,%d,%d", p.X, p.Y, p.Z)
}

func pointsToMap(points []*Point) map[string]*Point {
	m := map[string]*Point{}
	for _, p := range points {
		m[pointToString(p)] = p
	}
	return m
}

func compareBeacons(a []*Point, b []*Point) *Point {
	set := pointsToMap(a)
	for _, ap := range a {
		for _, bp := range b {
			common := 0
			delta := &Point{
				X: ap.X - bp.X,
				Y: ap.Y - bp.Y,
				Z: ap.Z - bp.Z,
			}

			for _, bp1 := range b {
				modifiedPoint := &Point{
					X: bp1.X + delta.X,
					Y: bp1.Y + delta.Y,
					Z: bp1.Z + delta.Z,
				}
				if _, ok := set[pointToString(modifiedPoint)]; ok {
					common++
				}
			}

			if common >= 12 {
				return delta
			}
		}
	}
	return nil
}

func rotateX(beacons []*Point) []*Point {
	nb := []*Point{}
	for _, b := range beacons {
		nb = append(nb, &Point{X: -b.Y, Y: b.X, Z: b.Z})
	}
	return nb
}

func rotateY(beacons []*Point) []*Point {
	nb := []*Point{}
	for _, b := range beacons {
		nb = append(nb, &Point{X: b.X, Y: -b.Z, Z: b.Y})
	}
	return nb
}

func rotateZ(beacons []*Point) []*Point {
	nb := []*Point{}
	for _, b := range beacons {
		nb = append(nb, &Point{X: -b.Z, Y: b.Y, Z: b.X})
	}
	return nb
}

func compareScanners(a *Scanner, b *Scanner) (*Scanner, *Point) {
	cur := b.Beacons

	for xr := 0; xr < 4; xr++ {
		cur = rotateX(cur)
		for yr := 0; yr < 4; yr++ {
			cur = rotateY(cur)
			for zr := 0; zr < 4; zr++ {
				cur = rotateZ(cur)
				delta := compareBeacons(a.Beacons, cur)
				if delta == nil {
					continue
				}
				for _, p := range cur {
					p.X += delta.X
					p.Y += delta.Y
					p.Z += delta.Z
				}
				m := pointsToMap(append(a.Beacons, cur...))
				ns := &Scanner{IsPositioned: true}
				for _, v := range m {
					ns.Beacons = append(ns.Beacons, v)
				}
				return ns, delta
			}
		}
	}

	return nil, nil
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
	scanners := parseMan(rows)

	deltas := []*Point{}
	final := scanners[0]
	scanners = scanners[1:]
	for len(scanners) > 0 {
		fmt.Println("Remaining Scanners: ", len(scanners))
		for i := 0; i < len(scanners); i++ {
			out, delta := compareScanners(final, scanners[i])
			if out == nil {
				continue
			}
			final = out
			deltas = append(deltas, delta)
			scanners = append(scanners[:i], scanners[i+1:]...)
			i--
		}
	}

	fmt.Println("Count:", len(final.Beacons))
}
