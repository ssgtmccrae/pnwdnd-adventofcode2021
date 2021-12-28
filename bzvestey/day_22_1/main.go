package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

type Command struct {
	On bool
	XS int
	XE int
	YS int
	YE int
	ZS int
	ZE int
}

func parseInput(input []string) []Command {
	var cmds []Command
	re := regexp.MustCompile(
		"(\\w+) x=(-?\\d+)..(-?\\d+),y=(-?\\d+)..(-?\\d+),z=(-?\\d+)..(-?\\d+)",
	)
	for _, l := range input {
		if len(l) == 0 {
			continue
		}

		matches := re.FindStringSubmatch(l)
		if len(matches) != 8 {
			panic(fmt.Sprintln(l, len(matches), matches))
		}

		xs, _ := strconv.Atoi(matches[2])
		xe, _ := strconv.Atoi(matches[3])
		ys, _ := strconv.Atoi(matches[4])
		ye, _ := strconv.Atoi(matches[5])
		zs, _ := strconv.Atoi(matches[6])
		ze, _ := strconv.Atoi(matches[7])

		if xe < xs {
			temp := xs
			xs = xe
			xe = temp
		}
		if ye < ys {
			temp := ys
			ys = ye
			ye = temp
		}
		if ze < zs {
			temp := zs
			zs = ze
			ze = temp
		}

		if xs > 50 || xe < -50 || ys > 50 || ye < -50 || zs > 50 || ze < -50 {
			continue
		}

		cmds = append(cmds, Command{
			On: matches[1] == "on",
			XS: xs, XE: xe, YS: ys, YE: ye, ZS: zs, ZE: ze,
		})
	}
	return cmds
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

	cmds := parseInput(rows)

	//fmt.Println("Commands:", cmds)

	count := 0
	m := map[string]bool{}
	for _, cmd := range cmds {
		for x := cmd.XS; x <= cmd.XE; x++ {
			for y := cmd.YS; y <= cmd.YE; y++ {
				for z := cmd.ZS; z <= cmd.ZE; z++ {
					name := fmt.Sprintf("%d,%d,%d", x, y, z)
					_, ok := m[name]
					if cmd.On && !ok {
						m[name] = true
						count++
					} else if !cmd.On && ok {
						delete(m, name)
						count--
					}
				}
			}
		}
	}

	fmt.Println("Count: ", count)
}
