from collections import Counter
from dataclasses import dataclass
import math


@dataclass
class Box:
    id: int
    x: int
    y: int
    z: int
    circuit_id: int

    def __str__(self):
        return f"{self.x},{self.y},{self.z}"


@dataclass
class Connection:
    box_a: Box
    box_b: Box
    distance: int


def parse_boxes() -> list[Box]:
    with open("8.2.txt", 'r') as data_file:
        lines = data_file.readlines()

    boxes = []
    for index, line in enumerate(lines):
        x, y, z = list(map(int, line.strip().split(",")))
        box = Box(index, x, y, z, index)
        boxes.append(box)

    return boxes


def distance(box_a: Box, box_b: Box) -> int:
    x_delta = (box_b.x - box_a.x)**2
    y_delta = (box_b.y - box_a.y)**2
    z_delta = (box_b.z - box_a.z)**2
    distance = math.sqrt(x_delta + y_delta + z_delta)
    return distance


def connect_boxes(boxes: list[Box], connection: Connection) -> None:
    old_circuit_id = connection.box_a.circuit_id
    new_circuit_id = connection.box_b.circuit_id

    for box in boxes:
        if box.circuit_id == old_circuit_id:
            box.circuit_id = new_circuit_id


def collect_connections(boxes: list[Box]):
    possible_connections: list[Connection] = []
    for left_border, box_a in enumerate(boxes):
        for box_b in boxes[left_border+1:]:
            box_distance = distance(box_a, box_b)
            connection = Connection(box_a, box_b, box_distance)
            possible_connections.append(connection)
    return possible_connections


def sort_connections_by_distance_desc(connections: list[Connection]):
    return list(sorted(connections, key=lambda x: x.distance))


def is_single_circuit(boxes: list[Box]) -> bool:
    all_circuit_ids = [box.circuit_id for box in boxes]
    counter = Counter(all_circuit_ids)
    filled_circuits = set(counter.values()) - {0}
    return len(filled_circuits) == 1


def solve():
    BOXES = parse_boxes()
    possible_connections = collect_connections(BOXES)
    sorted_connections = sort_connections_by_distance_desc(possible_connections)

    for connection in sorted_connections:
        if connection.box_a.circuit_id == connection.box_b.circuit_id:
            continue

        connect_boxes(BOXES, connection)

        if is_single_circuit(BOXES):
            print(connection.box_a.x * connection.box_b.x)
            break


solve()
