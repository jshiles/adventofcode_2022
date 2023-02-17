import os
from adventofcode.utils import read_file_strings
from adventofcode.day_10 import CPU, execute_commands


class TestDay10:
    def test_example1(self):
        my_cpu = CPU()
        my_cpu.noop()
        my_cpu.addx(3)
        my_cpu.addx(-5)

        assert my_cpu.register_x == -1
        assert my_cpu.cycles == 5

    def test_signal_capture(self):
        test_data_filename = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "resources",
            "day_10.txt",
        )
        _, signal_strength, _ = execute_commands(
            read_file_strings(test_data_filename)
        )
        assert signal_strength == 13140

    def test_crt_display(self):
        test_data_filename = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "resources",
            "day_10.txt",
        )
        cpu, _, _ = execute_commands(read_file_strings(test_data_filename))
        assert len(cpu.crt.lines[0]) == 40
        assert cpu.crt.lines[0] == "##..##..##..##..##..##..##..##..##..##.."
        assert cpu.crt.lines[1] == "###...###...###...###...###...###...###."
        assert cpu.crt.lines[2] == "####....####....####....####....####...."
        assert cpu.crt.lines[3] == "#####.....#####.....#####.....#####....."
        assert cpu.crt.lines[4] == "######......######......######......####"
        assert cpu.crt.lines[5] == "#######.......#######.......#######....."
