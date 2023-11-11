from PyQt5.QtWidgets import (QPushButton, QLabel, QMainWindow,
                            QWidget, QVBoxLayout, QHBoxLayout,
                            QLineEdit)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class UserVerification(QMainWindow):
    def __init__(self, first_window):
        super().__init__()
        self.__first_window = first_window
        self.setWindowTitle("User verification")
        self.setStyleSheet("QWidget#MyWindow { background-image: url('C:/Users/Gulzhaev/Downloads/Telegram Desktop/IMG_5777.PNG'); background-repeat: no-repeat; background-position: center; }")
        #"C:/Users/Gulzhaev/Downloads/Telegram Desktop/IMG_5777.PNG"
        self.setObjectName("MyWindow")

        self.__go_back_button = QPushButton("←")
        self.__go_back_button.clicked.connect(self.__go_back_button_clicked)
        self.__go_back_button.setCursor(Qt.PointingHandCursor)
        self.__go_back_button.setFixedWidth(40)
        self.__go_back_button.setStyleSheet("color: black; background-color: rgb(255, 193, 0);")


        self.__widget_for_signing_in = QWidget()

        self.__opening_label = QLabel("<html><b><font size='20'>PRO BURGERS</html></b></font>")
        self.__opening_label.setStyleSheet("color: rgb(255, 193, 0);")
        self.__operation_result_label = QLabel()

        self.__username_line_edit = QLineEdit()
        self.__username_line_edit.setStyleSheet("color: black; background-color: rgb(255, 193, 0);")
        self.__username_line_edit.setPlaceholderText("enter your username")

        self.__password_line_edit = QLineEdit()
        self.__password_line_edit.setStyleSheet("color: black; background-color: rgb(255, 193, 0);")
        self.__password_line_edit.setPlaceholderText("enter your password")


        FONT = QFont()
        FONT.setBold(True)
        FONT.setPointSize(16)

        self.__sign_in_button = QPushButton("SIGN - IN")
        self.__sign_in_button.enterEvent = lambda event: self.__button_hovered(event, self.__sign_in_button)
        self.__sign_in_button.setCursor(Qt.PointingHandCursor)
        self.__sign_in_button.leaveEvent = lambda event: self.__button_unhovered(event, self.__sign_in_button)
        self.__sign_in_button.setStyleSheet("color: black; background-color: rgb(255, 193, 0);")
        self.__sign_in_button.setMinimumSize(120, 80)
        self.__sign_in_button.setFont(FONT)

        self.__verification_layout = self.__layout_maker(
                                  True,
                                  self.__opening_label,
                                  self.__operation_result_label,
                                  self.__username_line_edit,
                                  self.__password_line_edit,
                                  self.__sign_in_button
        )
        self.__verification_layout.setAlignment(self.__opening_label, Qt.AlignCenter)
        self.__widget_for_signing_in.setLayout(self.__verification_layout)
        self.__widget_for_signing_in.setStyleSheet("QWidget#MyBorder { border: 2px solid yellow; padding: 10px; }")
        self.__widget_for_signing_in.setObjectName("MyBorder")
        self.__username_line_edit.setObjectName("MyBorder")
        self.__password_line_edit.setObjectName("MyBorder")

        self.__sign_up_label = QLabel("<html><b>don't have an account yet ? </html></b>")
        self.__sign_up_label.setStyleSheet("color: rgb(255, 193, 0);")
        self.__link_to_sign_up_window = QPushButton("sign-up")
        self.__link_to_sign_up_window.setFixedSize(60, 15)
        self.__link_to_sign_up_window.setCursor(Qt.PointingHandCursor)
        self.__link_to_sign_up_window.setStyleSheet("color: rgb(255, 193, 0); background-color: black;")

        self.__sign_up_layout = self.__layout_maker(
                                                      False, self.__sign_up_label,
                                                      self.__link_to_sign_up_window
                                                    )

        self.__sign_up_widget = QWidget()
        self.__sign_up_widget.setLayout(self.__sign_up_layout)

        self.__main_layout = self.__layout_maker(
                        True,
                        self.__widget_for_signing_in,
                        self.__sign_up_widget
                        )
        self.__main_widget = QWidget()
        self.__main_widget.setLayout(self.__main_layout)
        self.__main_widget.setMinimumSize(600, 350)
        self.__main_widget.setMaximumSize(1000, 350)

        self.__the_main_layout = QVBoxLayout()
        self.__the_main_layout.addWidget(self.__go_back_button)
        self.__the_main_layout.setAlignment(self.__go_back_button, Qt.AlignLeft)
        self.__the_main_layout.addWidget(self.__main_widget)
        self.__the_main_layout.setAlignment(self.__main_widget, Qt.AlignCenter)
        self.__the_main_widget = QWidget()
        self.__the_main_widget.setLayout(self.__the_main_layout)

        self.setCentralWidget(self.__the_main_widget)

    def __layout_maker(self, is_vertical, * widgets):
        if is_vertical:
            layout = QVBoxLayout()
        else:
            layout = QHBoxLayout()
        for widget in widgets:
            layout.addWidget(widget)
        return layout

    def __go_back_button_clicked(self):
        self.__first_window.resize(self.width(), self.height())
        self.__first_window.move(self.pos())
        self.hide()
        self.__first_window.show()

    def __button_hovered(self, event, button):
        self.__current_stylesheet = button.styleSheet()
        button.setStyleSheet("background-color: rgb(255, 218, 100);")
        button.setText("LET'S EAT")

    def __button_unhovered(self, event, button):
        button.setText("SIGN - IN")
        button.setStyleSheet(self.__current_stylesheet)


