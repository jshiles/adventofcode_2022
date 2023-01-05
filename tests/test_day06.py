import os
from typing import List
from adventofcode.day_06 import (
    packet_marker_detection,
    message_start_detection,
)


class TestDay06:
    test_data_filename = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "resources",
        "day_06.txt",
    )

    def test_packet_marker_detection(self):
        assert packet_marker_detection("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7
        assert packet_marker_detection("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
        assert packet_marker_detection("nppdvjthqldpwncqszvftbrmjlhg") == 6
        assert (
            packet_marker_detection("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
        )
        assert (
            packet_marker_detection("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11
        )

    def test_packet_message_detection(self):
        assert message_start_detection("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 19
        assert message_start_detection("bvwbjplbgvbhsrlpgdmjqwftvncz") == 23
        assert message_start_detection("nppdvjthqldpwncqszvftbrmjlhg") == 23
        assert (
            message_start_detection("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 29
        )
        assert (
            message_start_detection("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 26
        )
