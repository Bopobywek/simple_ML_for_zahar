import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog
from cart_d import Ui_Dialog
from auth import Auth


class Cart(QDialog, Ui_Dialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.start()

    def start(self):
        main_menu = Auth()
        main_menu.exec_()

    def append_product(self):
        pass

    def delete_product(self):
        pass

    def use_microphone(self):
        pass

    def exit_from_account(self):
        pass

    def cost_of_product(self):
        pass

    def help(self):
        pass

    def microphone(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cart = Cart()
    cart.show()
    sys.exit(app.exec_())

