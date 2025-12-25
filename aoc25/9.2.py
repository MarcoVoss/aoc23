from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Tile:
    x: int
    y: int


def parse_red_tiles() -> list[Tile]:
    with open("9.2.txt", 'r') as data_file:
        lines = data_file.readlines()

    tiles = []
    for line in lines:
        x, y = line.strip().split(",")
        tile = Tile(int(x), int(y))
        tiles.append(tile)

    return tiles


def get_edge_green_tiles(tiles: list[Tile]) -> list[Tile]:
    edge_tiles: list[Tile] = []
    for i, tile_a in enumerate(tiles):
        for tile_b in tiles[i+1:]:
            x_delta = 0
            y_delta = 0
            steps = 0

            if tile_a.x == tile_b.x:
                y_delta = -1 if tile_a.y > tile_b.y else 1
                steps = abs(tile_a.y - tile_b.y)

            if tile_a.y == tile_b.y:
                x_delta = -1 if tile_a.x > tile_b.x else 1
                steps = abs(tile_a.x - tile_b.x)

            if x_delta != 0 or y_delta != 0:
                for step in range(steps):
                    current_position = (tile_a.x + step * x_delta, tile_a.y + step * y_delta)
                    tile = Tile(*current_position)
                    edge_tiles.append(tile)

    return edge_tiles


def calc_area(a: Tile, b: Tile) -> int:
    ARRAY_TO_REAL_DELTA = 1
    x_delta = abs(a.x - b.x) + ARRAY_TO_REAL_DELTA
    y_delta = abs(a.y - b.y) + ARRAY_TO_REAL_DELTA
    return x_delta * y_delta


def get_surrounding_tiles(all_tiles: list[Tile]) -> list[Tile]:
    plain_positions = set((tile.x, tile.y) for tile in all_tiles)

    inner_and_outer_positions: set[tuple[int, int]] = set()
    for tile in all_tiles:
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                if x == 0 and y == 0:
                    continue
                position = (tile.x + x, tile.y + y)
                if position not in plain_positions:
                    inner_and_outer_positions.add(position)

    first_tile = all_tiles[0]
    first_outer_position = None
    for x in range(first_tile.x):
        if (x, first_tile.y) in inner_and_outer_positions:
            first_outer_position = (x, first_tile.y)
            break

    all_outer_positions = set([first_outer_position])
    current_outer_position = first_outer_position
    for _ in range(len(inner_and_outer_positions)):
        x, y = current_outer_position
        adjacent_positions = [
            (x, y + 1),
            (x, y - 1),
            (x + 1, y),
            (x - 1, y),
        ]
        for adjacent_position in adjacent_positions:
            if adjacent_position in inner_and_outer_positions and adjacent_position not in all_outer_positions:
                current_outer_position = adjacent_position
                all_outer_positions.add(adjacent_position)

        if current_outer_position == first_outer_position:
            break

    all_outer_tiles = [
        Tile(*outer_position)
        for outer_position in all_outer_positions
    ]
    return all_outer_tiles


def is_valid(surrounding_tiles: list[Tile], tile_a: Tile, tile_b: Tile):
    max_x = max(tile_a.x, tile_b.x)
    min_x = min(tile_a.x, tile_b.x)
    max_y = max(tile_a.y, tile_b.y)
    min_y = min(tile_a.y, tile_b.y)

    for tile in surrounding_tiles:
        if (
            min_x < tile.x < max_x and
            min_y < tile.y < max_y
        ):
            return False
    return True


def solve():
    max_area = 0
    red_tiles = parse_red_tiles()
    edge_green_tiles = get_edge_green_tiles(red_tiles)
    surrounding_tiles = get_surrounding_tiles(red_tiles + edge_green_tiles)

    for i, tile_a in enumerate(red_tiles):
        for tile_b in red_tiles[i+1:]:
            if is_valid(surrounding_tiles, tile_a, tile_b):
                max_area = max(max_area, calc_area(tile_a, tile_b))

    print(max_area)


solve()
