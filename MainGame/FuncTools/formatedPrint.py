class FormattedPrint:
    def __init__(self):
        pass

    @staticmethod
    def printInfo(text):
        print('[*]', text)

    @staticmethod
    def printWarning(text):
        print('[!]', text)

    @staticmethod
    def printAdding(text):
        print('[+]', text)

    @staticmethod
    def printQuestion(text):
        print('[?]', text)
