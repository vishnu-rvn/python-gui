import sys
from PyQt4 import QtGui

class Mainwindow(QtGui.QMainWindow):
    def __init__(self,parent = None):
        QtGui.QMainWindow.__init__(self,parent)
        self.initUI()

    def initToolbar(self):

        self.newAction = QtGui.QAction(QtGui.QIcon('icon/file-1.png'),'New',self)
        self.newAction.setStatusTip("Create New File")
        self.newAction.triggered.connect(self.new)
        self.newAction.setShortcut('Ctrl+N')

        self.openAction = QtGui.QAction(QtGui.QIcon('icon/folder.png'),'Open',self)
        self.openAction.setStatusTip("Open an existing file")
        self.openAction.triggered.connect(self.open)
        self.openAction.setShortcut('Ctrl+O')

        self.saveAction = QtGui.QAction(QtGui.QIcon('icon/save.png'),'Save',self)
        self.saveAction.setStatusTip('Save to file')
        self.saveAction.triggered.connect(self.save)
        self.saveAction.setShortcut('Ctrl+S')

        self.previewAction = QtGui.QAction(QtGui.QIcon('icon/preview.png'),'Preview',self)
        self.previewAction.setStatusTip('Print Preview')
        self.previewAction.triggered.connect(self.preview)
        self.previewAction.setShortcut('Ctrl+Shift+P')

        self.printAction = QtGui.QAction(QtGui.QIcon('icon/print.png'),'Print',self)
        self.printAction.setStatusTip('Print file')
        self.printAction.triggered.connect(self.print)
        self.printAction.setShortcut('Ctrl+P')

        self.cutAction = QtGui.QAction(QtGui.QIcon('icon/scissors.png'),'Cut',self)
        self.cutAction.setStatusTip('Cut')
        self.cutAction.triggered.connect(self.text.cut)
        self.cutAction.setShortcut('Ctrl+X')

        self.copyAction = QtGui.QAction(QtGui.QIcon('icon/copy.png'), 'Copy', self)
        self.copyAction.setStatusTip('Copy')
        self.copyAction.triggered.connect(self.text.copy)
        self.copyAction.setShortcut('Ctrl+C')

        self.pasteAction = QtGui.QAction(QtGui.QIcon('icon/paste.png'), 'Paste', self)
        self.pasteAction.setStatusTip('Paste')
        self.pasteAction.triggered.connect(self.text.paste)
        self.pasteAction.setShortcut('Ctrl+V')

        self.redoAction = QtGui.QAction(QtGui.QIcon('icon/redo.png'), 'Redo', self)
        self.redoAction.setStatusTip('Redo')
        self.redoAction.triggered.connect(self.text.redo)
        self.redoAction.setShortcut('Ctrl+Shift+Z')

        self.undoAction = QtGui.QAction(QtGui.QIcon('icon/undo.png'), 'Undo', self)
        self.undoAction.setStatusTip('Undo')
        self.undoAction.triggered.connect(self.text.undo)
        self.undoAction.setShortcut('Ctrl+Z')

        self.bulletAction = QtGui.QAction(QtGui.QIcon('icon/list.png'), 'Bullets', self)
        self.bulletAction.setStatusTip('Bullet list')
        self.bulletAction.triggered.connect(self.bulletList)

        self.numberedAction = QtGui.QAction(QtGui.QIcon('icon/list-1.png'), 'Numbered', self)
        self.numberedAction.setStatusTip('Numbered list')
        self.numberedAction.triggered.connect(self.numberList)

        self.toolbar = self.addToolBar("Options")
        #self.toolbar.setMovable(False)
        self.toolbar.addAction(self.newAction)
        self.toolbar.addAction(self.openAction)
        self.toolbar.addAction(self.saveAction)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.previewAction)
        self.toolbar.addAction(self.printAction)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.cutAction)
        self.toolbar.addAction(self.copyAction)
        self.toolbar.addAction(self.pasteAction)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.redoAction)
        self.toolbar.addAction(self.undoAction)
        self.toolbar.addAction(self.bulletAction)
        self.toolbar.addAction(self.numberedAction)

        self.addToolBarBreak()

    def initFormatter(self):

        fontBox = QtGui.QFontComboBox(self)
        fontBox.currentFontChanged.connect(self.fontFamily)

        fontSize = QtGui.QComboBox(self)
        fontSize.setEditable(True)

        fontSize.setMinimumContentsLength(3)
        fontSize.activated.connect(self.fontSize)

        fontSizes = ['6','7','8','9','10','11','12','13','14',
             '15','16','18','20','22','24','26','28',
             '32','36','40','44','48','54','60','66',
             '72','80','88','96']

        for i in fontSizes:
            fontSize.addItem(i)

        self.formatter = self.addToolBar('Format')

    def initMenubar(self):
        menubar = self.menuBar()

        file = menubar.addMenu('File')
        file.addAction(self.newAction)
        file.addAction(self.openAction)
        file.addAction(self.saveAction)

        edit = menubar.addMenu('Edit')
        edit.addAction(self.previewAction)
        edit.addAction(self.printAction)
        edit.addAction(self.cutAction)
        edit.addAction(self.bulletAction)
        edit.addAction(self.numberedAction)

        view = menubar.addMenu('View')

    def initUI(self):
        self.setGeometry(100,100,1030,800)
        self.setWindowTitle("Writer")

        self.filename = ''

        self.text = QtGui.QTextEdit(self)
        self.setCentralWidget(self.text)

        self.initToolbar()
        self.initMenubar()
        #self.initFormatter()

        self.statusbar = self.statusBar()

    def new(self):
        quit_message = 'Are you sure you want to clear?'
        result = QtGui.QMessageBox.question(self,'Message',quit_message,QtGui.QMessageBox.Yes,QtGui.QMessageBox.No)
        if result == QtGui.QMessageBox.Yes:
            self.text.clear()
        else:
            pass


    def open(self):
        self.filename = QtGui.QFileDialog.getOpenFileName(self,'Open File','.','*.txt')
        if self.filename:
            with open(self.filename,'rt') as file:
                self.text.setText(file.read())

    def save(self):
        if not self.filename:
            self.filename = QtGui.QFileDialog.getSaveFileName(self,'Save File')

        if not self.filename.endswith('.txt'):
            self.filename += '.txt'

        with open(self.filename,'wt') as file:
            file.write(self.text.toHtml())


    def preview(self):
        preview = QtGui.QPrintPreviewDialog()
        preview.paintRequested.connect(lambda p: self.text.print_(p))
        preview.exec_()

    def print(self):
        dialog = QtGui.QPrintDialog()
        if dialog.exec_() == QtGui.QDialog.Accepted:
            self.text.document().print_(dialog.printer())

    def bulletList(self):
        cursor = self.text.textCursor()
        cursor.insertList(QtGui.QTextListFormat.ListDisc)

    def numberList(self):
        cursor = self.text.textCursor()
        cursor.insertList(QtGui.QTextListFormat.ListDecimal)

    def fontFamily(self,font):
        self.text.setCurorentFont(font)

    def fontSize(self,fontsize):
        self.text.setFontPointSize(int(fontsize))


def main():
    app = QtGui.QApplication(sys.argv)
    main = Mainwindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()