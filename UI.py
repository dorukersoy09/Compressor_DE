import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QHBoxLayout,
    QFrame,
    QFileDialog,
    QMessageBox
)
import metadata
import compressor
from dragdrop import DragDropWidget
from controles import ControlsWidget


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(
            "DECompressor"
        )
        self.resize(
            1000,
            700
        )
        mainLayout = QHBoxLayout()
        # LEFT SIDE
        self.dragDrop = DragDropWidget()
        # RIGHT SIDE
        self.controls = ControlsWidget()
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

window = MainWindow()

window.show()

sys.exit(
    app.exec()
)