import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QHBoxLayout,
    QFrame,
    QFileDialog,
    QMessageBox
)
import requests
import metadata
import compressor
import api_client
from dragdrop import DragDropWidget
from controles import ControlsWidget


class MainWindow(QWidget):
    def __init__(
        self,
        mode="standalone",
        sender="",
        receiver=""
    ):
        super().__init__()
        self.mode = mode
        self.sender = sender
        self.receiver = receiver

        self.setWindowTitle(
            "DECompressor"
        )
        if self.mode == "messenger":
            self.resize(
                1100,
                700
            )
        else:
            self.resize(
                1000,
                700
            )
        mainLayout = QHBoxLayout()
        # LEFT SIDE
        self.dragDrop = DragDropWidget()
        # RIGHT SIDE
        self.controls = ControlsWidget(self.mode)
        separator = QFrame()
        separator.setFrameShape(QFrame.VLine)
        separator.setFrameShadow(QFrame.Sunken)
        mainLayout.addWidget(self.dragDrop,2)
        mainLayout.addWidget(separator)
        mainLayout.addWidget(self.controls,1)
        # Buttons
        self.controls.compressPushButton.clicked.connect(
            self.compress_image
        )
        if self.mode == "messenger":
            self.controls.downloadButton.setText(
                "Send"
            )
            self.controls.downloadButton.clicked.connect(
                self.send_image
            )
        else:
            self.controls.downloadButton.clicked.connect(
                self.download_image
            )

        # When image is dropped
        self.dragDrop.imageLabel.imageDropped.connect(
            self.load_metadata
        )
        self.setLayout(
            mainLayout
        )
    
    def send_image(self):
        caption = self.controls.captionBox.toPlainText()
        if not hasattr(
            self,
            "compressed_path"
        ):
            QMessageBox.warning(
                self,
                "Error",
                "Compress an image first"
            )
            return
        result = api_client.send_image(
            self.sender,
            self.receiver,
            caption,
            self.compressed_path
        )
        print(result)
        if result.get("success"):
            self.close()


    def load_metadata(self):
        path = self.dragDrop.imageLabel.file_path
        data = metadata.get_metadata(
            path
        )
        self.controls.metadataWidget.set_metadata(
            data
        )

    def compress_image(self):
        src_path = self.dragDrop.imageLabel.file_path
        if src_path is None:
            return
        metadata_data = (
            self.controls.metadataWidget.get_metadata()
        )
        self.compressed_path = compressor.compress_image(
            src_path,
            self.controls.qualitySlider.value(),
            self.controls.widthSpinBox.value(),
            self.controls.formatComboBox.currentText(),
            self.controls.keepMetadata.isChecked(),
            metadata_data
        )
        # Show compressed image
        self.dragDrop.imageLabel.show_image(
            self.compressed_path
        )

    def download_image(self):
        if not hasattr(
            self,
            "compressed_path"
        ):
            return

        save_path,_ = QFileDialog.getSaveFileName(
            self,
            "Save Image",
            "compressed.jpg",
            "Images (*.jpg *.png *.webp)"
        )
        if save_path:
            import shutil
            shutil.copy(
                self.compressed_path,
                save_path
            )
            QMessageBox.information(
                self,
                "Saved",
                "Image saved successfully!"
            )

app = QApplication(sys.argv)

import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    "--mode",
    default="standalone"
)

parser.add_argument(
    "--sender",
    default=""
)

parser.add_argument(
    "--receiver",
    default=""
)

args = parser.parse_args()

window = MainWindow(
    args.mode,
    args.sender,
    args.receiver
)


if args.mode == "messenger":

    window.setWindowTitle(
        "JavaFXEncryptor - Image Compressor"
    )

    window.setWindowFlags(
        Qt.Window
    )


window.show()

sys.exit(app.exec_())
