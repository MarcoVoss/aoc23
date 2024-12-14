F: list[list[int]] = []

lines = open('14.2.txt').readlines()

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

t = 0
p = 1

# when looking into the first 100 images:
# there are 2 patterns where only the first occurrence is different for everyone
# one every 103 steps (first at 53)
# one every 101 steps (first at 98)
# we can still use try and error to find the lcm
# 98 + 101 * p = 53 + 103 * g  =>  (45 + 101 * p) / 103
# Offensichtlich geklaut aus den Lösungen xd
# Ich hab bei 7200 aufeghört mir die Bilder anzuschauen
# Lösung war 7572... Typisch
while True:
    if (45 + 101*p) % 103 == 0:
        t = 98 + 101*p
        break
    p += 1

for robot in ROBOTS:
    robot.move(t)

current = set([robot.current for robot in ROBOTS])
for i in range(HEIGHT):
    print("".join(["#" if (i, j) in current else " " for j in range(WIDTH)]))
