from MainGame.GameLoading.PreLoading import PreLoading
from MainGame.FuncTools.formatedPrint import FormattedPrint


class Game(PreLoading):
    def __init__(self):
        super().__init__()
        FormattedPrint.printInfo('"Endless Story" запущена!')

        self.run()

    def run(self):
        self.TextMenues.showMainMenu().run()
