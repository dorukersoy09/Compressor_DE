from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QSlider,
    QComboBox,
    QPushButton,
    QSpinBox,
    QCheckBox,
    QLabel
)
from PyQt5.QtCore import Qt
from MetadataWidget import MetadataWidget


class ControlsWidget(QWidget):


    def update_quality_value(self,value):
        self.qualityValueLabel.setText(str(value))

    def toggle_metadata(self,state):
        if state:
            self.metadataWidget.show()
        else:
            self.metadataWidget.hide()

    def __init__(self):
        super().__init__()
        # QUALITY
        self.qualitySlider = QSlider(Qt.Horizontal)
        self.qualitySlider.setRange(0,100)
        self.qualitySlider.setValue(80)
        self.qualityValueLabel = QLabel("80")
        self.qualitySlider.valueChanged.connect(self.update_quality_value)
        # FORMAT
        self.formatComboBox = QComboBox()
        self.formatComboBox.addItems(["JPEG", "PNG","WEBP","BMP"])
        # WIDTH
        self.widthSpinBox = QSpinBox()
        self.widthSpinBox.setRange(1,10000)
        self.widthSpinBox.setValue(1080)
        # METADATA CHECKBOX
        self.keepMetadata = QCheckBox("Keep metadata")
        self.keepMetadata.setChecked(True)
        # METADATA EDITOR
        self.metadataWidget = MetadataWidget()
        self.keepMetadata.stateChanged.connect(self.toggle_metadata)
        # BUTTONS
        self.compressPushButton = QPushButton("Compress")
        self.downloadButton = QPushButton("Download")
        # LAYOUT
        layout = QVBoxLayout()
        qualityLayout = QHBoxLayout()
        qualityLayout.addWidget(self.qualitySlider)
        qualityLayout.addWidget(self.qualityValueLabel)
        layout.addLayout(qualityLayout)
        layout.addWidget(self.formatComboBox)
        layout.addWidget(self.widthSpinBox)
        layout.addWidget(self.keepMetadata)
        # metadata between checkbox and compress
        layout.addWidget(self.metadataWidget)
        layout.addWidget(self.compressPushButton)
        layout.addWidget(self.downloadButton)
        layout.addStretch()
        self.setLayout(layout)
        # Start hidden
        self.metadataWidget.hide()