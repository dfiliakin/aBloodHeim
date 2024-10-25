from .unit import Unit


# FIXME: use ORM, db, and sqlalchemy
class Hero(Unit):
    def __init__(
        self,
        name: str,
        hp: int,
        lvl: int,
        race: str,
        klass: str,
        descritpion: str,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.name = name
        self.hp = hp
        self.lvl = lvl
        self.race = race
        self.klass = klass
        self.descritpion = descritpion

    @classmethod
    def from_json(cls, json_data):
        return cls(
            name=json_data["name"],
            hp=json_data["hp"],
            lvl=json_data["lvl"],
            race=json_data["race"],
            klass=json_data["klass"],
            descritpion=json_data["descritpion"],
        )

    def __str__(self):
        return f" - HERO - {self.name} ({self.race}, {self.klass} {self.lvl}lvl)"
