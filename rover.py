import argparse
import sys
from pathlib import Path

from parser import parse_input
from simulation import simulate

SUCCESS_CODE = 0
FAILURE_CODE = 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=Path)
    args = parser.parse_args()

    try:
        content = args.input_file.read_text(encoding="utf-8")
        plateau, programs = parse_input(content)
    except (OSError, ValueError) as error:
        print(f"Erreur : {error}", file=sys.stderr)
        return FAILURE_CODE

    for rover in simulate(plateau, programs):
        x, y = rover.position
        print(f"{x} {y} {rover.direction}")

    return SUCCESS_CODE


if __name__ == "__main__":
    sys.exit(main())
