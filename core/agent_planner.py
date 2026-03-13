"""
Nova OS
Author: Tanju Aksit
Copyright (c) 2026 Tanju Aksit

This source code is licensed under the Nova OS Author Credit License.
"""

class AgentPlanner:

    def __init__(self):
        from modules.music import MusicModule
        from modules.system import SystemModule

        self.music = MusicModule()
        self.system = SystemModule()

    def execute(self, tool_command):

        if not tool_command or ":" not in tool_command:
            return None

        parts = tool_command.split(":")

        tool = parts[1].lower()

        param = parts[2] if len(parts) > 2 else None

        if tool == "music_play":
            return self.music.play(param)

        if tool == "chrome_open":
            return self.system.open_chrome()

        if tool == "shutdown_pc":
            return self.system.shutdown()

        return None