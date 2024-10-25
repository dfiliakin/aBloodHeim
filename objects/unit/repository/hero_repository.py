import json
from pathlib import Path

from config import SAVE_FOLDER
from objects.unit import Hero


class HeroRepository:

    SAVE_FILE_POSTFIX = "_all_heroes.json"

    @classmethod
    def fetch_heroes_by_names(
        cls,
        hero_names: list[str],
        guild_name: str,
    ) -> list[Hero]:

        filename = guild_name + cls.SAVE_FILE_POSTFIX
        filepath = Path.joinpath(SAVE_FOLDER, filename)

        with open(filepath, "r") as f:
            all_heroes_data_json = json.load(f)

        heroes = []
        for hero_name in hero_names:
            hero = Hero.from_json(all_heroes_data_json.get(hero_name))
            heroes.append(hero)

        return heroes
