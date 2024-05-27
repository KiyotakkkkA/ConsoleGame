from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QFormLayout, QGroupBox, \
    QScrollArea, QComboBox, QTextEdit, QTabWidget, QFrame, QCheckBox, QDialog, QHBoxLayout

from PyQt6.QtGui import QFont
import json

from ContentManagerUI.QuestTab import (DetailsRequirementDialog, DetailsActionDialog, DetailsRewardsDialog,
                                       DetailsQuestBlockDialog, CustomComboBox)

from MainGame.GameLoading.PreLoading import PreLoading


class QuestManager(QWidget):
    def __init__(self):
        super().__init__()

        self.Atlas = PreLoading.ResourcesLoadFromJson()

        self.style_file = open("ContentManagerUI/styles.css", "r")
        self.style = self.style_file.read()
        self.setStyleSheet(self.style)
        self.style_file.close()

        self.font = QFont('Times', 14)
        self.font.setBold(True)

        self.currentBlocksArray = []

        self.tab_quests = QWidget()
        self.tab_items = QWidget()
        self.form_layout = QFormLayout()

        self.setWindowTitle('Менеджер контента')

        self.tab_widget = QTabWidget()

        self.createTabQuests()
        self.tab_widget.addTab(self.tab_items, 'Предметы')

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tab_widget)
        self.setLayout(self.layout)

    def createTabQuests(self):
        def addRequirementBlock():
            _name_ = "Пусто"

            groupbox = QGroupBox(f"Требование - {_name_}")
            groupbox.setFont(self.font)
            groupbox_layout = QFormLayout(groupbox)

            details_dialog = DetailsRequirementDialog(_name_, groupbox, self.Atlas)
            self.currentBlocksArray.append(details_dialog)

            def showDetailsWindow():
                details_dialog.exec()

            def hideDetailsWindow():
                self.currentBlocksArray.remove(details_dialog)
                groupbox.setVisible(False)

            detail_button = QPushButton('Показать детали')
            detail_button.setStyleSheet("QPushButton { font-size: 16px; font-family: "
                                        "'Arial'; font-weight: bold;}")
            detail_button.clicked.connect(showDetailsWindow)

            hide_detail_button = QPushButton('Удалить блок')
            hide_detail_button.setStyleSheet("QPushButton { background-color: #dc3545; font-size: 16px; font-family: "
                                             "'Arial'; font-weight: bold;}"
                                             "QPushButton:hover {background-color: #992027}")
            hide_detail_button.clicked.connect(hideDetailsWindow)

            self.form_layout.insertRow(-1, groupbox)
            groupbox_layout.addWidget(detail_button)
            groupbox_layout.addWidget(hide_detail_button)

        def addQuestBlock():
            _name_ = "Пусто"

            groupbox = QGroupBox(f"Квестовый блок - {_name_}")
            groupbox.setFont(self.font)
            groupbox_layout = QFormLayout(groupbox)

            details_dialog = DetailsQuestBlockDialog(_name_, groupbox)
            self.currentBlocksArray.append(details_dialog)

            def showDetailsWindow():
                details_dialog.exec()

            def hideDetailsWindow():
                self.currentBlocksArray.remove(details_dialog)
                groupbox.setVisible(False)

            detail_button = QPushButton('Показать детали')
            detail_button.setStyleSheet("QPushButton { font-size: 16px; font-family: "
                                        "'Arial'; font-weight: bold;}")
            detail_button.clicked.connect(showDetailsWindow)

            hide_detail_button = QPushButton('Удалить блок')
            hide_detail_button.setStyleSheet("QPushButton { background-color: #dc3545; font-size: 16px; font-family: "
                                             "'Arial'; font-weight: bold;}"
                                             "QPushButton:hover {background-color: #992027}")
            hide_detail_button.clicked.connect(hideDetailsWindow)

            self.form_layout.insertRow(-1, groupbox)
            groupbox_layout.addWidget(detail_button)
            groupbox_layout.addWidget(hide_detail_button)

        def addClaimBlock():
            _name_ = "Пусто"

            groupbox = QGroupBox(f"Награда - {_name_}")
            groupbox.setFont(self.font)
            groupbox_layout = QFormLayout(groupbox)

            details_dialog = DetailsRewardsDialog(_name_, groupbox)
            self.currentBlocksArray.append(details_dialog)

            def showDetailsWindow():
                details_dialog.exec()

            def hideDetailsWindow():
                self.currentBlocksArray.remove(details_dialog)
                groupbox.setVisible(False)

            detail_button = QPushButton('Показать детали')
            detail_button.setStyleSheet("QPushButton { font-size: 16px; font-family: "
                                        "'Arial'; font-weight: bold;}")
            detail_button.clicked.connect(showDetailsWindow)

            hide_detail_button = QPushButton('Удалить блок')
            hide_detail_button.setStyleSheet("QPushButton { background-color: #dc3545; font-size: 16px; font-family: "
                                             "'Arial'; font-weight: bold;}"
                                             "QPushButton:hover {background-color: #992027}")
            hide_detail_button.clicked.connect(hideDetailsWindow)

            self.form_layout.insertRow(-1, groupbox)
            groupbox_layout.addWidget(detail_button)
            groupbox_layout.addWidget(hide_detail_button)

        def addActionBlock():
            _name_ = "Пусто"

            groupbox = QGroupBox(f"Действие - {_name_}")
            groupbox.setFont(self.font)
            groupbox_layout = QFormLayout(groupbox)

            details_dialog = DetailsActionDialog(_name_, groupbox)
            self.currentBlocksArray.append(details_dialog)

            def showDetailsWindow():
                details_dialog.exec()

            def hideDetailsWindow():
                self.currentBlocksArray.remove(details_dialog)
                groupbox.setVisible(False)

            detail_button = QPushButton('Показать детали')
            detail_button.setStyleSheet("QPushButton { font-size: 16px; font-family: "
                                        "'Arial'; font-weight: bold;}")
            detail_button.clicked.connect(showDetailsWindow)

            hide_detail_button = QPushButton('Удалить блок')
            hide_detail_button.setStyleSheet("QPushButton { background-color: #dc3545; font-size: 16px; font-family: "
                                             "'Arial'; font-weight: bold;}"
                                             "QPushButton:hover {background-color: #992027}")
            hide_detail_button.clicked.connect(hideDetailsWindow)

            self.form_layout.insertRow(-1, groupbox)
            groupbox_layout.addWidget(detail_button)
            groupbox_layout.addWidget(hide_detail_button)

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

        separator3 = QFrame()
        separator3.setFrameShape(QFrame.Shape.HLine)
        separator3.setFrameShadow(QFrame.Shadow.Sunken)

        layout = QVBoxLayout()
        inner_widget.setLayout(layout)

        button_add_requirement = QPushButton('Добавить требование')
        button_add_requirement.setFont(self.font)

        button_add_questblock = QPushButton('Добавить квестовый блок')
        button_add_questblock.setFont(self.font)

        button_add_claim = QPushButton('Добавить награду')
        button_add_claim.setFont(self.font)

        button_add_action = QPushButton('Добавить действие')
        button_add_action.setFont(self.font)

        button_add_quest = QPushButton('Добавить квест')
        button_add_quest.setFont(self.font)

        self.form_layout.addRow(label_quest_id, edit_quest_id)
        self.form_layout.addRow(label_quest_name, edit_quest_name)

        main_layout = QVBoxLayout(self.tab_quests)

        self.form_layout.addRow(button_add_requirement)

        self.form_layout.addWidget(separator1)

        self.form_layout.addRow(button_add_questblock)
        layout.addLayout(self.form_layout)
        main_layout.addWidget(scroll_area)

        self.form_layout.addWidget(separator2)

        self.form_layout.addRow(button_add_action)

        self.form_layout.addWidget(separator3)

        self.form_layout.addRow(button_add_claim)

        main_layout.addWidget(button_add_quest)

        button_add_requirement.clicked.connect(addRequirementBlock)
        button_add_questblock.clicked.connect(addQuestBlock)
        button_add_claim.clicked.connect(addClaimBlock)
        button_add_action.clicked.connect(addActionBlock)

        self.tab_widget.addTab(self.tab_quests, 'Квесты')


if __name__ == '__main__':
    app = QApplication([])
    manager = QuestManager()
    manager.showMaximized()
    app.exec()
