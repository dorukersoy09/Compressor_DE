# Compressor_DE

A desktop image compression and optimization application built with Python and PyQt5. DECompressor allows users to compress images while maintaining visual quality, resize images, convert between multiple formats, preview the compressed result before saving, and edit image metadata through an intuitive drag-and-drop interface.

---

## Overview

DECompressor was created as a personal project to learn desktop application development, image processing, and graphical user interface design with Python. The application focuses on making image compression simple while giving users control over quality, resolution, output format, and metadata.

Instead of using command-line tools, DECompressor provides an easy-to-use graphical interface where users can simply drag an image into the application, adjust compression settings, preview the result, and save the optimized image to any location.

---

## Features

* Drag and drop image importing
* Live image preview
* Adjustable JPEG/WebP compression quality
* Image resizing while preserving aspect ratio
* Multiple output formats

  * JPEG
  * PNG
  * WEBP
  * BMP
* Metadata preservation
* Metadata editing

  * Camera model
  * Artist
  * Description
  * Copyright
  * Date Taken
* Preview compressed image before saving
* Download compressed image to any location
* Clean and modular user interface built with PyQt5

---

## Technologies Used

* Python 3
* PyQt5
* Pillow (PIL)
* piexif

---

## Project Structure

```text
DECompressor/
│
├── UI.py                 # Main application window
├── DragDrop.py           # Drag-and-drop image widget
├── controles.py          # Control panel (quality, format, width, buttons)
├── MetadataWidget.py     # Metadata editing interface
├── metadata.py           # Reads image metadata
├── compressor.py         # Image compression engine
│
├── requirements.txt
└── README.md
```

---

## How It Works

### 1. Import an Image

Drag and drop an image into the preview area.

---

### 2. Configure Compression

Users can choose:

* Compression quality
* Output width
* Output format
* Whether metadata should be preserved

---

### 3. Edit Metadata (Optional)

If metadata preservation is enabled, users may edit metadata before compression.

Editable fields include:

* Camera Model
* Artist
* Description
* Copyright
* Date Taken

---

### 4. Compress

The application:

* Reads the original image
* Resizes it if necessary
* Compresses it using the selected quality
* Writes the selected metadata
* Generates a compressed preview

---

### 5. Save

The user can choose the filename and destination using the Download button.

---

## Learning Objectives

This project was developed to gain experience with:

* Desktop GUI development
* Object-oriented programming
* Python project organization
* Image manipulation
* File handling
* EXIF metadata management
* Event-driven programming
* Modular software architecture

---

## Future Improvements

Some planned improvements include:

* Batch image compression
* Folder compression
* Drag-and-drop multiple files
* Image size comparison
* Compression statistics
* Before/after file size graphs
* Dark mode
* Undo functionality
* Custom output folder selection
* More editable EXIF fields
* TIFF and HEIC support
* Better metadata handling for PNG and WEBP
* Progress indicators during compression

---

## Screenshots

*Screenshots will be added as the project evolves.*

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/DECompressor.git
cd DECompressor
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python UI.py
```

---

## Requirements

```
Python 3.10+
PyQt5
Pillow
piexif
```

---

## Author

**Doruk Ersoy**

Developed as a personal software engineering project to explore Python desktop application development, image processing, and modular GUI design.

---

## License

This project is licensed under the MIT License. See the LICENSE file for more information.

