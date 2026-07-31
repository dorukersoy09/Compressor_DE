import requests


API_URL = "http://127.0.0.1:8000/send-image"


def send_image(
        sender,
        receiver,
        caption,
        image_path
):

    data = {

        "sender": sender,

        "receiver": receiver,

        "caption": caption

    }


    with open(image_path, "rb") as file:

        files = {

            "image": file

        }


        response = requests.post(

            API_URL,

            files=files,

            data=data

        )


    try:

        return response.json()

    except Exception:

        return {
            "error": response.text
        }
