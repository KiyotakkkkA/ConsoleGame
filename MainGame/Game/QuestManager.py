import json
import os
import time


class Choose:
    def __init__(self, options, delay):
        self.options = options
        self.choose = None
        self.delay = delay

    def ask(self):
        print("\n[*] ВЫБЕРИТЕ 1 ВАРИАНТ ОТВЕТА [*]")
        for x in range(len(self.options['playerAnswers'])):
            print(f'{x + 1}. {self.options['playerAnswers'][x]}')
        print()

        while True:
            answer = input()
            if answer.isdigit():
                self.choose = int(answer) - 1
                while self.options['returnBack'][self.choose]:

                    print(self.options['playerAnswers'][self.choose])
                    time.sleep(self.delay)

                    for x in range(len(self.options['otherAnswers'][self.choose]['data'])):
                        print(self.options['otherAnswers'][self.choose]['data'][x])
                        time.sleep(self.delay)

                    print("\n[*] ВЫБЕРИТЕ 1 ВАРИАНТ ОТВЕТА [*]")
                    for x in range(len(self.options['playerAnswers'])):
                        print(f'{x + 1}. {self.options['playerAnswers'][x]}')
                    print()

                    while True:
                        answer = input()
                        if answer.isdigit():
                            self.choose = int(answer) - 1
                            break

                else:

                    print(self.options['playerAnswers'][self.choose])
                    break

        time.sleep(self.delay)

        for x in range(len(self.options['otherAnswers'][self.choose]['data'])):
            print(self.options['otherAnswers'][self.choose]['data'][x])
            time.sleep(self.delay)


class QuestManager:
    def __init__(self, Player):
        self.QuestAtlas = self.loadQuestsFromJson()
        self.Player = Player

    def printStoryBlock(self, currentQuest, storyBlock, delay):
        for x in range(len(currentQuest[storyBlock]['data'])):
            print(currentQuest[storyBlock]['data'][x].replace("{playername}", self.Player.getName()))
            time.sleep(delay)

    @staticmethod
    def loadQuestsFromJson():
        dictionary = {}
        files = os.scandir("MainGame/Game/QuestsMessages")
        for file in files:
            with open(f"MainGame/Game/QuestsMessages/{file.name}", encoding="UTF-8") as f:
                dictionary[file.name.split("_")[1].replace('.json', '')] = json.load(f)

        return dictionary

    def processQuests(self, questNameID, delay):
        currentQuest = self.QuestAtlas[questNameID]
        self.Player.setQuestStage(questNameID, 'active')

        for stage in currentQuest:
            if len(stage) == 2:
                if 'M' in stage:
                    self.printStoryBlock(currentQuest, stage, delay)
                if 'A' in stage:
                    choose = Choose(currentQuest[stage], delay)
                    choose.ask()
            elif 'event' in stage:
                if 'SetName' in stage:
                    print(currentQuest[stage]['data']['m1'])
                    name = input()
                    print()
                    self.Player.setName(name)

        print(f'\n[*] КВЕСТ "{currentQuest['questName']}" ЗАВЕРШЁН [*]')
        self.Player.setQuestStage(questNameID, 'complete')
