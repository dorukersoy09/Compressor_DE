from PIL import Image
import piexif


def get_metadata(image_path):
    image = Image.open(image_path)
    data = {}

    if "exif" not in image.info:
        return data

    exif = piexif.load(
        image.info["exif"]
    )

    zero = exif["0th"]
    exif_data = exif["Exif"]

    if piexif.ImageIFD.Model in zero:
        data["camera"] = (
            zero[
                piexif.ImageIFD.Model
            ]
            .decode(errors="ignore")
        )

    if piexif.ImageIFD.Artist in zero:
        data["artist"] = (
            zero[
                piexif.ImageIFD.Artist
            ]
            .decode(errors="ignore")
        )

    if piexif.ImageIFD.ImageDescription in zero:
        data["description"] = (
            zero[
                piexif.ImageIFD.ImageDescription
            ]
            .decode(errors="ignore")
        )

    if piexif.ExifIFD.DateTimeOriginal in exif_data:
        data["date"] = (
            exif_data[
                piexif.ExifIFD.DateTimeOriginal
            ]
            .decode(errors="ignore")
        )

    if piexif.ImageIFD.Copyright in zero:
        data["copyright"] = (
            zero[
                piexif.ImageIFD.Copyright
            ]
            .decode(errors="ignore")
        )
    return data