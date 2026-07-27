from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit
)

class MetadataWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.camera = QLineEdit()
        self.artist = QLineEdit()
        self.description = QLineEdit()
        self.date = QLineEdit()
        self.copyright = QLineEdit()

        fields = [
            ("Camera", self.camera),
            ("Artist", self.artist),
            ("Description", self.description),
            ("Date Taken", self.date),
            ("Copyright", self.copyright)
        ]

        for name,field in fields:
            layout.addWidget(
                QLabel(name)
            )
            layout.addWidget(
                field
            )
        self.setLayout(
            layout
        )

    def get_metadata(self):
        return {
            "camera":
            self.camera.text(),
            "artist":
            self.artist.text(),
            "description":
            self.description.text(),
            "date":
            self.date.text(),
            "copyright":
            self.copyright.text()
        }

    def set_metadata(self,data):
        self.camera.setText(
            data.get("camera","")
        )
        self.artist.setText(
            data.get("artist","")
        )
        self.description.setText(
            data.get("description","")
        )
        self.date.setText(
            data.get("date","")
        )
        self.copyright.setText(
            data.get("copyright","")
        )