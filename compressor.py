from PIL import Image
import piexif


def compress_image(
        src_path,
        quality,
        width,
        output_format,
        keep_metadata,
        metadata):

    image = Image.open(src_path)

    original_width, original_height = image.size
    
    exif_bytes = None

    # -----------------------------
    # Create metadata if requested
    # -----------------------------

    if keep_metadata:
        exif_dict = {
            "0th": {},
            "Exif": {},
            "GPS": {},
            "1st": {},
            "thumbnail": None
        }

        if metadata["artist"]:
            exif_dict["0th"][
                piexif.ImageIFD.Artist
            ] = metadata["artist"].encode()

        if metadata["description"]:
            exif_dict["0th"][
                piexif.ImageIFD.ImageDescription
            ] = metadata["description"].encode()

        if metadata["camera"]:
            exif_dict["0th"][
                piexif.ImageIFD.Model
            ] = metadata["camera"].encode()

        if metadata["copyright"]:
            exif_dict["0th"][
                piexif.ImageIFD.Copyright
            ] = metadata["copyright"].encode()

        if metadata["date"]:
            exif_dict["0th"][
                piexif.ImageIFD.DateTime
            ] = metadata["date"].encode()

        exif_bytes = piexif.dump(exif_dict)

    # -----------------------------
    # Resize image
    # -----------------------------

    if original_width > width:
        new_height = int(
            original_height *
            (width / original_width)
        )
        image = image.resize(
            (
                width,
                new_height
            )
        )

    # -----------------------------
    # Output file
    # -----------------------------

    output_path = ( "compressed." + output_format.lower())

    # -----------------------------
    # Save formats
    # -----------------------------
    if output_format == "JPEG":
        # JPEG does not support transparency
        if image.mode == "RGBA":
            image = image.convert("RGB")

        image.save(
            output_path,
            "JPEG",
            quality=quality,
            exif=exif_bytes if exif_bytes else b""
        )
    elif output_format == "PNG":
        image.save(
            output_path,
            "PNG"
        )
    elif output_format == "WEBP":
        image.save(
            output_path,
            "WEBP",
            quality=quality
        )
    else:
        image.save(
            output_path
        )
    return output_path