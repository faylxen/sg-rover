# Mars Rovers

Python 3.10 minimum. Aucune dépendance pour lancer le programme.

```bash
python rover.py input.txt
```

## Organisation

- `models.py` : plateau, rover et positions.
- `parser.py` : lecture et validation du contenu du fichier.
- `simulation.py` : exécution séquentielle des commandes et collisions.
- `rover.py` : arguments, lecture du fichier et affichage.
- `tests/test_rover.py` : rotations, déplacements, bordures et collisions.
- `tests/test_parser.py` : validation des entrées.
- `tests/test_cli.py` : lancement en ligne de commande et affichage.

## Règles ajoutées à l'énoncé

Les limites sont inclusives. Un mouvement hors du plateau ou vers une case
occupée est ignoré, puis les commandes suivantes sont exécutées. Tous les rovers
occupent leur case, y compris ceux qui attendent et ceux qui ont terminé.
Une case libérée peut être réutilisée.

Les entrées invalides sont refusées avant de déplacer les rovers. Il faut au moins
un rover. Une ligne de commandes vide est acceptée. Le plateau `0 0` contient
une seule case.

Les positions sont des tuples `(x, y)`. Un ensemble contient uniquement les
positions occupées : aucune grille complète n'est créée en mémoire.
La simulation modifie les objets rover reçus.

## Outils de développement

Poetry gère les dépendances de développement définies dans `pyproject.toml`.
La première installation génère `poetry.lock`, à conserver dans le dépôt.

```bash
poetry install
poetry run pytest
poetry run ruff check .
poetry run ruff format --check .
```

```bash
poetry run pre-commit install
poetry run pre-commit run --all-files
```
