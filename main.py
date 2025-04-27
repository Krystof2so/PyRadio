import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl, Qt
from PySide6.QtGui import QMovie


class RadioApp(QWidget):
    def __init__(self):
        super().__init__()

        # Configuration de la fenêtre principale
        self.setWindowTitle("Radio France")
        self.setFixedSize(480, 450)  # Taille fixe de la fenêtre

        # Dictionnaire des radios avec leurs noms et URLs (sources urls : https://fluxurlradio.fr/)
        self.radios = {
            "FIP": "http://direct.fipradio.fr/live/fip-midfi.mp3",
            "France Culture": "http://direct.franceculture.fr/live/franceculture-midfi.mp3",
            "France Info": "http://direct.franceinfo.fr/live/franceinfo-midfi.mp3",
            "France Inter": "http://direct.franceinter.fr/live/franceinter-midfi.mp3",
            "France Musique": "http://direct.francemusique.fr/live/francemusique-midfi.mp3",
            "Mouv'": "http://direct.mouv.fr/live/mouv-midfi.mp3"
        }

        # Layout principale horizontal :
        main_layout = QGridLayout()

        # Compteurs pour les positions dans la grille
        row, col = 0, 0

        # Création des boutons pour chaque radio
        for radio_name in self.radios.keys():
            button = QPushButton(f"{radio_name}")
            button.clicked.connect(lambda _, name=radio_name: self.play_radio(name))
            main_layout.addWidget(button, row, col)

            # Mise à jour des positions
            col += 1
            if col == 2:  # Si on atteint la troisième colonne, passer à la ligne suivante
                col = 0
                row += 1

        # Label pour afficher l'animation des ondes sonores
        self.animation_label = QLabel(self)
        self.animation_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.animation_label, 3, 0, 1, 2)

        # Charger l'animation GIF
        self.movie = QMovie("./IMG/onde.gif")  # Remplacez par le chemin de votre GIF
        self.animation_label.setMovie(self.movie)
        self.movie.jumpToFrame(0)

        # Boutons de contrôle pour le lecteur :
        self.play_pause_button = QPushButton()
        self.play_pause_button.clicked.connect(self.toggle_play_pause)
        main_layout.addWidget(self.play_pause_button, 5, 0, 2, 2)

        # Configuration du layout pour la fenêtre :
        self.setLayout(main_layout)

        # Initialisation du lecteur multimédia
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)

        self.current_radio = None

    def play_radio(self, radio_name):
        # Récupérer l'URL de la radio à partir du dictionnaire
        url = QUrl(self.radios[radio_name])
        self.player.setSource(url)
        self.current_radio = radio_name
        self.play_pause_button.setText(f"{self.current_radio} (clic pour pause)")
        self.player.play()
        self.movie.start()

    def toggle_play_pause(self):
        if self.player.playbackState() == QMediaPlayer.PlayingState:
            self.player.pause()
            self.movie.stop()
            self.play_pause_button.setText("En pause...")
        else:
            self.player.play()
            self.movie.start()
            self.play_pause_button.setText(f"{self.current_radio} (clic pour pause)" if self.current_radio else "")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RadioApp()
    window.show()
    sys.exit(app.exec())

