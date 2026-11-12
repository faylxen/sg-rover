import unittest

from models import Rover
from parser import parse_input
from simulation import simulate


class ParserTests(unittest.TestCase):
    def test_invalid_inputs(self) -> None:
        for content in (
            "",
            "5",
            "five 5",
            "-1 5\n0 0 N\nM",
            "5 5",
            "5 5\n0 0 N",
            "5 5\n0 N\nM",
            "5 5\nx 0 N\nM",
            "5 5\n0 0 NE\nM",
            "5 5\n0 0 X\nM",
            "5 5\n6 0 N\nM",
            "5 5\n0 -1 N\nM",
            "5 5\n0 0 N\nMX",
            "5 5\n0 0 N\nM\n0 0 E\nM",
        ):
            with self.subTest(content=content):
                with self.assertRaises(ValueError):
                    parse_input(content)

    def test_empty_commands_on_single_cell_plateau(self) -> None:
        plateau, programs = parse_input("0 0\n0 0 N\n\n")
        self.assertEqual(simulate(plateau, programs), [Rover((0, 0), "N")])


if __name__ == "__main__":
    unittest.main()
