SPACES: list[str] = []
FILE_VALUE: int = 0

line = open('9.2.txt').readlines()[0]
for i, n in enumerate(line.strip()):
    if i % 2 == 0:
        k = FILE_VALUE
        FILE_VALUE += 1
    else:
        k = "."
    for _ in range(int(n)):
        SPACES.append(k)


class EndOfSpaceError(Exception):
    pass


class NoMoreFilesFound(Exception):
    pass


def get_next_space(left_border: int, right_border: int) -> tuple[int, int]:
    i = left_border
    while True:
        if i >= right_border:
            raise EndOfSpaceError
        if SPACES[i] == ".":
            break
        i += 1

    j = i + 1
    while True:
        if j > right_border:
            raise EndOfSpaceError
        if SPACES[j] != ".":
            break
        j += 1
    return i, j


def get_next_file(right_border: int) -> tuple[int, int]:
    i = right_border
    while True:
        if i < 0:
            raise NoMoreFilesFound
        if SPACES[i] != ".":
            break
        i -= 1
    j = i - 1
    while True:
        if j < 0:
            raise NoMoreFilesFound
        if SPACES[j] != SPACES[i]:
            break
        j -= 1
    return j + 1, i + 1


def is_fitting(space: tuple[int, int], file: tuple[int, int]):
    return space[1] - space[0] >= file[1] - file[0]


def move_file(space_start: int, file: tuple[int, int]):
    for i in range(file[1] - file[0]):
        SPACES[space_start + i], SPACES[file[0] + i] = SPACES[file[0] + i], SPACES[space_start + i]


R = len(SPACES)-1
try:
    while file := get_next_file(R):
        S = 0
        try:
            while space := get_next_space(S, file[0]):
                if is_fitting(space, file):
                    move_file(space[0], file)
                    break
                S = space[1]
        except EndOfSpaceError:
            pass
        R = file[0] - 1
except NoMoreFilesFound:
    pass

C = 0
for i, n in enumerate(SPACES):
    if SPACES[i] != ".":
        C += i * int(n)
print(C)
# 6262891638328 too low
# 6287317016845 ?
# 6287317036313 too high
