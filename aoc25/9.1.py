from dataclasses import dataclass


@dataclass
class Tile:
    x: int
    y: int


def parse_red_tiles() -> list[Tile]:
    with open("9.1.txt", 'r') as data_file:
        lines = data_file.readlines()

    tiles = []
    for line in lines:
        x, y = line.strip().split(",")
        tile = Tile(int(x), int(y))
        tiles.append(tile)

    return tiles


def calc_area(a: Tile, b: Tile) -> int:
    ARRAY_TO_REAL_DELTA = 1
    x_delta = abs(a.x - b.x) + ARRAY_TO_REAL_DELTA
    y_delta = abs(a.y - b.y) + ARRAY_TO_REAL_DELTA
    return x_delta * y_delta


def solve():
    red_tiles = parse_red_tiles()

    max_area = 0
    for i, tile_a in enumerate(red_tiles):
        for tile_b in red_tiles[i+1:]:
            area = calc_area(tile_a, tile_b)
            if area > max_area:
                max_area = area

    print(max_area)


solve()
