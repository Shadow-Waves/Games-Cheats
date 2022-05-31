from PyQt6.QtWidgets import QMainWindow,QLabel,QTextEdit,QComboBox,QApplication
from PyQt6.QtGui import QIcon,QPixmap
from sys import argv 

class CheatsSheet(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cheats Sheet")
        self.setWindowIcon(QIcon("iconic.png"))
        self.setStyleSheet("background-color:black;")
        self.setFixedSize(600,600)

        self.game_list = QComboBox(self)
        self.game_list.setGeometry(10,50,200,50)
        self.game_list.addItem(QIcon("gtavicon.png"),"GTA V")
        self.game_list.addItem(QIcon("gtaivicon.png"),"GTA IV")
        self.game_list.addItem(QIcon("gtasaicon.png"),"GTA SA")
        self.game_list.addItem(QIcon("reddeadredemption2icon.png"),"RED DEAD REDEMPTION 2")
        self.game_list.setCurrentIndex(0)
        self.game_list.setStyleSheet("background-color:transparent;border:0px groove yellow;font-size:20px;font-weight:bold;color:lightgreen;")
        self.game_list.currentIndexChanged.connect(self.change)
        
        self.picture_label = QLabel(self)
        self.picture_label.setGeometry(270,50,300,300)
        self.picture_label.setPixmap(QPixmap("gtavicon.png").scaled(300,300))

        x = open("gtav.txt")
        self.each_game_codes_list = [(code.split(" : ",1)[1],code.split(" : ",1)[0]) for code in x]
        x.close()

        self.codes_list = QComboBox(self)
        self.codes_list.setGeometry(10,150,250,50)
        for each in self.each_game_codes_list:
            self.codes_list.addItem(each[1])
        self.codes_list.setStyleSheet("background-color:transparent;border:0px groove yellow;font-size:20px;font-weight:bold;color:lightgreen;")
        self.codes_list.currentIndexChanged.connect(self.changer)

        self.result = QTextEdit(self.each_game_codes_list[0][0],self)
        self.result.setGeometry(10,370,580,220)
        self.result.setStyleSheet("background-color:rgba(255,110,199,0.2);border:1px groove yellow;font-size:40px;font-weight:bold;color:magenta;")
        
        self.show()

    def change(self):
        x = open("" + self.game_list.currentText().replace(" ","").lower() + ".txt")
        del(self.each_game_codes_list)
        self.each_game_codes_list = [(code.split(" : ",1)[1],code.split(" : ",1)[0]) for code in x]
        x.close()
        for _ in range(self.codes_list.count()):
            self.codes_list.removeItem(0)
        for each in self.each_game_codes_list:
            self.codes_list.addItem(each[1])
        self.result.setText(self.each_game_codes_list[0][0])
        self.picture_label.setPixmap(QPixmap("" + self.game_list.currentText().replace(" ","").lower() + "icon.png").scaled(300,300))

    def changer(self):
        self.result.setText(self.each_game_codes_list[self.codes_list.currentIndex()][0])

if __name__ == "__main__":
    application = QApplication(argv)
    cheats_sheet = CheatsSheet()
    application.exec()