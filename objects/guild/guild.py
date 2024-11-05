from typing import TYPE_CHECKING
from objects.unit.repository import HeroRepository

if TYPE_CHECKING:
    from objects.unit import Hero


class Resources:
    def __init__(self, gold=0, mana=0, materials=0):
        self.gold = gold
        self.mana = mana
        self.materials = materials


class Guild:

    def __init__(
        self,
        name: str,
        resources: Resources,
        heroes: list["Hero"],
    ):
        self.name = name
        self.resources = resources
        self.heroes = heroes

    @classmethod
    def from_json(cls, json_data):
        return cls(
            name=json_data["name"],
            resources=Resources(**json_data["resources"]),
            heroes=HeroRepository.fetch_heroes_by_names(
                hero_names=json_data.get("hero_names", []),
                guild_name=json_data["name"],
            ),
        )

    def __str__(self):
        return f" - GUILD - {self.name} ({self.resources}; heroes: {len(self.heroes)})"
