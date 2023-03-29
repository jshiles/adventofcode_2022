from __future__ import annotations
import shapely
from dataclasses import dataclass
from typing import List


@dataclass(eq=True, order=True, frozen=True)
class Coordinate:
    x: int
    y: int

    def manh_distance(self, other: Coordinate) -> int:
        """Returns the manhatten distance between two coordiantes."""
        return abs(self.x - other.x) + abs(self.y - other.y)

    def tuning_frequency(self) -> int:
        """
        To isolate the distress beacon's signal, you need to determine its tuning
        frequency, which can be found by multiplying its x coordinate by 4000000
        and then adding its y coordinate.
        """
        return self.x * 4000000 + self.y


@dataclass(eq=True, order=True, frozen=True)
class Sensor:
    location: Coordinate
    closest_beacon: Coordinate

    def create_polygon(self) -> shapely.Polygon:
        """
        Use shapely package to create a Polygon from the most extreme points,
        computed using manhattan distance from the sensor.
        """
        manh_dist = self.location.manh_distance(self.closest_beacon)
        left = shapely.Point(self.location.x - manh_dist, self.location.y)
        right = shapely.Point(self.location.x + manh_dist, self.location.y)
        upper = shapely.Point(self.location.x, self.location.y - manh_dist)
        lower = shapely.Point(self.location.x, self.location.y + manh_dist)
        return shapely.Polygon((left, upper, right, lower))


def no_beacon(sensors: List[Sensor], y: int = 2000000) -> List[Coordinate]:
    """ 
    Find the locatins on the line denoted by 'y' where a beacon cannot exist.
    Returns:
        List[Coordinate], Coordinates where beacons cannot exist.
    """
    sensor_locations = [s.location for s in sensors]
    beacon_locations = [s.closest_beacon for s in sensors]

    sensor_mesh = shapely.union_all([s.create_polygon() for s in sensors])
    min_x = min(
        [
            int(s.x)
            for s in shapely.points(sensor_mesh.exterior.coords).tolist()
        ]
    )
    max_x = max(
        [
            int(s.x)
            for s in shapely.points(sensor_mesh.exterior.coords).tolist()
        ]
    )
    search_area = search_area = shapely.geometry.box(
        min_x - 1, y - 1, max_x + 1, y + 1
    )
    remaining = shapely.intersection(search_area, sensor_mesh)

    points: List[Coordinate] = []
    for x in range(min_x, max_x + 1):
        p = shapely.Point(x, y)
        if (
            shapely.within(p, remaining) or shapely.touches(remaining, p)
        ) and Coordinate(x, y) not in sensor_locations + beacon_locations:
            points.append(Coordinate(x, y))
    return points


def find_distress_beacon(
    sensors: List[Sensor], min_xy: int = 0, max_xy: int = 20
) -> Coordinate:
    """
    Returns the location of the distress beacon; assumes only one is possible.
    Returns:
        Coordiante, the location of the distress beacon
    """
    # subtract the total space created by sensors and beacons, search mesh,
    # from the given search area.
    search_area = shapely.geometry.box(min_xy, min_xy, max_xy, max_xy)
    sensor_mesh = shapely.union_all([s.create_polygon() for s in sensors])
    remaining = shapely.difference(search_area, sensor_mesh)

    return Coordinate(
        int(remaining.point_on_surface().x),
        int(remaining.point_on_surface().y),
    )
