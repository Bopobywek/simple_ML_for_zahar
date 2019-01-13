import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog, QMessageBox
from cart_d import Ui_Dialog
from auth import Auth
from  codereader import CodeReader


class Cart(QDialog, Ui_Dialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.start()
        self.exit_from_account.clicked.connect(self.exit_from_acc)
        self.add_to_cart.clicked.connect(self.append_product)
        self.product_cost.clicked.connect(self.cost_of_product)
        self.add_to_cart_2.clicked.connect(self.delete_product)

    def start(self):
        self.main_menu = Auth()
        self.main_menu.exec_()

    def append_product(self):
        reader = CodeReader()
        reader.exec_()
        if reader.info_product:
            self.user_cart.addItem(reader.info_product["name"])

    def delete_product(self):
        self.user_cart.item(self.user_cart.currentIndex())

    def use_microphone(self):
        pass

    def exit_from_acc(self):
        self.main_menu.status = False
        self.main_menu.auth2.auth_state = False
        self.start()

    def cost_of_product(self):
        reader = CodeReader()
        reader.exec_()
        if reader.info_product:
            self.cost_msg_box(reader.info_product['cost'])

    def cost_msg_box(self, cost):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.resize(300, 300)
        msg.move(self.x() + 300, self.y() + 350)
        msg.setText("Цена:")
        msg.setWindowTitle("Цена этого продукта")
        msg.setText("{}P".format(cost))
        msg.setStandardButtons(QMessageBox.Cancel)
        msg.exec_()
        
    def help(self):
        pass

    def create_list(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cart = Cart()
    cart.show()
    sys.exit(app.exec_())

