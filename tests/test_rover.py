import unittest

from models import Plateau, Rover
from simulation import simulate


class RoverTests(unittest.TestCase):
    def test_turns(self) -> None:
        for direction, left, right in (
            ("N", "W", "E"),
            ("E", "N", "S"),
            ("S", "E", "W"),
            ("W", "S", "N"),
        ):
            for command, expected in (("L", left), ("R", right)):
                with self.subTest(direction=direction, command=command):
                    rover = Rover((2, 2), direction)
                    rover.turn(command)
                    self.assertEqual(rover.direction, expected)
                    self.assertEqual(rover.position, (2, 2))

    def test_forward_in_each_direction(self) -> None:
        for direction, expected in (
            ("N", (2, 3)),
            ("E", (3, 2)),
            ("S", (2, 1)),
            ("W", (1, 2)),
        ):
            with self.subTest(direction=direction):
                rover = Rover((2, 2), direction)
                simulate(Plateau(5, 5), [(rover, "M")])
                self.assertEqual(rover.position, expected)
                self.assertEqual(rover.direction, direction)

    def test_all_borders_block_movement(self) -> None:
        for position, direction in (
            ((2, 5), "N"),
            ((5, 2), "E"),
            ((2, 0), "S"),
            ((0, 2), "W"),
        ):
            with self.subTest(direction=direction):
                rover = Rover(position, direction)
                simulate(Plateau(5, 5), [(rover, "M")])
                self.assertEqual(rover.position, position)

    def test_continues_after_blocked_movement(self) -> None:
        rover = Rover((0, 0), "S")
        simulate(Plateau(2, 2), [(rover, "MLM")])
        self.assertEqual(rover, Rover((1, 0), "E"))

    def test_collision_with_waiting_rover(self) -> None:
        first = Rover((0, 0), "E")
        second = Rover((1, 0), "N")
        simulate(Plateau(2, 2), [(first, "MLM"), (second, "M")])
        self.assertEqual(first.position, (0, 1))
        self.assertEqual(second.position, (1, 1))

    def test_collision_with_finished_rover(self) -> None:
        first = Rover((0, 0), "E")
        second = Rover((2, 0), "W")
        simulate(Plateau(2, 2), [(first, "M"), (second, "M")])
        self.assertEqual(first.position, (1, 0))
        self.assertEqual(second.position, (2, 0))

    def test_vacated_position_becomes_free(self) -> None:
        first = Rover((1, 0), "N")
        second = Rover((0, 0), "E")
        simulate(Plateau(2, 2), [(first, "M"), (second, "M")])
        self.assertEqual(first.position, (1, 1))
        self.assertEqual(second.position, (1, 0))


if __name__ == "__main__":
    unittest.main()
