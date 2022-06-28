"""
This is a helper script that handles the wall keybinds.
"""

# Author: sathya-pramodh
# Github: https://github.com/sathya-pramodh/

# Software Licensed under the MIT License.

# License terms:

# MIT License

# Copyright (c) 2022 sathya-pramodh

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Imports
import os
from obswebsocket import obsws, requests


def wall_switch_macro(
    obs_hex_code, host, port, password, wall_scene_name, switch_to_wall=True
):
    """
    Handles the switch to wall macro.

    obs_hex_code
    The string that denotes the hex code of the OBS window.

    host
    The string that denotes the hostname of the OBS websocket server.

    port
    The integer port number of the OBS websocket server to connect to.

    password
    The string password to be used to connect to the OBS websocket server.

    wall_scene_name
    The string denoting the name of the wall scene on OBS.

    switch_to_wall
    The boolean value indicating whether to switch to the wall scene or an instance scene.

    Returns 0 if the code executed successfully, else -1
    """
    if switch_to_wall:
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
