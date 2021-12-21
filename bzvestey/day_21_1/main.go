package main

import (
	"fmt"
	"math"
)

func main() {
	// Example data
	runData(4, 8)
	// Input data
	runData(6, 10)
}

func move(pos int, score int, rolls int) (int, int, int) {
	moves := 0

	for i := 0; i < 3; i++ {
		rolls++

		// deterministic rolling...
		moves += int(math.Mod(float64(rolls-1), 100) + 1)
	}

	pos = int(math.Mod(float64(pos+moves), 10))
	score += pos + 1

	return pos, score, rolls
}

func runData(p1StartPos int, p2StartPos int) {
	fmt.Printf("Player 1 at %d and Player 2 at %d\n", p1StartPos, p2StartPos)

	p1Pos := p1StartPos - 1
	p1Score := 0

	p2Pos := p2StartPos - 1
	p2Score := 0

	rolls := 0

	for i := 0; p1Score < 1000 && p2Score < 1000; i++ {
		if math.Mod(float64(i), 2) == 0 {
			p1Pos, p1Score, rolls = move(p1Pos, p1Score, rolls)
		} else {
			p2Pos, p2Score, rolls = move(p2Pos, p2Score, rolls)
		}
	}

	fmt.Printf("P1 Score %d | P2 Score %d | rolls %d | answer 1 %d | answer 2 %d\n", p1Score, p2Score, rolls, p1Score*rolls, p2Score*rolls)

	//
}
