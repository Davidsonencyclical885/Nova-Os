"""
Nova OS
Author: Tanju Aksit
Copyright (c) 2026 Tanju Aksit

This source code is licensed under the Nova OS Author Credit License.
"""

import re


class SemanticMemory:

    def analyze(self, text):

        t = text.lower()

        # yüksek güven (direkt kaydet)
        high_patterns = [
            r"ben (\d{1,3}) yaşındayım",
            r"ben .* yaşıyorum",
            r"benim hedefim (.+)",
            r"ben .* yapıyorum"
        ]

        for p in high_patterns:
            if re.search(p, t):
                return {
                    "type": "high",
                    "action": "save"
                }

        # orta güven (sor)
        medium_patterns = [
            r"ben .* seviyorum",
            r"ben .* öğreniyorum",
            r"ben .* ile ilgileniyorum"
        ]

        for p in medium_patterns:
            if re.search(p, t):
                return {
                    "type": "medium",
                    "action": "ask"
                }

        return None