import os
import shlex
import stat
from lutris.runners.runner import Runner
from lutris.util import system


class moonlight(Runner):
    human_name = "Moonlight"
    description = "Streams games via moonlight"
    platforms = ["Stream"]
    runner_executable = "/snap/bin/moonlight"

    runner_options = [
        {
            "option": "src_ip",
            "type": "string",
            "label": "Source IP",
            "help": "IP Address to be used to stream from",
        },
    ]
    game_options = [
        {
            "option": "game_name",
            "type": "string",
            "default_path": "game_name",
            "label": "Game name",
            "help": "Name of game to stream",
        },
        {
            "option": "src_ip",
            "type": "string",
            "label": "Source IP",
            "help": "IP Address to be used to stream from",
        },
    ]

    def __init__(self, config=None):
        super(moonlight, self).__init__(config)
        self.ld_preload = None

    def play(self):
        # Find the executable
        executable = self.get_executable()
        src_ip = self.game_config.get("src_ip")

        if (src_ip == None):
             src_ip = self.runner_config.get("src_ip")

        command = [
             executable,
             "stream",
             src_ip,
             self.game_config.get("game_name")
        ]

        return {"command": command}
