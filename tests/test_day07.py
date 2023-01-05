import os
from typing import List
from adventofcode.utils import read_file_strings
from adventofcode.day_07 import (
    Directory,
    File,
    Command,
    parse_command_line,
    process_commands,
)


class TestDay07:
    test_data_filename = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "resources",
        "day_07.txt",
    )

    def test_terminal_output(self):
        terminal_output: List[str] = read_file_strings(self.test_data_filename)
        commands: List[Command] = parse_command_line(terminal_output)
        assert len(commands) == 10

    def test_command_line_process(self):
        terminal_output: List[str] = read_file_strings(self.test_data_filename)
        commands: List[Command] = parse_command_line(terminal_output)
        root_dir = process_commands(commands)

        assert len(root_dir.directories) == 2
        assert len(root_dir.files) == 2
        assert root_dir.file_size() == 48381165

        dir_a = root_dir.get_dir("a")
        assert len(dir_a.directories) == 1
        assert len(dir_a.files) == 3
        assert dir_a.file_size() == 94853

        dir_e = dir_a.get_dir("e")
        assert len(dir_e.directories) == 0
        assert len(dir_e.files) == 1
        assert dir_e.file_size() == 584

        dir_d = root_dir.get_dir("d")
        assert len(dir_d.directories) == 0
        assert len(dir_d.files) == 4
        assert dir_d.file_size() == 24933642

    def test_dir_size_lte_100000(self):
        terminal_output: List[str] = read_file_strings(self.test_data_filename)
        commands: List[Command] = parse_command_line(terminal_output)
        root_dir = process_commands(commands)
        assert root_dir.sum_dirs_lte_n(n=100000) == 95437

    def test_all_dirs(self):
        terminal_output: List[str] = read_file_strings(self.test_data_filename)
        commands: List[Command] = parse_command_line(terminal_output)
        root_dir = process_commands(commands)

        disk_used = root_dir.file_size()
        disk_required = 30000000 - (70000000 - disk_used)
        assert disk_required == 8381165

        dirs = root_dir.dir_sizes()
        assert len(dirs.keys()) == 4

        dir, _ = min(
            [(k, v) for k, v in dirs.items() if v >= disk_required],
            key=lambda t: t[1],
        )
        assert dir == "d"
