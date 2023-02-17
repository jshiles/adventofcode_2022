from dataclasses import dataclass, field
from typing import List, Tuple


@dataclass
class CRTDisplay:
    lines: List[str] = field(default_factory=list)

    def add_cycle(self, x: int):
        """ """
        row_idx = len(self.lines) - 1
        if row_idx < 0 or len(self.lines[row_idx]) == 40:
            self.lines.append("")
            row_idx += 1

        col_idx = len(self.lines[row_idx])
        self.lines[row_idx] = self.lines[row_idx] + (
            "#" if x - 1 <= col_idx <= x + 1 else "."
        )


@dataclass
class CPU:
    register_x: int = field(default=1)
    cycles: int = field(default=0)
    signal_strengths: List[int] = field(default_factory=list)
    crt: CRTDisplay = field(default=None)

    def addx(self, v: int) -> int:
        """
        addx V takes two cycles to complete. After two cycles, the X register
        is increased by the value V. (V can be negative.)
        """
        for _ in range(self.cycles + 1, self.cycles + 3):
            self.increment_cycle()
        self.register_x += v
        return self.register_x

    def noop(self):
        """
        noop takes one cycle to complete. It has no other effect.
        """
        self.increment_cycle()

    def increment_cycle(self):
        self.cycles += 1
        self.capture_signal()
        self.add_to_crt()

    def capture_signal(self) -> bool:
        """
        captures the signal during the 20th cycle and every 40 cycles after
        that (that is, during the 20th, 60th, 100th, 140th, 180th, and 220th
        cycles).
        """
        if self.cycles == 20 or ((self.cycles - 20) % 40 == 0):
            self.signal_strengths.append(self.register_x * self.cycles)

    def sum_signal_strength(self) -> int:
        return sum(self.signal_strengths)

    def add_to_crt(self):
        """ """
        if self.crt is None:
            self.crt = CRTDisplay()
        self.crt.add_cycle(self.register_x % 40)


def execute_commands(commands: List[str]) -> Tuple[CPU, int, int]:
    my_cpu = CPU()
    for instr in commands:
        if instr.lower().startswith("noop"):
            my_cpu.noop()
        elif instr.lower().startswith("addx"):
            _, arg = instr.strip().split(" ")
            my_cpu.addx(int(arg))
    return (my_cpu, my_cpu.sum_signal_strength(), my_cpu.register_x)
