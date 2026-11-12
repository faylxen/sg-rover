from models import DIRECTIONS, MIN_COORDINATE, Plateau, Position, Program, Rover

PLATEAU_COORDINATE_COUNT = 2
ROVER_FIELD_COUNT = 3
ROVER_LINE_COUNT = 2


def parse_input(content: str) -> tuple[Plateau, list[Program]]:
    lines = content.splitlines()
    if not lines:
        raise ValueError("Le fichier est vide.")

    dimensions = lines[0].split()
    if len(dimensions) != PLATEAU_COORDINATE_COUNT:
        raise ValueError("Le plateau doit avoir deux coordonnées.")

    max_x, max_y = map(int, dimensions)
    if max_x < MIN_COORDINATE or max_y < MIN_COORDINATE:
        raise ValueError("Les limites du plateau doivent être positives ou nulles.")

    plateau = Plateau(max_x, max_y)
    rover_line_count = len(lines) - 1
    if rover_line_count < ROVER_LINE_COUNT or rover_line_count % ROVER_LINE_COUNT != 0:
        raise ValueError(
            "Chaque rover doit avoir une position et une ligne de commandes."
        )

    occupied: set[Position] = set()
    programs: list[Program] = []

    for index in range(1, len(lines), ROVER_LINE_COUNT):
        values = lines[index].split()
        if len(values) != ROVER_FIELD_COUNT:
            raise ValueError(f"Position invalide à la ligne {index + 1}.")

        x, y, direction = values
        position = (int(x), int(y))
        commands = lines[index + 1].strip()

        if direction not in DIRECTIONS:
            raise ValueError(f"Direction invalide : {direction}.")
        if not plateau.contains(position):
            raise ValueError(f"Position hors du plateau : {position}.")
        if position in occupied:
            raise ValueError(f"Position déjà occupée : {position}.")
        if any(command not in "LRM" for command in commands):
            raise ValueError(f"Commande invalide à la ligne {index + 2}.")

        occupied.add(position)
        programs.append((Rover(position, direction), commands))

    return plateau, programs
