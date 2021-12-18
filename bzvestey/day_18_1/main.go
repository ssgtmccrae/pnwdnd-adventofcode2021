package main

import (
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

type SnailNum struct {
	IsPair bool

	Value int

	Left  *SnailNum
	Right *SnailNum
}

func (sn *SnailNum) String() string {
	if sn.IsPair {
		return fmt.Sprintf("[%s,%s]", sn.Left, sn.Right)
	} else {
		return fmt.Sprintf("%d", sn.Value)
	}
}

func parseNumber(numStr string, offset int) (*SnailNum, int) {
	num := &SnailNum{}

	var temp *SnailNum
	if numStr[offset] == '[' {
		num.IsPair = true
		offset++
		temp, offset = parseNumber(numStr, offset)
		num.Left = temp
		offset++
		temp, offset = parseNumber(numStr, offset)
		num.Right = temp
		offset++
	} else {
		newStr := ""
		for numStr[offset] != ']' && numStr[offset] != ',' {
			newStr += string(numStr[offset])
			offset++
		}
		n, err := strconv.Atoi(newStr)
		if err != nil {
			panic(err)
		}
		num.IsPair = false
		num.Value = n
	}

	return num, offset
}

func addToLeft(num int, sn *SnailNum) {
	if sn.IsPair {
		addToLeft(num, sn.Left)
	} else {
		sn.Value += num
	}
}

func addToRight(num int, sn *SnailNum) {
	if sn.IsPair {
		addToRight(num, sn.Right)
	} else {
		sn.Value += num
	}
}

func explodeNum(sn *SnailNum, depth int, left *SnailNum, right *SnailNum) bool {
	if sn.IsPair {
		if depth >= 4 && !sn.Left.IsPair && !sn.Right.IsPair {
			//fmt.Printf("Exploding with left %s and right %s\n", left, right)
			if left != nil {
				addToRight(sn.Left.Value, left)
			}
			if right != nil {
				addToLeft(sn.Right.Value, right)
			}
			sn.IsPair = false
			sn.Value = 0
			sn.Left = nil
			sn.Right = nil
			return true
		} else {
			if explodeNum(sn.Left, depth+1, left, sn.Right) {
				return true
			} else if explodeNum(sn.Right, depth+1, sn.Left, right) {
				return true
			}
		}
	} else {
		return false
	}
	return false
}

func splitNum(sn *SnailNum) bool {
	if sn.IsPair {
		if splitNum(sn.Left) {
			return true
		}
		if splitNum(sn.Right) {
			return true
		}
	} else {
		if sn.Value >= 10 {
			sn.IsPair = true
			sn.Left = &SnailNum{IsPair: false, Value: int(math.Floor(float64(sn.Value) / 2))}
			sn.Right = &SnailNum{IsPair: false, Value: int(math.Ceil(float64(sn.Value) / 2))}
			sn.Value = 0
			return true
		}
	}
	return false
}

func reduceNumber(sn *SnailNum) *SnailNum {
	hasChange := true
	for hasChange {
		fmt.Printf("Reducing number %s\n", sn)
		hasChange = false

		hasChange = explodeNum(sn, 0, nil, nil)

		if hasChange {
			continue
		}

		hasChange = splitNum(sn)
	}
	fmt.Println("Reduced to ", sn)
	return sn
}

func getMagnitude(sn *SnailNum) int {
	if sn.IsPair {
		return (getMagnitude(sn.Left) * 3) + (getMagnitude(sn.Right) * 2)
	} else {
		return sn.Value
	}
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

	nums := []*SnailNum{}
	for _, r := range rows {
		if len(r) == 0 {
			continue
		}
		sn, _ := parseNumber(r, 0)
		nums = append(nums, sn)
	}

	for k, n := range nums {
		fmt.Println(k, "     | ", n)
	}

	fn := nums[0]
	//for i := 1; i < 2; i++ {
	for i := 1; i < len(nums); i++ {
		fn = reduceNumber(&SnailNum{IsPair: true, Left: fn, Right: nums[i]})
	}

	fmt.Println("Reduced | ", fn)
	fmt.Println("Magnitude | ", getMagnitude(fn))
}
