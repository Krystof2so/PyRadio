from PySide6.QtCore import QUrl
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput

class RadioModel:
    def __init__(self):
        self.radios = {
            "FIP": "http://direct.fipradio.fr/live/fip-midfi.mp3",
            "France Culture": "http://direct.franceculture.fr/live/franceculture-midfi.mp3",
            "France Info": "http://direct.franceinfo.fr/live/franceinfo-midfi.mp3",
            "France Inter": "http://direct.franceinter.fr/live/franceinter-midfi.mp3",
            "France Musique": "http://direct.francemusique.fr/live/francemusique-midfi.mp3",
            "Mouv'": "http://direct.mouv.fr/live/mouv-midfi.mp3"
        }
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        self.current_radio = None

    def get_radio_url(self, radio_name):
        return QUrl(self.radios.get(radio_name))

    def play_radio(self, radio_name):
        self.current_radio = radio_name
        self.player.setSource(self.get_radio_url(radio_name))
        self.player.play()

    def toggle_play_pause(self):
        if self.player.playbackState() == QMediaPlayer.PlayingState:
            self.player.pause()
        else:
            self.player.play()

