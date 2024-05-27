import json
import os

from MainGame.Game.Menues import TextMenues
from MainGame.GameLoading.Element import Element
from MainGame.Game.QuestManager import QuestManager
from MainGame.Player.Player import Player


class PreLoading:
    def __init__(self):

        self.Atlas = self.ResourcesLoadFromJson()
        self.Player = Player()
        self.QuestManager = QuestManager(self.Player)
        self.TextMenues = TextMenues(self.Player, self.QuestManager, self.Atlas)

    @staticmethod
    def indexingAtlasElements(elements: dict) -> None:
        for keys in elements:
            elements[keys] = Element(elements[keys])

    @staticmethod
    def ResourcesLoadFromJson() -> dict:
        dictionary = {}
        directories = os.scandir("MainGame/Resources")
        for directory in directories:
            files = os.scandir(f"MainGame/Resources/{directory.name}")
            for file in files:
                with open(f"MainGame/Resources/{directory.name}/{file.name}", encoding="UTF-8") as f:
                    data = json.load(f)
                    PreLoading.indexingAtlasElements(data)
                    dictionary[file.name.split('.')[0].lower()] = data

        return dictionary

    def getElementByNameID(self, nameID: str) -> Element:
        category, item = nameID.split(':')
        return self.Atlas[category][item]

