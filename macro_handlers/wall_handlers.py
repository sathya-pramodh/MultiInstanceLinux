import os
from obswebsocket import obsws, requests


def wall_switch_macro(obs_hex_code, host, port, password, wall_scene_name):
    os.system("wmctrl -i -a " + obs_hex_code)
    websocket_object = obsws(host, port, password)
    websocket_object.connect()
    try:
        scene_object = websocket_object.call(requests.GetSceneList())
        list_scenes = scene_object.datain["scenes"]
        for scene in list_scenes:
            if scene["name"] == wall_scene_name:
                websocket_object.call(requests.SetCurrentScene(wall_scene_name))
                websocket_object.disconnect()
                return 0
        else:
            websocket_object.disconnect()
            return -1
    except KeyboardInterrupt:
        websocket_object.disconnect()
        return 0
