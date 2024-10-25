import json
from pathlib import Path

from config import SAVE_FOLDER
from objects.guild import Guild


class GuildRepository:

    SAVE_FILE_POSTFIX = "_save.json"

    @classmethod
    def fetch_guild_by_guild_name(cls, guild_name):
        filename = guild_name + cls.SAVE_FILE_POSTFIX
        filepath = Path.joinpath(SAVE_FOLDER, filename)

        with open(filepath, "r") as f:
            save_data_json = json.load(f)

        return Guild.from_json(save_data_json)
