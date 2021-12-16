from collections import defaultdict, deque
import numpy as np

with open("input.txt", "r", encoding="utf-8") as file:
    data = file.read().strip()

class Transmission:
    def __init__(self, hex_input) -> None:
        self.bytes = deque()
        for char in hex_input:
            self.bytes.append(format(int(char, 16), '0>4b'))
        self.buffer = ""
    def get(self, amt) -> str:
        while len(self.buffer) < amt:
            self.buffer += self.bytes.popleft()
        bits, self.buffer = self.buffer[:amt], self.buffer[amt:]
        return bits
    def clear_buffer(self) -> None:
        self.buffer = ""

class SubTransmission(Transmission):
    def __init__(self, bin_input) -> None:
        bit_length = len(bin_input)
        rem = bit_length % 4
        if rem:
            bit_length = bit_length - rem + 4
        bin_input = format(bin_input, f'0<{bit_length}')

        self.bytes = deque()
        for i in range(0,bit_length, 4):
            self.bytes.append(bin_input[i:i+4])
        self.buffer = ""

PTYPES = defaultdict(lambda:"operator")
PTYPES[4] = "literal"
OTYPES = {  0: "sum",
            1: "product",
            2: "minimum",
            3: "maximum",
            5: "greater",
            6: "less",
            7: "equal"
}

def parse_packets(x: Transmission):
    pver_sum = 0
    packets = []
    int_bits = lambda i: int(x.get(i), 2)
    pver, ptype = int_bits(3), int_bits(3)
    pver_sum += pver

    match PTYPES[ptype]:
        case "literal":
            num = ""
            read_more = int_bits(1)
            num += x.get(4)
            while read_more:
                read_more = int_bits(1)
                num += x.get(4)
            packets.append(int(num, 2))
        case "operator":
            ltype = int_bits(1)
            packet = []
            match ltype:
                case 0:
                    bit_length = int_bits(15)
                    sub = SubTransmission(x.get(bit_length))
                    while sub.bytes:
                        sub_packet, sub_pver = parse_packets(sub)
                        sub_packet = sub_packet.pop()
                        pver_sum += sub_pver
                        packet.append(sub_packet)
                case 1:
                    num_packets = int_bits(11)
                    for _ in range(num_packets):
                        sub_packet, sub_pver = parse_packets(x)
                        sub_packet = sub_packet.pop()
                        pver_sum += sub_pver
                        packet.append(sub_packet)
            match OTYPES[ptype]:
                case "sum":
                    packet = sum(packet)
                case "product":
                    packet = np.product(packet)
                case "minimum":
                    packet = min(packet)
                case "maximum":
                    packet = max(packet)
                case "greater":
                    packet = 1 if packet[0] > packet [1] else 0
                case "less":
                    packet = 1 if packet[0] < packet [1] else 0
                case "equal":
                    packet = 1 if packet[0] == packet [1] else 0
            packets.append(packet)
    return packets, pver_sum

p2_answer, p1_answer = parse_packets(Transmission(data))
p2_answer = p2_answer[0]

print("Part 1, sum of packet versions:", p1_answer)
print("Part 2, evaluated transmission:", p2_answer)
