package main

import (
	"encoding/hex"
	"fmt"
	"math"
	"os"
	"strings"
)

type Packet struct {
	Version int
	TypeId  int

	Value int

	Children []*Packet
}

func m8(n int) int {
	return 7 - int(math.Mod(float64(n), 8))
}

func getBits(data []byte, offset int, length int) ([]byte, int) {
	res := make([]byte, int(math.Ceil(float64(length)/8)))
	for lo := 0; lo < length; lo++ {
		res[lo/8] |= (data[offset/8] >> m8(offset) & 1) << m8(lo)
		offset++
	}
	return res, offset
}

func bytesToint(data []byte, length int) int {
	num := 0
	for _, b := range data {
		num = (num << 8) | int(b)
	}
	return num >> ((len(data) * 8) - length)
}

func parsePacket(data []byte, offset int) (*Packet, int) {
	v, offset := getBits(data, offset, 3)
	t, offset := getBits(data, offset, 3)

	p := &Packet{
		Version: bytesToint(v, 3),
		TypeId:  bytesToint(t, 3),
	}

	var temp []byte
	if p.TypeId == 4 {
		// Value
		pieces := []byte{}
		hasMore := true
		for hasMore {
			temp, offset = getBits(data, offset, 5)
			p := temp[0] >> 3
			pieces = append(pieces, p)
			hasMore = (p & 16) == 16
		}
		for _, piece := range pieces {
			p.Value = (p.Value << 4) | int(piece&15)
		}
	} else {
		// Operator
		temp, offset = getBits(data, offset, 1)
		lti := temp[0] >> 7
		var c *Packet
		if lti == 1 {
			temp, offset = getBits(data, offset, 11)
			num := bytesToint(temp, 11)
			for i := 0; i < num; i++ {
				c, offset = parsePacket(data, offset)
				p.Children = append(p.Children, c)
			}
		} else {
			temp, offset = getBits(data, offset, 15)
			end := bytesToint(temp, 15) + offset
			for offset < end {
				c, offset = parsePacket(data, offset)
				p.Children = append(p.Children, c)
			}
		}
	}

	return p, offset
}

func calcVersionInfo(packet *Packet) int {
	v := packet.Version
	for _, c := range packet.Children {
		v += calcVersionInfo(c)
	}
	return v
}

func calc(packet *Packet) int {
	switch packet.TypeId {
	case 0:
		sum := 0
		for _, c := range packet.Children {
			sum += calc(c)
		}
		return sum
	case 1:
		prod := 1
		for _, c := range packet.Children {
			prod *= calc(c)
		}
		return prod
	case 2:
		min := calc(packet.Children[0])
		for _, c := range packet.Children {
			cv := calc(c)
			if cv < min {
				min = cv
			}
		}
		return min
	case 3:
		max := calc(packet.Children[0])
		for _, c := range packet.Children {
			cv := calc(c)
			if cv > max {
				max = cv
			}
		}
		return max
	case 4:
		return packet.Value
	case 5:
		if calc(packet.Children[0]) > calc(packet.Children[1]) {
			return 1
		}
		return 0
	case 6:
		if calc(packet.Children[0]) < calc(packet.Children[1]) {
			return 1
		}
		return 0
	case 7:
		if calc(packet.Children[0]) == calc(packet.Children[1]) {
			return 1
		}
		return 0
	}

	return 0
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
	runData("C200B40A82")
	runData("04005AC33890")
	runData("880086C3E88112")
	runData("CE00C43D881120")
	runData("D8005AC2A8F0")
	runData("F600BC2D8F")
	runData("9C005AC2F8F0")
	runData("9C0141080250320F1802104A08")
}

func runData(data string) {
	b, err := hex.DecodeString(strings.TrimSpace(string(data)))
	if err != nil {
		panic(err)
	}

	p, _ := parsePacket(b, 0)

	for _, c := range p.Children {
		fmt.Println(c)
	}

	fmt.Println(calc(p))
}
