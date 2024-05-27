import json
import os


class Player:
    def __init__(self):
        self.playerData = Player.PlayerDataLoadFromJson()

    @staticmethod
    def PlayerDataLoadFromJson() -> dict:
        dictionary = {}
        files = os.scandir("MainGame/Player/PlayerData")
        for file in files:
            with open(f"MainGame/Player/PlayerData/{file.name}", encoding="UTF-8") as f:
                data = json.load(f)
                dictionary[file.name.split('.')[0].lower()] = data

        return dictionary

    def setQuestStage(self, questNameID, questStage):
        self.playerData['playerquests'][questNameID] = questStage
        self.dumpQuestsToJson()

    def getQuestStage(self, questNameID):
        if questNameID in self.playerData['playerquests']:
            return self.playerData['playerquests'][questNameID]
        else:
            return 0

    def setHelmet(self, nameID):
        self.playerData['playermeta']['helmetID'] = nameID
        self.dumpMetaToJson()

    def setChestplate(self, nameID):
        self.playerData['playermeta']['chestplateID'] = nameID
        self.dumpMetaToJson()

    def setGloves(self, nameID):
        self.playerData['playermeta']['glovesID'] = nameID
        self.dumpMetaToJson()

    def setGreaves(self, nameID):
        self.playerData['playermeta']['greavesID'] = nameID
        self.dumpMetaToJson()

    def setBoots(self, nameID):
        self.playerData['playermeta']['bootsID'] = nameID
        self.dumpMetaToJson()

    def setLeftRing(self, nameID):
        self.playerData['playermeta']['leftRingID'] = nameID
        self.dumpMetaToJson()

    def setRightRing(self, nameID):
        self.playerData['playermeta']['rightRingID'] = nameID
        self.dumpMetaToJson()

    def setAmulet(self, nameID):
        self.playerData['playermeta']['amuletID'] = nameID
        self.dumpMetaToJson()

    def setCloak(self, nameID):
        self.playerData['playermeta']['cloakID'] = nameID
        self.dumpMetaToJson()

    def setName(self, name):
        self.playerData['playermeta']['name'] = name
        self.dumpMetaToJson()

    def getName(self):
        return self.playerData['playermeta']['name']

    def setLevel(self, level):
        self.playerData['playermeta']['level'] = level
        self.dumpMetaToJson()

    def getLevel(self):
        return self.playerData['playermeta']['level']

    def setNewGameStatus(self, status):
        self.playerData['playermeta']['newGame'] = status
        self.dumpMetaToJson()

    def getNewGameStatus(self):
        return self.playerData['playermeta']['newGame']

    def setExp(self, exp):
        self.playerData['playermeta']['exp'] = exp
        self.dumpMetaToJson()

    def getExp(self):
        return self.playerData['playermeta']['exp']

    def setMoney(self, money):
        self.playerData['playermeta']['money'] = money
        self.dumpMetaToJson()

    def getMoney(self):
        return self.playerData['playermeta']['money']

    def setHP(self, hp):
        self.playerData['playermeta']['current_hp'] = hp
        self.dumpMetaToJson()

    def getHP(self):
        return self.playerData['playermeta']['current_hp']

    def setEnergy(self, energy):
        self.playerData['playermeta']['current_energy'] = energy
        self.dumpMetaToJson()

    def getEnergy(self):
        return self.playerData['playermeta']['current_energy']

    def setStamina(self, energy):
        self.playerData['playermeta']['current_stamina'] = energy
        self.dumpMetaToJson()

    def getStamina(self):
        return self.playerData['playermeta']['current_stamina']

    def setPlayerMenuStatus(self, status):
        self.playerData['playermeta']['isPlayerMenuUnlocked'] = status
        self.dumpMetaToJson()

    def getPlayerMenuStatus(self):
        return self.playerData['playermeta']['isPlayerMenuUnlocked']

    def setEndlessFightStatus(self, status):
        self.playerData['playermeta']['isEndlessFightUnlocked'] = status
        self.dumpMetaToJson()

    def getEndlessFightStatus(self):
        return self.playerData['playermeta']['isEndlessFightUnlocked']

    def setBountyTasksStatus(self, status):
        self.playerData['playermeta']['isBountyTasksUnlocked'] = status
        self.dumpMetaToJson()

    def getBountyTasksStatus(self):
        return self.playerData['playermeta']['isBountyTasksUnlocked']

    def newGame(self):
        self.setHelmet('armor:woodenHelmet')
        self.setChestplate('armor:woodenChestplate')
        self.setGloves('armor:batteredGloves')
        self.setGreaves('armor:woodenGreaves')
        self.setBoots('armor:woodenBoots')
        self.setCloak('armor:batteredCloak')
        self.setRightRing('armor:elderRightRing')
        self.setLeftRing('armor:elderLeftRing')
        self.setAmulet('armor:elderAmulet')

        self.setName('-')
        self.setLevel(1)
        self.setExp(0)
        self.setMoney(50)
        self.setNewGameStatus(1)
        self.setHP(100)
        self.setStamina(100)
        self.setEnergy(100)

    def dumpMetaToJson(self):
        with open("MainGame/Player/PlayerData/PlayerMeta.json", 'w') as f:
            json.dump(self.playerData['playermeta'], f, indent=1)

    def dumpStatsToJson(self):
        with open("MainGame/Player/PlayerData/PlayerStats.json", 'w') as f:
            json.dump(self.playerData['playerstats'], f, indent=1)

    def dumpQuestsToJson(self):
        with open("MainGame/Player/PlayerData/PlayerQuests.json", 'w') as f:
            json.dump(self.playerData['playerquests'], f, indent=1)



