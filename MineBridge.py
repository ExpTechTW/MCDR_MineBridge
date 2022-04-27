from mcdreforged.api.all import *
import json
import threading
import websocket
import time

PLUGIN_METADATA = {
    'id': 'minebridge',
    'version': '1.0.0',
    'name': 'MineBridge'
}

UUID = "9fab9d6e-dc44-460e-8bc7-8293564152ab"


def on_server_startup(server: PluginServerInterface):
    ws.send(json.dumps({
        "APIkey": "a5ef9cb2cf9b0c14b6ba71d0fc39e329",
        "Function": "MineBridge",
        "Type": "data",
        "FormatVersion": 1,
        "UUID": UUID,
        "Value": {
            "function": "on_server_startup"
        }
    }))


def on_server_stop(server: PluginServerInterface, old):
    ws.send(json.dumps({
        "APIkey": "a5ef9cb2cf9b0c14b6ba71d0fc39e329",
        "Function": "MineBridge",
        "Type": "data",
        "FormatVersion": 1,
        "UUID": UUID,
        "Value": {
            "function": "on_server_stop"
        }
    }))


def on_player_left(server: ServerInterface, player: str):
    ws.send(json.dumps({
        "APIkey": "a5ef9cb2cf9b0c14b6ba71d0fc39e329",
        "Function": "MineBridge",
        "Type": "data",
        "FormatVersion": 1,
        "UUID": UUID,
        "Value": {
            "function": "on_player_left",
            "player": player
        }
    }))


def on_player_joined(server: ServerInterface, player, info):
    print(info)
    ws.send(json.dumps({
            "APIkey": "a5ef9cb2cf9b0c14b6ba71d0fc39e329",
            "Function": "MineBridge",
            "Type": "data",
            "FormatVersion": 1,
            "UUID": UUID,
            "Value": {
                "function": "on_player_joined",
                "player": player
            }
            }))


def on_server_start(server: PluginServerInterface):
    global Server
    Server = server


def on_user_info(server: PluginServerInterface, info: Info):
    if info.is_player:
        ws.send(json.dumps({
            "APIkey": "a5ef9cb2cf9b0c14b6ba71d0fc39e329",
            "Function": "MineBridge",
            "Type": "data",
            "FormatVersion": 1,
            "UUID": UUID,
            "Value": {
                "function": "on_user_info",
                "player": info.player,
                "text": info.content
            }
        }))


def main():
    def on_message(ws, message):
        Json = json.loads(message)
        if Json["text"] != "":
            Server.say(Json["text"])

    def on_close(ws, close_status_code, close_msg):
        time.sleep(2)
        ws.run_forever()

    def on_open(ws):
        ws.send(json.dumps({
            "APIkey": "a5ef9cb2cf9b0c14b6ba71d0fc39e329",
            "Function": "MineBridge",
            "Type": "connect",
            "FormatVersion": 1,
            "UUID": UUID
        }))

    global ws
    ws = websocket.WebSocketApp("ws://150.117.110.118:910",
                                on_open=on_open,
                                on_message=on_message,
                                on_close=on_close)
    ws.run_forever()


t = threading.Thread(target=main)
t.start()
