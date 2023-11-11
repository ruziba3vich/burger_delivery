from PyQt5.QtWidgets import (QPushButton, QLabel, QMainWindow,
                            QWidget, QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from abc_c_user_verification import UserVerification

class FirstWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__user_verification_window = UserVerification(self)
        self.setWindowTitle("WELCOME")
        #"C:\Users\Gulzhaev\Downloads\Telegram Desktop\image_2023-11-11_22-11-23.png"
        self.setStyleSheet("QWidget#MyWindow { background-image: url('C:/Users/Gulzhaev/Downloads/Telegram Desktop/image_2023-11-11_22-11-23.png'); background-repeat: no-repeat; background-position: center; }")

        self.setObjectName("MyWindow")


        self.__welcoming_label = QLabel("<html><b><font size='10'>WELCOME</font></b></html>")
        self.__welcoming_label.setStyleSheet("color: rgb(255, 193, 0);")
        font = QFont()
        font.setBold(True)
        font.setPointSize(16)
        self.__user_button = QPushButton("USER")
        self.__user_button.setCursor(Qt.PointingHandCursor)
        self.__user_button.clicked.connect(self.__user_button_clicked)
        self.__user_button.setMinimumHeight(80)
        self.__user_button.setFont(font)
        self.__user_button.setStyleSheet("""color: black;
                                            background-color: rgb(255, 193, 0);""")
        self.__user_button.enterEvent = lambda event: self.__button_hovered(event, self.__user_button)
        self.__user_button.leaveEvent = lambda event: self.__button_unhovered(event, self.__user_button)
        self.__admin_button = QPushButton("ADMIN")
        self.__admin_button.setMinimumHeight(80)
        self.__admin_button.setFont(font)
        self.__admin_button.setCursor(Qt.PointingHandCursor)
        self.__admin_button.setStyleSheet("""color: black;
                                            background-color: rgb(255, 193, 0);""")
        self.__admin_button.enterEvent = lambda event: self.__button_hovered(event, self.__admin_button)
        self.__admin_button.leaveEvent = lambda event: self.__button_unhovered(event, self.__admin_button)

        self.__main_layout = self.__layout_maker(
                                    True,
                                    self.__welcoming_label,
                                    self.__user_button,
                                    self.__admin_button
                                )
        self.__main_layout.setAlignment(self.__welcoming_label, Qt.AlignLeft)

        self.__main_widget = QWidget()
        self.__main_widget.setLayout(self.__main_layout)

        self.setCentralWidget(self.__main_widget)

    def __layout_maker(self, is_vertical, * widgets):
        if is_vertical:
            layout = QVBoxLayout()
        else:
            layout = QHBoxLayout()
        for widget in widgets:
            layout.addWidget(widget)
        return layout
    
    def __button_hovered(self, event, button):
        self.__current_stylesheet = button.styleSheet()
        button.setStyleSheet("background-color: rgb(255, 218, 100);")

    def __button_unhovered(self, event, button):
        button.setStyleSheet(self.__current_stylesheet)

    def __user_button_clicked(self):
        self.__user_verification_window.resize(self.width(), self.height())
        self.__user_verification_window.move(self.pos())
        self.hide()
        self.__user_verification_window.show()
