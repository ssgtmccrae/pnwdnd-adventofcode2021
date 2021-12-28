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

func checkOnAgainstOff(on Command, offs []Command) []Command {
	for i, off := range offs {
		// Check to see if they don't overlap.
		if on.XE < off.XS || on.XS > off.XE || on.YE < off.YS || on.YS > off.YE || on.ZE < off.ZS || on.ZS > off.ZE {
			continue
		}

		// Check to see if they completely overlap
		if on.XS > off.XS && on.XE < off.XE && on.YS > off.YS && on.YE < off.YE && on.ZS > off.ZS && on.ZE < off.ZE {
			return []Command{}
		}

		// Cut up the uncovered parts of the on and check them against the remaining offs.
		cmds := []Command{}
		rmOff := offs[i+1:]

		xe := on.XE
		xs := on.XS

		ys := on.YS
		ye := on.YE

		zs := on.ZS
		ze := on.ZE

		// -z check
		if on.ZS < off.ZS {
			cmds = append(cmds, checkOnAgainstOff(Command{
				On: true,
				XS: xs,
				XE: xe,
				YS: ys,
				YE: ye,
				ZS: zs,
				ZE: off.ZS - 1,
			}, rmOff)...)
			zs = off.ZS
		}

		// +z check
		if on.ZE > off.ZE {
			cmds = append(cmds, checkOnAgainstOff(Command{
				On: true,
				XS: xs,
				XE: xe,
				YS: ys,
				YE: ye,
				ZS: off.ZE + 1,
				ZE: ze,
			}, rmOff)...)
			ze = off.ZE
		}

		// -y check
		if on.YS < off.YS {
			cmds = append(cmds, checkOnAgainstOff(Command{
				On: true,
				XS: xs,
				XE: xe,
				YS: ys,
				YE: off.YS - 1,
				ZS: zs,
				ZE: ze,
			}, rmOff)...)
			ys = off.YS
		}

		// +y check
		if on.YE > off.YE {
			cmds = append(cmds, checkOnAgainstOff(Command{
				On: true,
				XS: xs,
				XE: xe,
				YS: off.YE + 1,
				YE: ye,
				ZS: zs,
				ZE: ze,
			}, rmOff)...)
			ye = off.YE
		}

		// -x check
		if on.XS < off.XS {
			cmds = append(cmds, checkOnAgainstOff(Command{
				On: true,
				XS: xs,
				XE: off.XS - 1,
				YS: ys,
				YE: ye,
				ZS: zs,
				ZE: ze,
			}, rmOff)...)
			xs = off.XS
		}

		// +x check
		if on.XE > off.XE {
			cmds = append(cmds, checkOnAgainstOff(Command{
				On: true,
				XS: off.XE + 1,
				XE: xe,
				YS: ys,
				YE: ye,
				ZS: zs,
				ZE: ze,
			}, rmOff)...)
			xs = off.XS
		}

		return cmds
	}

	return []Command{on}
}

func runData(data string) {
	rows := strings.Split(string(data), "\n")

	cmds := parseInput(rows)

	// First weed out any on commands that are negated by off commands
	offCmds := []Command{}
	remOn := []Command{}
	for i := len(cmds) - 1; i >= 0; i-- {
		// Save the list of off commands
		if !cmds[i].On {
			offCmds = append(offCmds, cmds[i])
			continue
		}

		// Check on command against
		remOn = append(remOn, checkOnAgainstOff(cmds[i], offCmds)...)
	}

	fmt.Println("On after Off: ", len(remOn))

	// Make sure that none of the on commands overlap
	finCmds := []Command{}
	for i, cmd := range remOn {
		finCmds = append(finCmds, checkOnAgainstOff(cmd, remOn[i+1:])...)
	}

	fmt.Println("Final after On: ", len(finCmds))

	// Calculate the area of the non-overlapping on commands
	count2 := 0
	for _, cmd := range finCmds {
		count2 += (cmd.XE - cmd.XS + 1) * (cmd.YE - cmd.YS + 1) * (cmd.ZE - cmd.ZS + 1)
	}

	fmt.Println("Count 2: ", count2)
}
