from models import Plateau, Program, Rover


def simulate(plateau: Plateau, programs: list[Program]) -> list[Rover]:
    occupied = {rover.position for rover, _ in programs}

    for rover, commands in programs:
        for command in commands:
            if command in "LR":
                rover.turn(command)
                continue

            position = rover.next_position()
            if plateau.contains(position) and position not in occupied:
                occupied.remove(rover.position)
                occupied.add(position)
                rover.position = position

    return [rover for rover, _ in programs]
