"""
Nova OS
Author: Tanju Aksit
Copyright (c) 2026 Tanju Aksit

This source code is licensed under the Nova OS Author Credit License.
"""

import re
from config.loader import config


class EventExtractor:

    def extract(self, text):

        t = text.lower()

        patterns = [
            (r"([a-zA-ZçğıöşüÇĞİÖŞÜ]+) ile buluştum", "buluştu"),
            (r"([a-zA-ZçğıöşüÇĞİÖŞÜ]+) ile konuştum", "konuştu"),
            (r"([a-zA-ZçğıöşüÇĞİÖŞÜ]+) ile görüştüm", "görüştü"),
            (r"arduino yaptım", "arduino yaptı"),
            (r"kod yazdım", "kod yazdı")
        ]

        for pattern, action in patterns:

            match = re.search(pattern, t)

            if match:

                target = match.group(1).capitalize() if match.groups() else None

                return {
                    "subject": config.get("name", "User"),
                    "action": action,
                    "target": target
                }

        return None