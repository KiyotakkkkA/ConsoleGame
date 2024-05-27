import sys

from MainGame.FuncTools.formatedPrint import FormattedPrint


class MenuConstructor:
    def __init__(self, header, size):
        self.header = header
        self.size = size
        self.optionsMap = {}

        self.options = []

    def createContent(self, options):
        self.options = options

    def showMenu(self):
        print()
        print('+{:-^{}s}+'.format(f' {self.header} ', self.size * 2))
        print('|{:^{}s}|'.format('Выберите опцию', self.size * 2))
        print('+{:-^{}s}+'.format('', self.size * 2))

        for i in range(len(self.options)):
            print('|{:^{}s}|'.format(f'{i + 1}. {self.options[i].name}', self.size * 2))

        print('+{:-^{}s}+'.format('', self.size * 2))
        print('|{:^{}s}|'.format('', self.size * 2))
        print('+{:-^{}s}+'.format(f' {self.header} ', self.size * 2))


class TextMenues:

    def __init__(self, Player, QuestManager, Atlas):
        super().__init__()
        self.Player = Player
        self.QuestManager = QuestManager
        self.Atlas = Atlas

        self.exitButton = self.Button("Выйти", self.exitGame)
        self.newGameButton = self.Button("Новая игра", self.newGame)
        self.continueGameButton = self.Button("Продолжить", self.toGameMenu)
        self.playerButton = self.Button(f"Персонаж "
                                        f"{'(недоступно)' if not self.Player.getPlayerMenuStatus() else ''}",
                                        self.empty)
        self.storyButton = self.Button("Сюжет", self.storyMode)
        self.questBookButton = self.Button("Квесты", self.toQuestMenu)
        self.toMainMenuButton = self.Button("В главное меню", self.toMainMenu)
        self.endlessFightButton = self.Button(f"Расколотый мир "
                                              f"{'(недоступно)' if not self.Player.getEndlessFightStatus() else ''}",
                                              self.empty)
        self.toGameMenuButton = self.Button("В игровое меню", self.toGameMenu)
        self.bountyTasksButton = self.Button(f"Доска объявлений "
                                             f"{'(недоступно)' if not self.Player.getBountyTasksStatus() else ''}",
                                             self.empty)

        self.mainMenuOptions = [self.newGameButton, self.exitButton] \
            if self.Player.playerData['playermeta']['newGame'] else [self.continueGameButton, self.newGameButton,
                                                                     self.exitButton]

        self.gameMenuOptions = [self.storyButton, self.playerButton, self.questBookButton, self.endlessFightButton,
                                self.bountyTasksButton, self.toMainMenuButton]

        self.MainMenu = MenuConstructor('ГЛАВНОЕ МЕНЮ', 20)
        self.MainMenu.createContent(self.mainMenuOptions)

        self.GameMenu = MenuConstructor("ИГРОВОЕ МЕНЮ", 20)
        self.GameMenu.createContent(self.gameMenuOptions)

    class Button:
        def __init__(self, name, command):
            self.name = name
            self.command = command

        def run(self):
            self.command()

    def empty(self):
        print("[*] В разработке...")
        self.showMainMenu().run()

    def exitGame(self):
        FormattedPrint.printInfo('Выключение...')
        sys.exit()

    def storyMode(self):
        allMainQuests = [x for x in self.Player.playerData['playerquests'] if "MQ" in x
                         and self.Player.playerData['playerquests'][x] == 'complete']

        lastCompletedQuest = self.QuestManager.QuestAtlas[allMainQuests[-1]]
        nextQuest = self.QuestManager.QuestAtlas[lastCompletedQuest['nextQuestNameID']]
        self.QuestManager.processQuests(nextQuest['questNameID'], 2.5)

    def newGame(self):
        self.Player.newGame()
        self.Player.setNewGameStatus(0)
        self.QuestManager.processQuests('MQ1', 2.5)
        self.toGameMenu()

    def toMainMenu(self):
        self.showMainMenu().run()

    def toGameMenu(self):
        self.showGameMenu().run()

    def toQuestMenu(self):
        self.showQuestsMenu().run()

    def showMainMenu(self):
        self.MainMenu.showMenu()
        while True:
            answer = input()
            if answer.isdigit():
                return self.mainMenuOptions[int(answer) - 1]

    def showGameMenu(self):
        self.GameMenu.showMenu()
        while True:
            answer = input()
            if answer.isdigit():
                return self.gameMenuOptions[int(answer) - 1]

    def showQuestsMenu(self):
        questsArray = self.Player.playerData['playerquests']
        allQuests = self.QuestManager.QuestAtlas
        counter = 1
        print('\n+-[*] КНИГА ЗАДАНИЙ [*]-\n|')

        for quest in questsArray:
            print(f'| {counter}) '
                  f'"{allQuests[quest]['questName'].upper()}" {'(ОСНОВНОЙ СЮЖЕТ)' if "MQ" in quest else ''} : '
                  f"{questsArray[quest].replace('complete', 'завершено').replace('active', 'в процессе').upper()}")
            counter += 1
        print('|\n+-[*] КНИГА ЗАДАНИЙ [*]-\n|')
        print(f'| 0. {self.toGameMenuButton.name}\n')
        while True:
            answer = input()
            if answer.isdigit() and int(answer) == 0:
                return self.toGameMenuButton
