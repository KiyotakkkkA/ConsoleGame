from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QFormLayout, QGroupBox, \
    QScrollArea, QComboBox, QTextEdit, QTabWidget, QFrame, QCheckBox, QDialog

from PyQt6.QtGui import QFont
import json


class CustomComboBox(QComboBox):
    def wheelEvent(self, event):
        event.ignore()


class AddGroupBoxDialog(QDialog):
    def __init__(self, parent=None):
        super(AddGroupBoxDialog, self).__init__(parent)

        self.setWindowTitle("Добавить группу")

        self.maxAnswersCount = [str(x) for x in range(1, 4)]

        self.groupbox = QGroupBox(f'Квестовый блок')
        self.groupbox.setFont(self.font)
        self.groupbox_layout = QFormLayout(self.groupbox)

        self.chooseTypeLabel = QLabel("Тип блока: ")
        self.chooseTypeLabel.setFont(self.font)

        self.chooseTypeCombo = CustomComboBox()
        self.chooseTypeCombo.addItems(self.questOptions)
        self.chooseTypeCombo.setCurrentIndex(-1)
        self.chooseTypeCombo.setFont(self.font)

        self.groupbox_layout.addRow(self.chooseTypeLabel, self.chooseTypeCombo)

        self.textMainStatusEntry = QTextEdit()
        self.textMainStatusEntry.setFont(self.font)
        self.textMainStatusEntry.setStyleSheet("border: 2px solid gray;")
        self.textMainStatusLabel = QLabel("Текст")
        self.textMainStatusLabel.setFont(self.font)
        self.textMainStatusEntry.setVisible(False)
        self.textMainStatusLabel.setVisible(False)

        self.textChooseStatusCombo = CustomComboBox()
        self.textChooseStatusCombo.addItems(self.maxAnswersCount)
        self.textChooseStatusCombo.setCurrentIndex(-1)
        self.textChooseStatusCombo.setFont(self.font)
        self.textChooseStatusLabel = QLabel("Количество вариантов ответа")
        self.textChooseStatusLabel.setFont(self.font)
        self.textChooseStatusCombo.setVisible(False)
        self.textChooseStatusLabel.setVisible(False)

        self.tempLabels = []
        self.tempEdits = []
        self.tempAnswerLabels = []
        self.tempAnswerEdits = []
        self.tempReturnChecks = []

        self.groupbox_layout.addRow(self.textMainStatusLabel)
        self.groupbox_layout.addRow(self.textMainStatusEntry)

        self.groupbox_layout.addRow(self.textChooseStatusLabel, self.textChooseStatusCombo)

        self.chooseTypeCombo.currentTextChanged.connect(self.changeVisibilityWidgets)
        self.textChooseStatusCombo.currentTextChanged.connect(self.createAnswerForm)

        self.groupbox.setMinimumHeight(self.groupbox.sizeHint().height() * 10)

    def changeVisibilityWidgets(self, text):
        if text == "Текст":
            self.textMainStatusEntry.setVisible(True)
            self.textMainStatusLabel.setVisible(True)
        else:
            self.textMainStatusEntry.setVisible(False)
            self.textMainStatusLabel.setVisible(False)

        if text == 'Выбор':
            self.textChooseStatusLabel.setVisible(True)
            self.textChooseStatusCombo.setVisible(True)
        else:
            if self.tempLabels or self.tempEdits or self.tempAnswerEdits or self.tempAnswerLabels:
                for x in range(len(self.tempLabels)):
                    self.tempLabels[x].setVisible(False)
                    self.tempEdits[x].setVisible(False)
                    self.tempAnswerEdits[x].setVisible(False)
                    self.tempAnswerLabels[x].setVisible(False)
                    self.tempReturnChecks[x].setVisible(False)

            self.textChooseStatusLabel.setVisible(False)
            self.textChooseStatusCombo.setVisible(False)

    def createAnswerForm(self, count):
        if self.tempLabels or self.tempEdits or self.tempAnswerEdits or self.tempAnswerLabels:
            for x in range(len(self.tempLabels)):
                self.tempLabels[x].setVisible(False)
                self.tempEdits[x].setVisible(False)
                self.tempAnswerEdits[x].setVisible(False)
                self.tempAnswerLabels[x].setVisible(False)
                self.tempReturnChecks[x].setVisible(False)

        for i in range(int(count)):
            self.tempLabels.append(QLabel(f"|-  Вариант ответа {i + 1}  -|"))
            self.tempEdits.append(QLineEdit())
            self.tempAnswerLabels.append(QLabel(f"|-  Серия ответов {i + 1}  -|"))
            temp = QTextEdit()
            temp.setStyleSheet("border: 2px solid gray;")
            temp.setFont(self.font)
            temp.setMinimumHeight(temp.sizeHint().height() // 2)
            self.tempAnswerEdits.append(temp)
            self.tempReturnChecks.append(QCheckBox('Возвращение к вопросу'))

        for x in range(len(self.tempLabels)):
            self.groupbox_layout.addRow(self.tempLabels[x])
            self.groupbox_layout.addRow(self.tempEdits[x])
            self.groupbox_layout.addRow(self.tempReturnChecks[x])
            self.groupbox_layout.addRow(self.tempAnswerLabels[x])
            self.groupbox_layout.addRow(self.tempAnswerEdits[x])


class QuestManager(QWidget):
    def __init__(self):
        super().__init__()

        self.style_file = open("ContentManagerUI/styles.css", "r")
        self.style = self.style_file.read()

        self.setStyleSheet(self.style)
        self.style_file.close()

        self.questOptions = ['Текст', 'Выбор', 'Команда', 'Бой']

        self.font = QFont('Times', 14)
        self.font.setBold(True)

        self.tab_quests = QWidget()
        self.tab_items = QWidget()
        self.form_layout = QFormLayout()

        self.setWindowTitle('Менеджер контента')

        self.tab_widget = QTabWidget()

        self.createTabQuests()
        self.createTabItems()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tab_widget)
        self.setLayout(self.layout)

    def createTabQuests(self):

        label_quest_id = QLabel('ID квеста:')
        label_quest_id.setFont(self.font)
        edit_quest_id = QLineEdit()
        edit_quest_id.setFont(self.font)
        edit_quest_id.setObjectName('questNameID')

        label_quest_name = QLabel('Название квеста:')
        label_quest_name.setFont(self.font)
        edit_quest_name = QLineEdit()
        edit_quest_name.setFont(self.font)
        edit_quest_name.setObjectName('questName')

        label_exp_reward = QLabel('Опыт за квест:')
        label_exp_reward.setFont(self.font)
        edit_exp_reward = QLineEdit()
        edit_exp_reward.setFont(self.font)
        edit_exp_reward.setObjectName('expReward')

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        inner_widget = QWidget()
        scroll_area.setWidget(inner_widget)

        separator1 = QFrame()
        separator1.setFrameShape(QFrame.Shape.HLine)
        separator1.setFrameShadow(QFrame.Shadow.Sunken)

        separator2 = QFrame()
        separator2.setFrameShape(QFrame.Shape.HLine)
        separator2.setFrameShadow(QFrame.Shadow.Sunken)

        layout = QVBoxLayout()
        inner_widget.setLayout(layout)

        button_add_requirement = QPushButton('Добавить требование')
        button_add_requirement.setFont(self.font)

        button_add_groupbox = QPushButton('Добавить квестовый блок')
        button_add_groupbox.setFont(self.font)
        button_add_groupbox.clicked.connect(self.add_groupbox)

        button_add_claim = QPushButton('Добавить награду')
        button_add_claim.setFont(self.font)

        button_add_quest = QPushButton('Добавить квест')
        button_add_quest.clicked.connect(self.add_quest)
        button_add_quest.setFont(self.font)

        self.form_layout.addRow(label_quest_id, edit_quest_id)
        self.form_layout.addRow(label_quest_name, edit_quest_name)

        main_layout = QVBoxLayout(self.tab_quests)

        self.form_layout.addRow(button_add_requirement)
        self.form_layout.addWidget(separator1)
        self.form_layout.addRow(button_add_groupbox)
        layout.addLayout(self.form_layout)
        main_layout.addWidget(scroll_area)
        self.form_layout.addWidget(separator2)
        self.form_layout.addRow(button_add_claim)

        main_layout.addWidget(button_add_quest)

        self.tab_widget.addTab(self.tab_quests, 'Квесты')

    def createTabItems(self):
        self.tab_widget.addTab(self.tab_items, 'Предметы')

    def add_groupbox(self):
        maxAnswersCount = [str(x) for x in range(1, 4)]

        groupbox = QGroupBox(f'Квестовый блок {len(self.form_layout) - 7}')
        groupbox.setFont(self.font)
        groupbox_layout = QFormLayout(groupbox)

        chooseTypeLabel = QLabel("Тип блока: ")
        chooseTypeLabel.setFont(self.font)

        chooseTypeCombo = self.CustomComboBox()
        chooseTypeCombo.addItems(self.questOptions)
        chooseTypeCombo.setCurrentIndex(-1)
        chooseTypeCombo.setFont(self.font)

        groupbox_layout.addRow(chooseTypeLabel, chooseTypeCombo)

        textMainStatusEntry = QTextEdit()
        textMainStatusEntry.setFont(self.font)
        textMainStatusEntry.setStyleSheet("border: 2px solid gray;")
        textMainStatusLabel = QLabel("Текст")
        textMainStatusLabel.setFont(self.font)
        textMainStatusEntry.setVisible(False)
        textMainStatusLabel.setVisible(False)

        textChooseStatusCombo = self.CustomComboBox()
        textChooseStatusCombo.addItems(maxAnswersCount)
        textChooseStatusCombo.setCurrentIndex(-1)
        textChooseStatusCombo.setFont(self.font)
        textChooseStatusLabel = QLabel("Количество вариантов ответа")
        textChooseStatusLabel.setFont(self.font)
        textChooseStatusCombo.setVisible(False)
        textChooseStatusLabel.setVisible(False)

        tempLabels = []
        tempEdits = []
        tempAnswerLabels = []
        tempAnswerEdits = []
        tempReturnChecks = []

        groupbox_layout.addRow(textMainStatusLabel)
        groupbox_layout.addRow(textMainStatusEntry)

        groupbox_layout.addRow(textChooseStatusLabel, textChooseStatusCombo)

        def changeVisibilityWidgets(text):
            if text == "Текст":
                textMainStatusEntry.setVisible(True)
                textMainStatusLabel.setVisible(True)
            else:
                textMainStatusEntry.setVisible(False)
                textMainStatusLabel.setVisible(False)

            if text == 'Выбор':
                textChooseStatusLabel.setVisible(True)
                textChooseStatusCombo.setVisible(True)
            else:
                if tempLabels or tempEdits or tempAnswerEdits or tempAnswerLabels:
                    for x in range(len(tempLabels)):
                        tempLabels[x].setVisible(False)
                        tempEdits[x].setVisible(False)
                        tempAnswerEdits[x].setVisible(False)
                        tempAnswerLabels[x].setVisible(False)
                        tempReturnChecks[x].setVisible(False)

                textChooseStatusLabel.setVisible(False)
                textChooseStatusCombo.setVisible(False)

        def createAnswerForm(count):
            if tempLabels or tempEdits or tempAnswerEdits or tempAnswerLabels:
                for x in range(len(tempLabels)):
                    tempLabels[x].setVisible(False)
                    tempEdits[x].setVisible(False)
                    tempAnswerEdits[x].setVisible(False)
                    tempAnswerLabels[x].setVisible(False)
                    tempReturnChecks[x].setVisible(False)

            for i in range(int(count)):
                tempLabels.append(QLabel(f"|-  Вариант ответа {i + 1}  -|"))
                tempEdits.append(QLineEdit())
                tempAnswerLabels.append(QLabel(f"|-  Серия ответов {i + 1}  -|"))
                temp = QTextEdit()
                temp.setStyleSheet("border: 2px solid gray;")
                temp.setFont(self.font)
                temp.setMinimumHeight(temp.sizeHint().height() // 2)
                tempAnswerEdits.append(temp)
                tempReturnChecks.append(QCheckBox('Возвращение к вопросу'))

            for x in range(len(tempLabels)):
                groupbox_layout.addRow(tempLabels[x])
                groupbox_layout.addRow(tempEdits[x])
                groupbox_layout.addRow(tempReturnChecks[x])
                groupbox_layout.addRow(tempAnswerLabels[x])
                groupbox_layout.addRow(tempAnswerEdits[x])

        chooseTypeCombo.currentTextChanged.connect(changeVisibilityWidgets)
        textChooseStatusCombo.currentTextChanged.connect(createAnswerForm)

        self.form_layout.insertRow(-1, groupbox)
        groupbox.setMinimumHeight(groupbox.sizeHint().height() * 10)

    def add_quest(self):
        quest_data = {
            "expReward": int(self.findChild(QLineEdit, 'expReward').text()),
            "questNameID": self.findChild(QLineEdit, 'questNameID').text().split('_')[1],
            "questName": self.findChild(QLineEdit, 'questName').text()
        }

        types = {
            'Текст': 'M',
            'Выбор': 'A',
            'Команда': 'C'
        }

        counter = 1
        currentType = 'M'

        for group_box in self.tab_quests.findChildren(QGroupBox):
            tempPlayerAnswers = []
            tempOtherAnswers = []
            returnBack = []
            for child in group_box.children():
                if isinstance(child, QComboBox) and child.currentText() in types:
                    currentType = types[child.currentText()]
                elif isinstance(child, QTextEdit) and child.isVisible() and currentType == 'M':
                    field_value = child.toPlainText().split('\n')
                    quest_data.setdefault(f'{currentType}{counter}', {})['data'] = list(field_value)
                    counter += 1
                elif isinstance(child, QLineEdit) and child.isVisible() and currentType == 'A':
                    tempPlayerAnswers.append(child.text())
                    counter += 1
                elif isinstance(child, QTextEdit) and child.isVisible() and currentType == 'A':
                    field_value = child.toPlainText().split('\n')
                    tempOtherAnswers.append({'data': list(field_value)})
                    counter += 1
                elif isinstance(child, QCheckBox) and child.isVisible() and currentType == 'A':
                    returnBack.append(child.isChecked())

            if tempPlayerAnswers and tempOtherAnswers:
                quest_data[f"A{counter}"] = {"playerAnswers": tempPlayerAnswers,
                                             "otherAnswers": tempOtherAnswers,
                                             "returnBack": returnBack}

        with open(f"ContentManagerUI/Output/{self.findChild(QLineEdit, 'questNameID').text()}.json", 'w',
                  encoding="UTF-8") as f:
            json.dump(quest_data, f, indent=1, ensure_ascii=False)


if __name__ == '__main__':
    app = QApplication([])
    manager = QuestManager()
    manager.showMaximized()
    app.exec()
