package main

import (
	"encoding/hex"
	"fmt"
	"math"
	"os"
	"strconv"
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

func calcVersionInfo(packet *Packet) int {
	v := packet.Version
	for _, c := range packet.Children {
		v += calcVersionInfo(c)
	}
	return v
}

func parsePacket(data []byte, offset int) (*Packet, int) {
	v, offset := getBits(data, offset, 3)
	t, offset := getBits(data, offset, 3)
	fmt.Println(offset, strconv.FormatInt(int64(v[0]), 2), strconv.FormatInt(int64(t[0]), 2))

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

func main() {
	fileName := "./input"
	if len(os.Args) > 1 {
		fileName = os.Args[1]
	}
	data, err := os.ReadFile(fileName)
	if err != nil {
		panic(err)
	}

	b, err := hex.DecodeString(strings.TrimSpace(string(data)))
	if err != nil {
		panic(err)
	}

	p, _ := parsePacket(b, 0)

	fmt.Println(calcVersionInfo(p))
}
