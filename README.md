# DECompressor

A desktop image compression and optimization application built with **Python and PyQt5**.

DECompressor allows users to reduce image file sizes while maintaining visual quality through adjustable compression settings, resizing tools, format conversion, metadata management, and real-time preview. The application provides a simple drag-and-drop workflow similar to professional image optimization tools while giving users detailed control over the compression process.

---

# Overview

DECompressor was developed as a personal software engineering project focused on desktop application development, image processing, and user interface design.

The goal of the project was to create a lightweight but powerful image optimization tool that allows users to:

- Reduce image file size
- Preserve or modify image metadata
- Convert between different image formats
- Preview compression results before exporting
- Control output quality and resolution

Instead of relying on command-line utilities, DECompressor provides a complete graphical workflow where users can import an image, customize optimization settings, preview changes, and export the final result.

---

# Features

## Image Processing

- Drag-and-drop image importing
- Real-time image preview
- Adjustable compression quality
- Image resizing with aspect ratio preservation
- Compression optimization for smaller file sizes
- Before-save preview system

## Supported Formats

Input and output support:

- JPEG
- PNG
- WEBP
- BMP

## Metadata Management

DECompressor supports reading and modifying EXIF metadata.

Editable metadata fields include:

- Camera Model
- Artist
- Image Description
- Copyright Information
- Date Taken

Users can choose whether metadata should be preserved during compression.

## User Interface

- Modern desktop interface built with PyQt5
- Modular component-based design
- Dedicated compression controls
- Drag-and-drop workflow
- Image preview system
- File export functionality

---

# Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Core application language |
| PyQt5 | Desktop graphical interface |
| Pillow (PIL) | Image processing and manipulation |
| piexif | EXIF metadata handling |

---

# Project Architecture

```
DECompressor/
│
├── UI.py                 # Main application window
├── DragDrop.py           # Drag and drop image importing
├── controles.py          # Compression controls and settings
├── MetadataWidget.py     # Metadata editing interface
│
├── metadata.py            # EXIF metadata extraction
├── compressor.py          # Compression engine
│
├── requirements.txt
└── README.md
```

The project follows a modular structure where:

- UI components handle user interaction
- The compressor engine handles image processing
- Metadata modules manage EXIF information
- DragDrop handles file importing

---

# How It Works

## 1. Import Image

Users drag an image into the application window.

The application automatically:

- Detects the file type
- Loads the image
- Displays a preview

---

## 2. Configure Optimization Settings

Users can customize:

- Compression quality
- Output resolution
- File format
- Metadata preservation options

---

## 3. Modify Metadata

Optional metadata editing allows users to change:

- Camera information
- Artist details
- Description
- Copyright
- Date information

---

## 4. Compression Process

The compression engine:

1. Loads the original image
2. Applies resizing if selected
3. Converts the image format if needed
4. Compresses using the chosen quality level
5. Applies metadata changes
6. Generates a preview result

---

## 5. Export

Users can select the destination location and save the optimized image.

---

# Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/DECompressor.git

cd DECompressor
```

---

## Install Dependencies

Recommended:

```bash
python -m venv venv
```

Activate environment:

### macOS / Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install requirements:

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
python UI.py
```

---

# Requirements

```
Python 3.10+
PyQt5
Pillow
piexif
```

---

# Screenshots

<img width="1010" height="732" alt="DECompressor Interface" src="https://github.com/user-attachments/assets/bf88d389-2b7c-49c4-bcd6-866e2f25f906" />

<img width="1005" height="728" alt="Compression Controls" src="https://github.com/user-attachments/assets/d946e65e-9f40-4fb4-84d2-e2cf41d7dc4e" />

<img width="999" height="728" alt="Metadata Editing" src="https://github.com/user-attachments/assets/949a5953-f181-46b8-9482-f01b752a52ed" />

---

# Learning Objectives

This project helped develop experience in:

- Desktop application development
- GUI architecture
- Object-oriented programming
- Image processing algorithms
- File management
- EXIF metadata manipulation
- Event-driven programming
- Modular software design

---

# Future Improvements

Planned improvements:

- Batch image compression
- Folder-level optimization
- Multiple image drag-and-drop
- Compression statistics
- Before/after size comparison
- Compression graphs
- Dark mode
- Undo system
- Custom export locations
- More EXIF fields
- TIFF and HEIC support
- Improved PNG and WEBP metadata handling
- Compression progress indicators

---

# Author

## Doruk Ersoy

Developed as a personal software engineering project exploring:

- Python desktop applications
- Image optimization
- GUI engineering
- File processing systems

---

# License

Copyright © 2026 Doruk Ersoy

All rights reserved.

This project is provided for educational and portfolio purposes. No part of this software may be copied, modified, distributed, or used commercially without explicit written permission from the author.
