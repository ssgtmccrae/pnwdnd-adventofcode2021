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

type Player struct {
	Pos          int
	Score        int
	DiceScore    int
	Posibilities int
}

type Game struct {
	Rolls    int
	Moves    int
	SubMoves int
}

type FinalScore struct {
	P1 int
	P2 int
}

func (l *FinalScore) Add(r *FinalScore) *FinalScore {
	l.P1 += r.P1
	l.P2 += r.P2
	return l
}

func moveDirac(p1 Player, p2 Player, g Game) *FinalScore {
	// Select the current player.
	playerNum := math.Mod(float64(g.Moves), 2)
	curPlayer := &p1
	if playerNum == 1 {
		//fmt.Println(g.Moves, " | ", playerNum, " | ", p1, " | ", p2)
		curPlayer = &p2
	}

	// Update the board
	g.SubMoves++
	if g.SubMoves > 3 {
		// Move to the next turn
		g.Moves++
		g.SubMoves = 0

		// Update the current players score
		curPlayer.Pos = int(math.Mod(float64(curPlayer.Pos+curPlayer.DiceScore), 10))
		curPlayer.Score += curPlayer.Pos + 1
		//fmt.Println(curPlayer.DiceScore, " | ", g.Moves, " | ", *curPlayer)
		curPlayer.DiceScore = 0

		if curPlayer.Score >= 21 {
			fs := &FinalScore{}
			if playerNum == 0 {
				fs.P1 = 1
			} else {
				fs.P2 = 1
			}
			return fs
		} else {
			return moveDirac(p1, p2, g)
		}
	} else {
		curPlayer.DiceScore++
		s1 := moveDirac(p1, p2, g)
		curPlayer.DiceScore++
		s2 := moveDirac(p1, p2, g)
		curPlayer.DiceScore++
		s3 := moveDirac(p1, p2, g)
		return s1.Add(s2).Add(s3)
	}
}

func handleMove(cur *Player, dist int, count int, update bool) {
	if update {
		pos := int(math.Mod(float64(cur.Pos+dist), 10))
		cur.Pos = pos
		cur.Score += pos + 1
	}
	cur.Posibilities *= count
}

func movePlayers(p1 Player, p2 Player, move int, dist int, count int) *FinalScore {
	if math.Mod(float64(move), 2) == 0 {
		handleMove(&p1, dist, count, true)
		handleMove(&p2, 0, count, false)

		if p1.Score >= 21 {
			return &FinalScore{P1: p1.Posibilities}
		}
	} else {
		handleMove(&p1, 0, count, false)
		handleMove(&p2, dist, count, true)

		if p2.Score >= 21 {
			return &FinalScore{P2: p2.Posibilities}
		}
	}
	move++
	return moveDirac2(p1, p2, move)
}

func moveDirac2(p1 Player, p2 Player, move int) *FinalScore {
	return movePlayers(p1, p2, move, 3, 1).Add(
		movePlayers(p1, p2, move, 4, 3),
	).Add(
		movePlayers(p1, p2, move, 5, 6),
	).Add(
		movePlayers(p1, p2, move, 6, 7),
	).Add(
		movePlayers(p1, p2, move, 7, 6),
	).Add(
		movePlayers(p1, p2, move, 8, 3),
	).Add(
		movePlayers(p1, p2, move, 9, 1),
	)
}

func runData(p1StartPos int, p2StartPos int) {
	fmt.Printf("Player 1 at %d and Player 2 at %d\n", p1StartPos, p2StartPos)

	fs := moveDirac2(
		Player{Pos: p1StartPos - 1, Posibilities: 1},
		Player{Pos: p2StartPos - 1, Posibilities: 1},
		0,
	)

	fmt.Printf("P1 Score %d | P2 Score %d\n", fs.P1, fs.P2)

	//
}
