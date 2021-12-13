package main

import (
	"fmt"
	"os"
	"strings"
)

type Cave struct {
	Name  string
	Large bool

	Routes []Route
}

type Route struct {
	Cave1 *Cave
	Cave2 *Cave
}

type Map struct {
	Caves   []*Cave
	CaveMap map[string]*Cave

	Routes []Route

	Start *Cave
	End   *Cave
}

type Path struct {
	Caves   []*Cave
	CaveMap map[string]bool

	hasSmallTwice bool
}

func addCave(cave string, m *Map) *Cave {
	isLarge := cave[0] >= 'A' && cave[0] <= 'Z'
	m.Caves = append(m.Caves, &Cave{Name: cave, Large: isLarge})
	c := m.Caves[len(m.Caves)-1]
	m.CaveMap[cave] = c

	if cave == "start" {
		m.Start = c
	} else if cave == "end" {
		m.End = c
	}

	return c
}

func parseMap(routes []string) *Map {
	m := &Map{
		CaveMap: map[string]*Cave{},
	}
	for _, r := range routes {
		caves := strings.Split(r, "-")
		if len(caves) != 2 {
			fmt.Println(caves)
			panic("Cave length bad")
		}
		if _, ok := m.CaveMap[caves[0]]; !ok {
			addCave(caves[0], m)
		}
		if _, ok := m.CaveMap[caves[1]]; !ok {
			addCave(caves[1], m)
		}
		m.Routes = append(m.Routes, Route{Cave1: m.CaveMap[caves[0]], Cave2: m.CaveMap[caves[1]]})
		route := &m.Routes[len(m.Routes)-1]
		m.CaveMap[caves[0]].Routes = append(m.CaveMap[caves[0]].Routes, *route)
		m.CaveMap[caves[1]].Routes = append(m.CaveMap[caves[1]].Routes, *route)
	}
	return m
}

func newCaveMap(cave *Cave, cm map[string]bool) map[string]bool {
	nm := map[string]bool{cave.Name: true}
	for k, v := range cm {
		nm[k] = v
	}
	return nm
}

func checkForMatchingCell(p1 *Path, p2 *Path) bool {
	if len(p1.Caves) != len(p2.Caves) {
		return false
	}
	for k, c := range p1.Caves {
		if p2.Caves[k].Name != c.Name {
			return false
		}
	}
	return true
}

func checkForMatchingPath(path *Path, paths []*Path) bool {
	for _, p := range paths {
		if checkForMatchingCell(path, p) {
			return true
		}
	}
	return false
}

func goToCave(n *Cave, o *Cave, path *Path) bool {
	if n.Name == o.Name || n.Name == "start" {
		return false
	}

	if n.Large {
		return true
	}

	if _, ok := path.CaveMap[n.Name]; !ok {
		return true
	}

	return path.hasSmallTwice == false
}

func main() {
	data, err := os.ReadFile("./input")
	//data, err := os.ReadFile("./example1")
	if err != nil {
		panic(err)
	}

	rows := strings.Split(string(data), "\n")
	rows = rows[:len(rows)-1]

	m := parseMap(rows)

	for _, c := range m.Caves {
		fmt.Println("Cave ", c.Name, " l: ", c.Large, " nr: ", len(c.Routes))
	}

	for _, r := range m.Routes {
		fmt.Println("Route ", r.Cave1.Name, "-", r.Cave2.Name)
	}

	queue := []*Path{
		{
			Caves:         []*Cave{m.Start},
			CaveMap:       map[string]bool{m.Start.Name: true},
			hasSmallTwice: false,
		},
	}
	var finished []*Path
	for len(queue) > 0 {
		current := queue[0]
		queue = queue[1:]

		lastCave := current.Caves[0] //current.Caves[len(current.Caves)-1]

		if lastCave.Name == m.End.Name {
			if checkForMatchingPath(current, finished) == false {
				finished = append(finished, current)
			}
			continue
		}

		for _, r := range lastCave.Routes {
			if goToCave(r.Cave1, lastCave, current) {
				hasSmallTwice := current.hasSmallTwice || (!r.Cave1.Large && current.CaveMap[r.Cave1.Name])
				queue = append(queue, &Path{
					Caves:         append([]*Cave{r.Cave1}, current.Caves...), //append(current.Caves, r.Cave1),
					CaveMap:       newCaveMap(r.Cave1, current.CaveMap),
					hasSmallTwice: hasSmallTwice,
				})
			}
			if goToCave(r.Cave2, lastCave, current) {
				hasSmallTwice := current.hasSmallTwice || (!r.Cave2.Large && current.CaveMap[r.Cave2.Name])
				queue = append(queue, &Path{
					Caves:         append([]*Cave{r.Cave2}, current.Caves...), //append(current.Caves, r.Cave2),
					CaveMap:       newCaveMap(r.Cave2, current.CaveMap),
					hasSmallTwice: hasSmallTwice,
				})
			}
		}
	}

	fmt.Println("Num Paths: ", len(finished))
}
