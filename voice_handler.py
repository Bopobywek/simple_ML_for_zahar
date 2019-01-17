import sys
from PyQt5.QtWidgets import QApplication
from voice_handler_d import Ui_Dialog
from PyQt5.QtWidgets import QDialog
from wav_recorder import record, CHUNK, FORMAT, CHANNELS, RATE, WAVE_OUTPUT_FILENAME


class VoiceHandler(QDialog, Ui_Dialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.off)

    def off(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    voice = VoiceHandler()
    voice.show()
    sys.exit(app.exec_())
