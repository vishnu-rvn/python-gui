import sys
from PyQt4 import QtGui, QtCore

class Calculator(QtGui.QMainWindow):
    def __init__(self):
        super(Calculator,self).__init__()
        self.setGeometry(800,200,True,True)
        self.setWindowTitle('Calculator')
        #self.setSizePolicy()
        self.home()

    def home(self):
        centralwidget = QtGui.QWidget()

        self.btn1 = QtGui.QPushButton('1',self)
        self.btn1.clicked.connect(lambda :self.entryAppend('1'))
        self.btn1.setFixedSize(40,40)

        self.btn2 = QtGui.QPushButton('2', self)
        self.btn2.clicked.connect(lambda: self.entryAppend('2'))
        self.btn2.setFixedSize(40,40)

        self.btn3 = QtGui.QPushButton('3', self)
        self.btn3.clicked.connect(lambda: self.entryAppend('3'))
        self.btn3.setFixedSize(40, 40)

        self.btn4 = QtGui.QPushButton('4', self)
        self.btn4.clicked.connect(lambda: self.entryAppend('4'))
        self.btn4.setFixedSize(40, 40)

        self.btn5 = QtGui.QPushButton('5', self)
        self.btn5.clicked.connect(lambda: self.entryAppend('5'))
        self.btn5.setFixedSize(40, 40)

        self.btn6 = QtGui.QPushButton('6', self)
        self.btn6.clicked.connect(lambda: self.entryAppend('6'))
        self.btn6.setFixedSize(40, 40)

        self.btn7 = QtGui.QPushButton('7', self)
        self.btn7.clicked.connect(lambda: self.entryAppend('6'))
        self.btn7.setFixedSize(40, 40)

        self.btn8 = QtGui.QPushButton('8', self)
        self.btn8.clicked.connect(lambda: self.entryAppend('8'))
        self.btn8.setFixedSize(40, 40)

        self.btn9 = QtGui.QPushButton('9', self)
        self.btn9.clicked.connect(lambda: self.entryAppend('9'))
        self.btn9.setFixedSize(40, 40)

        self.btn0 = QtGui.QPushButton('0', self)
        self.btn0.clicked.connect(lambda: self.entryAppend('0'))
        self.btn0.setFixedSize(40, 40)

        self.btnC = QtGui.QPushButton('C', self)
        self.btnC.clicked.connect(lambda: self.entryDelete())
        self.btnC.setFixedSize(40, 40)

        self.btndot = QtGui.QPushButton('.', self)
        self.btndot.clicked.connect(lambda: self.entryAppend('.'))
        self.btndot.setFixedSize(40, 40)

        self.btnplus = QtGui.QPushButton('+', self)
        self.btnplus.clicked.connect(lambda: self.entryAppend('+'))
        self.btnplus.setFixedSize(40, 40)

        self.btndivide = QtGui.QPushButton('/', self)
        self.btndivide.clicked.connect(lambda: self.entryAppend('/'))
        self.btndivide.setFixedSize(40, 40)

        self.btnminus = QtGui.QPushButton('-', self)
        self.btnminus.clicked.connect(lambda: self.entryAppend('-'))
        self.btnminus.setFixedSize(40, 40)

        self.btnmult = QtGui.QPushButton('*', self)
        self.btnmult.clicked.connect(lambda: self.entryAppend('*'))
        self.btnmult.setFixedSize(40, 40)

        self.btnequal = QtGui.QPushButton('=', self)
        self.btnequal.clicked.connect(lambda: self.evaluate())
        self.btnequal.setFixedSize(40, 40)

        self.btnexit = QtGui.QPushButton('Exit',self)
        self.btnexit.clicked.connect(lambda: self.appExit())
        self.btnexit.setFixedSize(40,40)

        self.btnCE = QtGui.QPushButton('CE',self)
        self.btnCE.clicked.connect(lambda: self.entryClear())
        self.btnCE.setFixedSize(40,40)

        self.entry = QtGui.QLineEdit()
        font = self.entry.font()
        font.setPointSize(25)
        self.entry.setText('0')
        self.entry.setReadOnly(True)
        self.entry.setFont(font)

        self.grid = QtGui.QGridLayout()
        self.grid.addWidget(self.entry,0,0,1,0)

        self.grid.addWidget(self.btn1, 5, 0)
        self.grid.addWidget(self.btn2, 5, 1)
        self.grid.addWidget(self.btn3, 5, 2)
        self.grid.addWidget(self.btn4, 4, 0)
        self.grid.addWidget(self.btn5, 4, 1)
        self.grid.addWidget(self.btn6, 4, 2)
        self.grid.addWidget(self.btn7, 3, 0)
        self.grid.addWidget(self.btn8, 3, 1)
        self.grid.addWidget(self.btn9, 3, 2)
        self.grid.addWidget(self.btn0, 6, 1)
        self.grid.addWidget(self.btnC, 2, 0)
        self.grid.addWidget(self.btndot, 6, 0)
        self.grid.addWidget(self.btnplus, 6, 3)
        self.grid.addWidget(self.btnminus,4 , 3)
        self.grid.addWidget(self.btnmult, 5, 3)
        self.grid.addWidget(self.btndivide, 3, 3)
        self.grid.addWidget(self.btnexit,2,2)
        self.grid.addWidget(self.btnCE,2,1)

        self.grid.addWidget(self.btnequal,6,2)

        centralwidget.setLayout(self.grid)
        self.setCentralWidget(centralwidget)
        self.show()

    def entryAppend(self,text):
        txt = self.entry.text()
        if txt == '0':
            self.entry.clear()
            self.entry.insert(text)
        else:
            self.entry.insert(text)

    def entryDelete(self):
        txt = self.entry.text()
        if not txt:
            self.entry.setText('0')
        else:
            self.entry.backspace()

    def entryClear(self):
        self.replace('0')

    def appExit(self):
        quit_message = 'Are you sure you want to exit?'
        result = QtGui.QMessageBox.question(self,'Message',quit_message,QtGui.QMessageBox.Yes,QtGui.QMessageBox.No)
        if result == QtGui.QMessageBox.Yes:
            exit()
        else:
            pass

    def evaluate(self):
        try:
            text = self.entry.text()
            result = str(eval(text))
            self.replace(result)
        except Exception:
            self.replace('Invalid')

    def replace(self,result):
        self.entry.clear()
        self.entry.insert(result)


app = QtGui.QApplication(sys.argv)
Gui = Calculator()
sys.exit(app.exec_())