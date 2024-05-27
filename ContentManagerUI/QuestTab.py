from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QFormLayout, QGroupBox, \
    QScrollArea, QComboBox, QTextEdit, QTabWidget, QFrame, QCheckBox, QDialog, QHBoxLayout

from PyQt6.QtGui import QFont


class CustomComboBox(QComboBox):
    def wheelEvent(self, event):
        event.ignore()


class DetailsRequirementDialog(QDialog):
    def __init__(self, block_name, parent, Atlas):
        super().__init__(parent)

        self.Atlas = Atlas

        self.NAME = "Требование"
        self.data = {}

        self.font = QFont('Times', 14)
        self.font.setBold(True)

        self.block_name = block_name
        self.parent = parent

        self.setWindowTitle(f"{self.NAME} - " + self.block_name + ' [Детали]')

        self.form_layout = QFormLayout()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.layout.addLayout(self.form_layout)

        block_name_label = QLabel("Имя блока")
        block_name_label.setFont(self.font)

        self.block_name_edit = QLineEdit(block_name)
        self.block_name_edit.setFont(self.font)
        self.block_name_edit.setObjectName('NameSelector')

        self.form_layout.addRow(block_name_label, self.block_name_edit)

        save_button = QPushButton('Сохранить')
        save_button.clicked.connect(self.saveBlockName)
        save_button.setFont(self.font)

        self.options = ['Уровень', 'Предмет', 'Навык']

        type_label = QLabel("Тип требования")
        type_label.setFont(self.font)

        self.second_choose_label = None
        self.second_choose_entry = None

        self.third_choose_label = None
        self.third_choose_entry = None

        type_combobox = CustomComboBox()
        type_combobox.setObjectName('TypeSelector')
        type_combobox.addItems(self.options)
        type_combobox.setFont(self.font)
        type_combobox.setCurrentIndex(-1)

        self.form_layout.addRow(type_label, type_combobox)

        def changeItemState(text):
            changeCategory = {
                'Броня': "armor",
                'Оружие': "weapons",
                'Материал': "materials",
                "Зелье": "potions",
                "Артефакт": "artefacts"
            }

            code = changeCategory[text]
            temp = []

            if code in self.Atlas:
                for x in self.Atlas[code]:
                    temp.append(self.Atlas[code][x].container['name'])

            if any([self.third_choose_label, self.third_choose_label]):
                self.third_choose_label.setVisible(False)
                self.third_choose_entry.setVisible(False)

            self.third_choose_label = QLabel(text)
            self.third_choose_label.setFont(self.font)

            self.third_choose_entry = QComboBox()
            self.third_choose_entry.setFont(self.font)
            self.third_choose_entry.addItems(temp)
            self.third_choose_entry.setCurrentIndex(-1)

            self.third_choose_label.setVisible(True)
            self.third_choose_entry.setVisible(True)

            self.form_layout.addRow(self.third_choose_label, self.third_choose_entry)

        def changeState(text):
            itemTypes = ['Материал', 'Оружие', 'Броня', 'Зелье', 'Артефакт']

            if any([self.second_choose_entry, self.second_choose_label]):
                self.second_choose_label.setVisible(False)
                self.second_choose_entry.setVisible(False)

            if text == "Уровень":
                self.second_choose_label = QLabel("Требуемый уровень")
                self.second_choose_label.setFont(self.font)
                self.second_choose_entry = QLineEdit()
                self.second_choose_entry.setFont(self.font)

            if text == "Навык":
                self.second_choose_label = QLabel("Требуемый навык")
                self.second_choose_label.setFont(self.font)
                self.second_choose_entry = CustomComboBox()
                self.second_choose_entry.setFont(self.font)
                self.second_choose_entry.setCurrentIndex(-1)

            if text == "Предмет":
                self.second_choose_label = QLabel("Требуемый тип предмета")
                self.second_choose_label.setFont(self.font)
                self.second_choose_entry = CustomComboBox()
                self.second_choose_entry.setFont(self.font)
                self.second_choose_entry.addItems(itemTypes)
                self.second_choose_entry.setCurrentIndex(-1)

            self.second_choose_label.setVisible(True)
            self.second_choose_entry.setVisible(True)
            self.second_choose_entry.setObjectName("")
            if isinstance(self.second_choose_entry, QComboBox):
                self.second_choose_entry.currentTextChanged.connect(changeItemState)

            self.form_layout.addRow(self.second_choose_label, self.second_choose_entry)

        type_combobox.currentTextChanged.connect(changeState)

        self.layout.addWidget(save_button)

    def saveBlockName(self):
        new_block_name = self.block_name_edit.text()
        self.parent.setTitle(f"{self.NAME} - " + new_block_name)
        self.setWindowTitle(f"{self.NAME} - " + new_block_name + ' [Детали]')

        for i in range(self.form_layout.rowCount()):
            item = self.form_layout.itemAt(i)
            if item and item.widget() and item.widget().isVisible():
                if isinstance(item.widget(), QLineEdit):
                    self.data[item.widget().objectName()] = item.widget().text()
                elif isinstance(item.widget(), QComboBox):
                    self.data[item.widget().objectName()] = item.widget().currentText()

        print(self.data)


class DetailsQuestBlockDialog(QDialog):
    def __init__(self, block_name, parent=None):
        super().__init__(parent)

        self.NAME = "Квестовый блок"
        self.data = {}

        self.font = QFont('Times', 14)
        self.font.setBold(True)

        self.block_name = block_name
        self.parent = parent

        self.setWindowTitle(f"{self.NAME} - " + self.block_name + ' [Детали]')

        self.form_layout = QFormLayout()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.layout.addLayout(self.form_layout)

        block_name_label = QLabel("Имя блока")
        block_name_label.setFont(self.font)

        self.block_name_edit = QLineEdit(block_name)
        self.block_name_edit.setFont(self.font)

        self.form_layout.addRow(block_name_label, self.block_name_edit)

        save_button = QPushButton('Сохранить')
        save_button.clicked.connect(self.saveBlockName)
        save_button.setFont(self.font)

        self.options = ['Текст', 'Выбор']

        type_label = QLabel("Тип квестового блока")
        type_label.setFont(self.font)

        def changeState(text):
            pass

        type_combobox = CustomComboBox()
        type_combobox.addItems(self.options)
        type_combobox.setFont(self.font)
        type_combobox.setCurrentIndex(-1)
        type_combobox.currentTextChanged.connect(changeState)

        self.form_layout.addRow(type_label, type_combobox)
        self.layout.addWidget(save_button)

    def saveBlockName(self):
        new_block_name = self.block_name_edit.text()
        self.parent.setTitle(f"{self.NAME} - " + new_block_name)
        self.setWindowTitle(f"{self.NAME} - " + new_block_name + ' [Детали]')


class DetailsActionDialog(QDialog):
    def __init__(self, block_name, parent=None):
        super().__init__(parent)

        self.NAME = "Действие"
        self.data = {}

        self.font = QFont('Times', 14)
        self.font.setBold(True)

        self.block_name = block_name
        self.parent = parent

        self.setWindowTitle(f"{self.NAME} - " + self.block_name + ' [Детали]')

        self.form_layout = QFormLayout()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.layout.addLayout(self.form_layout)

        block_name_label = QLabel("Имя блока")
        block_name_label.setFont(self.font)

        self.block_name_edit = QLineEdit(block_name)
        self.block_name_edit.setFont(self.font)

        self.form_layout.addRow(block_name_label, self.block_name_edit)

        save_button = QPushButton('Сохранить')
        save_button.clicked.connect(self.saveBlockName)
        save_button.setFont(self.font)

        self.options = ['Выдача', 'Взятие', 'Прочее']

        type_label = QLabel("Тип действия")
        type_label.setFont(self.font)

        def changeState(text):
            pass

        type_combobox = CustomComboBox()
        type_combobox.addItems(self.options)
        type_combobox.setFont(self.font)
        type_combobox.setCurrentIndex(-1)
        type_combobox.currentTextChanged.connect(changeState)

        self.form_layout.addRow(type_label, type_combobox)
        self.layout.addWidget(save_button)

    def saveBlockName(self):
        new_block_name = self.block_name_edit.text()
        self.parent.setTitle(f"{self.NAME} - " + new_block_name)
        self.setWindowTitle(f"{self.NAME} - " + new_block_name + ' [Детали]')


class DetailsRewardsDialog(QDialog):
    def __init__(self, block_name, parent=None):
        super().__init__(parent)

        self.NAME = "Награда"
        self.data = {}

        self.font = QFont('Times', 14)
        self.font.setBold(True)

        self.block_name = block_name
        self.parent = parent

        self.setWindowTitle(f"{self.NAME} - " + self.block_name + ' [Детали]')

        self.form_layout = QFormLayout()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.layout.addLayout(self.form_layout)

        block_name_label = QLabel("Имя блока")
        block_name_label.setFont(self.font)

        self.block_name_edit = QLineEdit(block_name)
        self.block_name_edit.setFont(self.font)

        self.form_layout.addRow(block_name_label, self.block_name_edit)

        save_button = QPushButton('Сохранить')
        save_button.clicked.connect(self.saveBlockName)
        save_button.setFont(self.font)

        self.options = ['Предмет', 'Деньги', 'Навык', 'Опыт']

        type_label = QLabel("Тип награды")
        type_label.setFont(self.font)

        def changeState(text):
            pass

        type_combobox = CustomComboBox()
        type_combobox.addItems(self.options)
        type_combobox.setFont(self.font)
        type_combobox.setCurrentIndex(-1)
        type_combobox.currentTextChanged.connect(changeState)

        self.form_layout.addRow(type_label, type_combobox)
        self.layout.addWidget(save_button)

    def saveBlockName(self):
        new_block_name = self.block_name_edit.text()
        self.parent.setTitle(f"{self.NAME} - " + new_block_name)
        self.setWindowTitle(f"{self.NAME} - " + new_block_name + ' [Детали]')
