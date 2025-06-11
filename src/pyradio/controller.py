from functools import partial
from PySide6.QtWidgets import QPushButton
from PySide6.QtMultimedia import QMediaPlayer

class RadioController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.setup_connections()

    def setup_connections(self):
        for idx, radio_name in enumerate(self.model.radios.keys()):
            row, col = divmod(idx, 2)
            button = QPushButton(radio_name)
            button.clicked.connect(partial(self.play_radio, radio_name))
            self.view.main_layout.addWidget(button, row, col)

        self.view.play_pause_button.clicked.connect(self.toggle_play_pause)

    def play_radio(self, radio_name):
        self.model.play_radio(radio_name)
        self.view.set_play_pause_button_text(f"{radio_name} (clic pour pause)")
        self.view.update_animation_state("play")

    def toggle_play_pause(self):
        self.model.toggle_play_pause()
        if self.model.player.playbackState() == QMediaPlayer.PlayingState:
            self.view.set_play_pause_button_text(f"{self.model.current_radio} (clic pour pause)")
            self.view.update_animation_state("play")
        else:
            self.view.set_play_pause_button_text("En pause...")
            self.view.update_animation_state("pause")

