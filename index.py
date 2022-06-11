from src.image import convert_image_to_base64
from src.ws import WS
from datetime import datetime
import json

if __name__ == '__main__':
    ws = WS.setup()
    while True:
        input()
        image = convert_image_to_base64("./test/WIN_20220611_19_45_33_Pro.jpg")

        now = datetime.now()
        current_time = now.strftime("%d/%m/%Y %H:%M:%S")

        data_package = {
            'data': str(image),
            'created_time': str(current_time)
        }
        
        WS.send(ws, json.dumps(data_package))

