import sys

from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *

from images_path import create_annotation
from images_copy import create_dataset2, create_annotation2
from images_random import create_dataset3, create_annotation3
from images_iterator import Iterator

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        self.initIterator()
        self.createMenuBar()
        self.createAction()
        self.createToolBar()
        
    def initUI(self):
    
        
        # qbtn=QPushButton('Quit',self)
        # qbtn.clicked.connect(QCoreApplication.instance().quit)
        # qbtn.resize(qbtn.sizeHint())
        # qbtn.move(50,50)
                
        self.resize(1200,900)
        self.center()
        self.setWindowTitle('Cat and Dog')
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        
        cat_btn=QPushButton('Next cat',self)
        dog_btn=QPushButton('Next dog',self)

        
        self.lbl = QLabel(self)
        
        hbox = QHBoxLayout()
        hbox.addSpacing(1)
        hbox.addWidget(cat_btn)
        hbox.addWidget(dog_btn)

        vbox = QVBoxLayout()
        vbox.addSpacing(1)
        vbox.addWidget(self.lbl)
        vbox.addLayout(hbox)

        self.centralWidget.setLayout(vbox)
        
        cat_btn.clicked.connect(self.nextcat)
        dog_btn.clicked.connect(self.nextdog)

        self.folderpath = ' '
        
        #self.showMaximized()
        
        self.show()
     
    def initIterator(self):
        self.cat=Iterator('cat','dataset')
        self.dog=Iterator('dog','dataset')
        
    def nextcat(self):
        lbl_size = self.lbl.size()
        next_image = next(self.cat)
        if next_image != None:
            img = QPixmap(next_image).scaled(
                lbl_size, aspectRatioMode=Qt.KeepAspectRatio)
            self.lbl.setPixmap(img)
            self.lbl.setAlignment(Qt.AlignCenter)
        else:        
            self.initIterator()
            self.nextcat()
                 
    def nextdog(self):
        lbl_size = self.lbl.size()
        next_image = next(self.dog)
        if next_image != None:
            img = QPixmap(next_image).scaled(
                lbl_size, aspectRatioMode=Qt.KeepAspectRatio)
            self.lbl.setPixmap(img)
            self.lbl.setAlignment(Qt.AlignCenter)
        else:        
            self.initIterator()
            self.nextdog()
        
        
    def center(self):
        qr=self.frameGeometry()
        cp=QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    
    def createMenuBar(self):
        
        menuBar = self.menuBar()
        self.fileMenu = menuBar.addMenu('&File')
        
        self.annotMenu = menuBar.addMenu('&Annotation')
        
        self.dataMenu=menuBar.addMenu('&Datasets')
        
    def createToolBar(self):
        fileToolBar=self.addToolBar('File')
        fileToolBar.addAction(self.exitAction)
        
        annotToolBar=self.addToolBar('File')
        annotToolBar.addAction(self.createAnnotAction)
        
    def createAction(self):
        self.exitAction = QAction('&Exit')
        self.exitAction.triggered.connect(qApp.quit)

        self.changeAction = QAction('&Change dataset')
        self.changeAction.triggered.connect(self.changeDataset)

        self.createAnnotAction = QAction('&Create annotation for current dataset')
        self.createAnnotAction.triggered.connect(self.createAnnotation)

        self.createData2Action = QAction('&Create dataset2')
        self.createData2Action.triggered.connect(self.createDataset2)

        self.createData3Action = QAction('&Create dataset3')
        self.createData3Action.triggered.connect(self.createDataset3)
        
    def createAnnotation(self):
        if 'dataset2' in str(self.folderpath):
            create_annotation2()
        elif 'dataset3' in str(self.folderpath):
            create_annotation3()
        elif 'dataset' in str(self.folderpath):
            create_annotation()
            
    def createDataset2(self):
        create_dataset2()
        self.dataMenu.addAction(self.createData3Action)
        
        
    def createDataset3(self):
        create_dataset3()
        
        
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