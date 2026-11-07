# DICOM _ Tools

Python tools to read DICOM files, visualize medical images, apply windowing, edit DICOM tags, perform basic anonymization, and convert a group of DICOM files into PNG images.

## Features

- Read DICOM files using `pydicom`
- Display DICOM images using `matplotlib`
- Apply Min-Max normalization
- Apply windowing using custom `min_v` and `max_v` values
- Edit patient, institution, physician, and study information
- Perform basic DICOM anonymization
- Convert multiple DICOM files into PNG images

## Requirements

Install the required libraries:

```bash
pip install pydicom numpy matplotlib Pillow
```

Or, if you have a `requirements.txt` file:

```bash
pip install -r requirements.txt
```
