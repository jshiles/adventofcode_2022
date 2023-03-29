import os
import re
from typing import List
from adventofcode.utils import read_file_strings
from adventofcode.day_15 import (
    Sensor,
    Coordinate,
    no_beacon,
    find_distress_beacon,
)

import numpy as np


def main():
    filename = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "resources",
        "day_15.txt",
    )

    # Part 1
    sensors: List[Sensor] = []
    for line in read_file_strings(filename):
        (sensor_x, sensor_y), (beacon_x, beacon_y) = re.findall(
            r"x=(-{0,1}\d+), y=(-{0,1}\d+)", line
        )
        s = Sensor(
            Coordinate(int(sensor_x), int(sensor_y)),
            Coordinate(int(beacon_x), int(beacon_y)),
        )
        sensors.append(s)
    print(len(no_beacon(sensors, y=2000000)))  # 5100463

    # Part 2
    coord = find_distress_beacon(sensors, max_xy=4000000)
    print(coord.tuning_frequency())  # 11557863040754


if __name__ == "__main__":
    main()
