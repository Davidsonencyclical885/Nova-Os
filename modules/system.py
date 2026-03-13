"""
Nova OS
Author: Tanju Aksit
Copyright (c) 2026 Tanju Aksit

This source code is licensed under the Nova OS Author Credit License.
"""

import os
import webbrowser


class SystemModule:

    def open_chrome(self):

        webbrowser.open("https://google.com")
        return "Chrome açıldı."

    def shutdown(self):

        os.system("shutdown /s /t 5")
        return "Bilgisayar 5 saniye içinde kapanacak."