package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Placement struct {
	Number   int
	Selected bool
}

type Board struct {
	Places []*Placement
}

func getRandomNumbers(input string) []int {
	strs := strings.Split(input, ",")
	var ints []int = make([]int, len(strs))

	for k, s := range strs {
		i, err := strconv.Atoi(s)
		if err != nil {
			panic(err)
		}
		ints[k] = i
	}

	return ints
}

func getBoards(input []string) []*Board {
	var boards []*Board
	b := &Board{}
	for _, line := range input {
		if len(line) == 0 {
			if len(b.Places) < 25 {
				panic(line)
			}
			boards = append(boards, b)
			b = &Board{}
			continue
		}

		ps := strings.Split(line, " ")
		for _, p := range ps {
			if len(p) == 0 {
				continue
			}
			i, err := strconv.Atoi(p)
			if err != nil {
				panic(err)
			}
			b.Places = append(b.Places, &Placement{Number: i, Selected: false})
		}
	}
	return boards
}

func checkIfBoardHasWin(b *Board) bool {
	return (b.Places[0].Selected && b.Places[1].Selected && b.Places[2].Selected && b.Places[3].Selected && b.Places[4].Selected) ||
		(b.Places[5].Selected && b.Places[6].Selected && b.Places[7].Selected && b.Places[8].Selected && b.Places[9].Selected) ||
		(b.Places[10].Selected && b.Places[11].Selected && b.Places[12].Selected && b.Places[13].Selected && b.Places[14].Selected) ||
		(b.Places[15].Selected && b.Places[16].Selected && b.Places[17].Selected && b.Places[18].Selected && b.Places[19].Selected) ||
		(b.Places[20].Selected && b.Places[21].Selected && b.Places[22].Selected && b.Places[23].Selected && b.Places[24].Selected) ||
		(b.Places[0].Selected && b.Places[5].Selected && b.Places[10].Selected && b.Places[15].Selected && b.Places[20].Selected) ||
		(b.Places[1].Selected && b.Places[6].Selected && b.Places[11].Selected && b.Places[16].Selected && b.Places[21].Selected) ||
		(b.Places[2].Selected && b.Places[7].Selected && b.Places[12].Selected && b.Places[17].Selected && b.Places[22].Selected) ||
		(b.Places[3].Selected && b.Places[8].Selected && b.Places[13].Selected && b.Places[18].Selected && b.Places[23].Selected) ||
		(b.Places[4].Selected && b.Places[9].Selected && b.Places[14].Selected && b.Places[19].Selected && b.Places[24].Selected)
}

func calculateScore(b *Board, win int) int {
	var score int = 0
	for _, p := range b.Places {
		if !p.Selected {
			score += p.Number
		}
	}
	return score * win
}

func main() {
	data, err := os.ReadFile("./input")
	if err != nil {
		panic(err)
	}

	rows := strings.Split(string(data), "\n")

	rands := getRandomNumbers(rows[0])
	boards := getBoards(rows[2:])

	for _, num := range rands {
		for _, b := range boards {
			for _, p := range b.Places {
				if p.Number == num {
					p.Selected = true
				}
			}

			if checkIfBoardHasWin(b) {
				fmt.Println("Final Score Is: ", calculateScore(b, num))
				return
			}
		}
	}
}
