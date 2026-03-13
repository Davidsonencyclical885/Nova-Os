"""
Nova OS
Author: Tanju Aksit
Copyright (c) 2026 Tanju Aksit

This source code is licensed under the Nova OS Author Credit License.
"""

import webbrowser


class MusicModule:

    def play(self, song):

        url = f"https://www.youtube.com/results?search_query={song}"
        webbrowser.open(url)

        return f"{song} için müzik açıyorum."