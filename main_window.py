from PyQt5.QtWidgets import *
import sys

from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QIcon, QPixmap

from images_path import create_annotation
from images_copy import create_dataset2, create_annotation2
from images_iterator import Iterator

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        self.createMenuBar()
        # self.initIterator()
        
    def initUI(self):
    
        
        # qbtn=QPushButton('Quit',self)
        # qbtn.clicked.connect(QCoreApplication.instance().quit)
        # qbtn.resize(qbtn.sizeHint())
        # qbtn.move(50,50)
                
        # self.setGeometry(300,300,300,200)
        
        # self.menu_bar = self.menuBar()
        # self.dataMenu = self.menu_bar.addMenu("Data")
        
        self.resize(500,150)
        self.center()
        self.setWindowTitle('Cat and Dog')
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        
        cat_btn=QPushButton('Next cat',self)
        dog_btn=QPushButton('Next dog',self)
        
        self.showMaximized()

        
        
    # def initIterator(self):
    #     self.cat=Iterator('cat','dataset')
    #     self.dog=Iterator('dog','dataset')
        
    def center(self):
        qr=self.frameGeometry()
        cp=QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.center())
        
    
    def createMenuBar(self):
        
        menuBar = self.menuBar()
        self.fileMenu = menuBar.addMenu('&File')
        
        
    def closeEvent(self,event):
        reply=QMessageBox.question(self,'Message', "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)
        
        if reply==QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())