from dataclasses import dataclass

Position = tuple[int, int]

MIN_COORDINATE = 0
DIRECTIONS = ("N", "E", "S", "W")
MOVEMENTS: dict[str, Position] = {
    "N": (0, 1),
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0),
}


@dataclass(frozen=True)
class Plateau:
    max_x: int
    max_y: int

    def contains(self, position: Position) -> bool:
        x, y = position
        return MIN_COORDINATE <= x <= self.max_x and MIN_COORDINATE <= y <= self.max_y


@dataclass
class Rover:
    position: Position
    direction: str

    def turn(self, command: str) -> None:
        index = DIRECTIONS.index(self.direction)
        rotation = -1 if command == "L" else 1
        self.direction = DIRECTIONS[(index + rotation) % len(DIRECTIONS)]

    def next_position(self) -> Position:
        x, y = self.position
        dx, dy = MOVEMENTS[self.direction]
        return x + dx, y + dy


Program = tuple[Rover, str]
