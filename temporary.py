from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

class BorderedButtonContainer(QWidget):
    def __init__(self):
        super().__init__()

        # Create a layout for the container
        container_layout = QVBoxLayout()

        # Create buttons and add them to the container layout
        button = QPushButton("first button")
        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")
        button3 = QPushButton("Button 3")

        container_layout.addWidget(button1)
        container_layout.addWidget(button2)
        container_layout.addWidget(button3)

        # Create a widget to act as a container for the buttons
        container_widget = QWidget()
        container_widget.setLayout(container_layout)

        # Set the border for the container widget using setStyleSheet
        container_widget.setStyleSheet("border: 2px solid red; padding: 10px;")

        main_layout = QVBoxLayout()
        main_layout.addWidget(button)
        main_layout.addWidget(container_widget)

        # Set the layout for the main widget
        self.setLayout(main_layout)

if __name__ == "__main__":
    app = QApplication([])
    window = BorderedButtonContainer()
    window.show()
    app.exec()
