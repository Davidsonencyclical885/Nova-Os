"""
Nova OS
Author: Tanju Aksit
Copyright (c) 2026 Tanju Aksit

This source code is licensed under the Nova OS Author Credit License.
"""

class EventQueryEngine:

    def __init__(self, event_memory):
        self.memory = event_memory

    def process(self, text):

        t = text.lower()

        if "en son ne yaptım" in t or "bugün ne yaptım" in t:

            events = self.memory.get_recent_events()

            if not events:
                return "Olay hafızamda kayıt bulunmuyor."

            answers = []

            for e in events:
                subject, action, target, ts = e

                if target:
                    answers.append(f"{target} ile {action}")
                else:
                    answers.append(action)

            return "Son olaylar: " + ", ".join(answers)

        if "kimi gördüm" in t or "kiminle konuştum" in t:

            events = self.memory.search_events("konuş")

            if not events:
                return "Bununla ilgili kayıt yok."

            return f"En son {events[0][2]} ile konuştun."

        return None