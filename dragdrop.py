from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout
)

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap


class ImageLabel(QLabel):

    imageDropped = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.file_path = None
        self.setAcceptDrops(True)
        self.setAlignment(Qt.AlignCenter)
        self.setText("Drop Image Here")
        self.setMinimumSize(500,350)
        self.setScaledContents(False)

        self.setStyleSheet("""
            QLabel{
                border:4px dashed #aaa;
            }
        """)

    def dragEnterEvent(self,event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()

    def dragMoveEvent(self,event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self,event):
        urls = event.mimeData().urls()
        if not urls:
            return

        self.file_path = urls[0].toLocalFile()
        self.load_image(self.file_path)
        # Tell UI.py image arrived
        self.imageDropped.emit()
        event.acceptProposedAction()

    def load_image(self,file_path):
        pixmap = QPixmap(file_path)
        if pixmap.isNull():
            self.setText(
                "Invalid Image"
            )
            return

        scaled = pixmap.scaled(self.size(),Qt.KeepAspectRatio,Qt.SmoothTransformation)
        self.setPixmap(scaled)

    def show_image(self,file_path):
        self.load_image(file_path)


class DragDropWidget(QWidget):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.imageLabel = ImageLabel()
        layout.addWidget(
            self.imageLabel
        )
        self.setLayout(layout)