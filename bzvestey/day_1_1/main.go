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

	last, err := strconv.Atoi(rows[0])
	var larger int = 0
	var lower int = 0
	for k, v := range rows {
		if len(v) == 0 || k == 0 {
			continue
		}
		cur, err := strconv.Atoi(v)
		if err != nil {
			panic(err)
		}
		if last < cur {
			larger = larger + 1
		} else {
			lower = lower + 1
		}
		last = cur
	}

	fmt.Println("larger:", larger)
	fmt.Println("Lower:", lower)
}
