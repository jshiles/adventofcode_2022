from __future__ import annotations
from dataclasses import dataclass, field
from functools import reduce
from typing import List, Union
import deepdiff
import re


class PacketData:
    input: List[Union[PacketData, int]]  # = field(default_factory=list)

    def __init__(self, data: list) -> None:
        self.input = data

        if len(self.input) == 1 and isinstance(self.input[0], str):
            self.input[0] = int(self.input[0]) if self.input[0] != "" else -1
        else:
            for idx, e in enumerate(self.input):
                if isinstance(e, str):
                    self.input[idx] = int(e)

    def __eq__(self, __o: object) -> bool:
        if (
            isinstance(self, PacketData)
            and isinstance(__o, PacketData)
            and len(deepdiff.DeepDiff(self, __o).keys()) == 0
        ):
            return True
        return False

    def __le__(self, __o: object) -> bool:
        """ """
        return self.compare(__o)

    def compare(self, __o: object) -> bool:
        # print(f"Compare {self} and {__o}")
        for x in range(min(len(self.input), len(__o.input))):
            # print(
            #     f"  -> Loop {self.input[x]} and {__o.input[x]} "
            #     f"range({min(len(self.input), len(__o.input))})"
            # )
            if (
                isinstance(self.input[x], int)
                and isinstance(__o.input[x], int)
                and self.input[x] != __o.input[x]
            ):
                return self.input[x] < __o.input[x]

            elif (
                isinstance(self.input[x], int)
                and isinstance(__o.input[x], PacketData)
                and not PacketData([self.input[x]]) == __o.input[x]
            ):
                return PacketData([self.input[x]]) <= __o.input[x]

            elif (
                isinstance(self.input[x], PacketData)
                and isinstance(__o.input[x], int)
                and not self.input[x] == PacketData([__o.input[x]])
            ):
                return self.input[x] <= PacketData([__o.input[x]])

            elif (
                isinstance(self.input[x], PacketData)
                and isinstance(__o.input[x], PacketData)
                and not self.input[x] == __o.input[x]
            ):
                return self.input[x] <= __o.input[x]

        if __o.length() < self.length():
            return False

        return True

    def length(self) -> int:
        return len(self.input) + sum(
            [x.length() for x in self.input if isinstance(x, PacketData)]
        )

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.input})"


def _parse_packet_recursive(data):
    max_open = max([i for i, x in enumerate(data) if x == "["])
    match_close = min(
        [i for i, x in enumerate(data) if x == "]" and i > max_open]
    )
    if match_close == len(data) - 1:
        # we've reached the end.
        return data
    else:
        return _parse_packet_recursive(
            data[:max_open]
            + [PacketData(data[max_open + 1 : match_close])]
            + data[match_close + 1 :]
        )


def str2packetdata(init_data: str) -> PacketData:
    def _str2list(x: str):
        return x.replace("[", "[,").replace("]", ",]").split(",")

    init_list = _str2list(init_data)
    return PacketData(_parse_packet_recursive(init_list)[1:-1])
