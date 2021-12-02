package main

import (
	"errors"
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

	var horiz int = 0
	var depth int = 0
	var aim int = 0

	for _, cmd := range rows {
		if len(cmd) == 0 {
			continue
		}

		parts := strings.Split(cmd, " ")
		if len(parts) != 2 {
			panic(errors.New("Not enough parts to command"))
		}

		amount, err := strconv.Atoi(parts[1])
		if err != nil {
			panic(err)
		}

		switch parts[0] {
		case "forward":
			horiz = horiz + amount
			depth = depth + (aim * amount)
		case "down":
			aim = aim + amount
		case "up":
			aim = aim - amount
		default:
			panic(errors.New(cmd))
		}
	}

	fmt.Println("Horizontal: ", horiz)
	fmt.Println("Depth: ", depth)
	fmt.Println("Aim: ", aim)
	fmt.Println("Combined: ", horiz*depth)
}
