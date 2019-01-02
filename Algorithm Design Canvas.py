import sys
from PyQt5.QtWidgets import (QMainWindow,QApplication,QWidget,
 QPlainTextEdit,QGridLayout,QLineEdit,QLabel)

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Algorithm Design Canvas'
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        grid.setSpacing(10)

        #Question name
        algoLabel = QLabel("Algorithm name:")
        algoName = QLineEdit()
        grid.addWidget(algoLabel,1,0)
        grid.addWidget(algoName,1,1,1,1)

        #Constraints textbox
        constraintsLabel = QLabel("Constraints")
        constraintsTextbox = QPlainTextEdit(self)
        grid.addWidget(constraintsLabel,2,0,1,1)
        grid.addWidget(constraintsTextbox,3,0,1,1)

        #Ideas textbox
        ideasLabel = QLabel("Ideas")
        ideasTextbox = QPlainTextEdit(self)
        grid.addWidget(ideasLabel,4,0,1,1)
        grid.addWidget(ideasTextbox,5,0,1,1)

        #Testcases textbox
        testLabel = QLabel("Testcases")
        testTextbox = QPlainTextEdit(self)
        grid.addWidget(testLabel,6,0,1,1)
        grid.addWidget(testTextbox,7,0,1,1)
        
        #Code textbox
        codeLabel = QLabel("Code")
        codeTextbox = QPlainTextEdit(self)
        grid.addWidget(codeLabel,2,1,1,1)
        grid.addWidget(codeTextbox,3,1,5,1)
        self.setLayout(grid)
        self.setWindowTitle(self.title)
        self.setGeometry(300,300,350,300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
