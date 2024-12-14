F: list[list[int]] = []

lines = open('14.1.txt').readlines()

HEIGHT = 103
WIDTH = 101
HEIGHT_MIDDLE = HEIGHT // 2
WIDTH_MIDDLE = WIDTH // 2


class Robot:
    def __init__(self, start: tuple[int, int], velocity: tuple[int, int]):
        self.start = start
        self.velocity = velocity
        self.current = start

    def move(self, time: int):
        self.current = (
            (self.current[0] + self.velocity[0] * time) % HEIGHT,
            (self.current[1] + self.velocity[1] * time) % WIDTH,
        )

    def quadrant(self) -> int | None:
        if 0 <= self.current[0] < HEIGHT_MIDDLE and 0 <= self.current[1] < WIDTH_MIDDLE:  # top left
            return 1
        if HEIGHT_MIDDLE < self.current[0] < HEIGHT and WIDTH_MIDDLE < self.current[1] < WIDTH:  # bottom right
            return 2
        if 0 <= self.current[0] < HEIGHT_MIDDLE and WIDTH_MIDDLE < self.current[1] < WIDTH:  # top right
            return 3
        if HEIGHT_MIDDLE < self.current[0] < HEIGHT and 0 <= self.current[1] < WIDTH_MIDDLE:  # bottom left
            return 4


ROBOTS: list[Robot] = []

for line in lines:
    p, v = line.strip().split(" ")
    x, y = list(map(int, p.split("=")[1].split(",")))
    vx, vy = list(map(int, v.split("=")[1].split(",")))
    ROBOTS.append(Robot((y, x), (vy, vx)))

quadrants = {}

for robot in ROBOTS:
    robot.move(100)
    quadrant = robot.quadrant()
    quadrants.setdefault(quadrant, 0)
    quadrants[quadrant] += 1

cost = 1
for quadrant, count in quadrants.items():
    if quadrant is not None:
        cost *= count
print(cost)
