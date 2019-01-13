import sys
from PyQt5.QtWidgets import QApplication
from auth_d import Ui_Dialog
from auth2 import Auth2
from PyQt5.QtWidgets import QDialog


class Auth(QDialog, Ui_Dialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
        self.status = False

    def run(self):
        auth2 = Auth2()
        auth2.exec_()
        if auth2.auth_state:
            self.status = True
            self.close()

    def closeEvent(self, event):
        if self.status:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    auth = Auth()
    auth.show()
    sys.exit(app.exec_())
