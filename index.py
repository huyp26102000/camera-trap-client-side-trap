from src.IO.camera import setup, capture
from src.image import convert_image_to_base64
from src.ws import WS
from datetime import datetime, timezone
import json

if __name__ == '__main__':
    # cam = setup()
    # capture(cam)


    ws = WS.setup()
    while True:
        index = input()
        image = convert_image_to_base64(f"./test/{index}.jpg")

        now = datetime.now(timezone.utc)
        current_time = now.strftime("%B %d %Y, %I:%M:%S %p")
        data_package = {
            'data': str(image),
            'created_time': str(current_time)
        }

        WS.send(ws, json.dumps(data_package))

