from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
import logging


@dataclass
class File:
    name: str
    size: int


@dataclass
class Directory:
    name: str = field(default="/")
    files: List[File] = field(default_factory=list)
    directories: List[Directory] = field(default_factory=list)

    def get_dir(self, name: str) -> Optional[Directory]:
        for dir in self.directories:
            if dir.name == name:
                return dir
        return None

    def file_size(self) -> int:
        """ """
        file_size = (
            0 if not len(self.files) else sum([f.size for f in self.files])
        )
        dir_size = sum([d.file_size() for d in self.directories])
        return file_size + dir_size

    def sum_dirs_lte_n(self, n: int = 100000):
        sum = 0
        for d in self.directories:
            sum += d.file_size() if d.file_size() <= n else 0
            sum += d.sum_dirs_lte_n(n)
        return sum

    def dir_sizes(self, n: int = 100000) -> dict:
        dirs: dict = {}
        dirs[self.name] = self.file_size()
        for d in self.directories:
            dirs = dirs | d.dir_sizes()
        return dirs


@dataclass
class Command:
    command: str
    output: List[str] = field(default_factory=list)


def parse_command_line(terminal_output: List[str]) -> List[Command]:
    """ """
    if terminal_output[0].strip() != "$ cd /":
        raise ValueError("First command must take us to root.")

    commands: List[Command] = []
    active_command = None

    for term_line in terminal_output[1:]:
        if term_line.startswith("$") and active_command is not None:
            commands.append(active_command)
        if term_line.startswith("$"):
            active_command = Command(term_line.strip())
        elif len(term_line.strip()):
            active_command.output.append(term_line.strip())
    if active_command is not None:
        commands.append(active_command)

    return commands


def _process_commands_recursive(
    active_dir: Directory, commands: List[Command], root_dir: Directory
) -> int:
    if len(commands) == 0:
        return 0

    else:
        commands_processed = 0

        while commands_processed < len(commands):
            cmd = commands[commands_processed]

            if cmd.command == "$ ls":
                for line in cmd.output:
                    if line.startswith("dir"):
                        _, name = line.strip().split(" ")
                        active_dir.directories.append(Directory(name))
                    else:
                        size, name = line.strip().split(" ")
                        active_dir.files.append(File(name, int(size)))
                commands_processed = commands_processed + 1

            elif cmd.command.startswith("$ cd .."):
                commands_processed = commands_processed + 1
                if root_dir != active_dir:
                    return commands_processed

            elif cmd.command.startswith("$ cd"):
                commands_processed = commands_processed + 1
                _, _, name = cmd.command.strip().split(" ")
                commands_processed += _process_commands_recursive(
                    active_dir.get_dir(name),
                    commands[commands_processed:],
                    root_dir,
                )

        return commands_processed


def process_commands(commands: List[Command]) -> Directory:
    """ """
    root_dir = Directory()
    commands_processed = _process_commands_recursive(
        root_dir, commands, root_dir
    )
    logging.debug(f"commands: {commands_processed}")
    return root_dir
