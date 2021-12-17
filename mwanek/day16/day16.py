from collections import defaultdict, deque
import numpy as np

with open("input.txt", "r", encoding="utf-8") as file:
    data = file.read().strip()

class Transmission:
    def __init__(self, raw_input) -> None:
        self.raw_input = raw_input
        self.parsed = False
        self.bytes = deque()
        self.buffer = ""

    def parse_hex(self) -> None:    #Convert hex into binary string in self.bytes
        if not self.parsed:
            for char in self.raw_input:
                self.bytes.append(format(int(char, 16), '0>4b'))
            self.parsed = True
            return self

    def parse_bin(self) -> None:    #Slice binary string into self.bytes
        if not self.parsed:
            bit_length = len(self.raw_input)
            remainder = bit_length % 4
            if remainder:     # If length isn't divisble by four
                bit_length = bit_length - remainder + 4   # Extend length to next divisor
            bin_input = format(self.raw_input, f'0<{bit_length}') # Add trailing zeros
            for i in range(0,bit_length, 4):
                self.bytes.append(bin_input[i:i+4]) # Add bytes in slices of 4
            self.parsed = True
            return self

    def get(self, amt) -> str: #Fill buffer until large enough for requested bits
        while len(self.buffer) < amt:
            self.buffer += self.bytes.popleft()
        bits, self.buffer = self.buffer[:amt], self.buffer[amt:]
        return bits

    def get_int(self, amt) -> str: # Do a get, but convert to integer
        return int(self.get(amt), 2)

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

def parse_packets(tx: Transmission):
    pver_sum = 0
    packets = []
    pver, ptype = tx.get_int(3), tx.get_int(3)
    pver_sum += pver
    match PTYPES[ptype]:
        case "literal":
            num = ""
            read_more = tx.get_int(1)
            num += tx.get(4)
            while read_more:
                read_more = tx.get_int(1)
                num += tx.get(4)
            packets.append(int(num, 2))
        case "operator":
            ltype = tx.get_int(1)
            packet = []
            match ltype:
                case 0:
                    bit_length = tx.get_int(15)
                    sub_tx = Transmission(tx.get(bit_length)).parse_bin()
                    while sub_tx.bytes:
                        sub_packet, sub_pver = parse_packets(sub_tx)
                        pver_sum += sub_pver
                        packet += sub_packet
                case 1:
                    num_packets = tx.get_int(11)
                    for _ in range(num_packets):
                        next_packet, next_pver = parse_packets(tx)
                        pver_sum += next_pver
                        packet += next_packet
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
                    packet = 1 if packet[0] > packet[1] else 0
                case "less":
                    packet = 1 if packet[0] < packet[1] else 0
                case "equal":
                    packet = 1 if packet[0] == packet[1] else 0
            packets.append(packet)
    return packets, pver_sum

p2_answer, p1_answer = parse_packets(Transmission(data).parse_hex())
p2_answer = p2_answer[0]

print("Part 1, sum of packet versions:", p1_answer)
print("Part 2, evaluated transmission:", p2_answer)
