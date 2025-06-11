from PySide6.QtWidgets import QWidget, QPushButton, QGridLayout, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QMovie

class RadioView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Radio France")
        self.setFixedSize(480, 450)

        self.main_layout = QGridLayout()
        self.setLayout(self.main_layout)

        self.animation_label = QLabel(self)
        self.animation_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.animation_label, 3, 0, 1, 2)

        self.movie = QMovie("./assets/IMG/onde.gif")
        self.animation_label.setMovie(self.movie)
        self.movie.jumpToFrame(0)

        self.play_pause_button = QPushButton()
        self.main_layout.addWidget(self.play_pause_button, 5, 0, 2, 2)

    def set_play_pause_button_text(self, text):
        self.play_pause_button.setText(text)

    def update_animation_state(self, state):
        if state == "play":
            self.movie.start()
        else:
            self.movie.stop()

