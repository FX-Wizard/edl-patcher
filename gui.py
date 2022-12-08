import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QFileDialog, QLineEdit
from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QPixmap

from main import fixMultipleEDL

class DropWidget(QLabel):
    def __ini__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.acceptDrops(True)
        self.dropped = None

    def dragEnterEvent(self, event):
        print('DRAG ENTER EVENT!')
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(Qt.CopyAction)
            event.accept()

            links = []
            print(event.mimeData().urls())
            self.onDropped(event.mimeData().urls())
        else:
            event.ignore()

    def onDropped(self, data):
        if self.dropped:
            self.dropped(data)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('EDL Patcher')

        self.layout = QVBoxLayout()

        self.dropWidget = DropWidget(self)
        self.layout.addWidget(self.dropWidget)

        # pixmap = QPixmap('image.jpg')
        # self.dropWidget.setPixmap(pixmap)
        # self.resize(pixmap.width(), pixmap.height())

        self.lineEdit = QLineEdit(self)
        self.lineEdit.setPlaceholderText('Regex search pattern')

        self.layout.addWidget(self.lineEdit)

        self.button = QPushButton('Open EDL(s)', self)
        self.button.clicked.connect(self.loadFile)

        self.layout.addWidget(self.button)

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

    def loadFile(self):
        if self.lineEdit.text() == '':
            print('ERROR: no search pattern entered')
            return False

        fileNames = QFileDialog.getOpenFileNames(self,
            'Open EDL', '', 'EDL Files (*.edl)')
        print(fileNames[0])
        fixMultipleEDL(fileNames[0], self.lineEdit.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())