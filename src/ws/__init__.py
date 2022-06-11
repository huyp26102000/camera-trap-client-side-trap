from websocket import create_connection

class WS:
    @staticmethod
    def setup():
        return create_connection("ws://94.237.66.183:8080")

    @staticmethod
    def send(ws, data):
        ws.send(data)
