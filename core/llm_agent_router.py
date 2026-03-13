"""
Nova OS
Author: Tanju Aksit
Copyright (c) 2026 Tanju Aksit

This source code is licensed under the Nova OS Author Credit License.
"""

class LLMAgentRouter:

    def __init__(self, brain):
        self.brain = brain

    def route(self, text):

        prompt = f"""
Aşağıdaki kullanıcı mesajını analiz et.

Eğer mesaj bir sistem komutuysa şu formatta cevap ver:

TOOL:tool_name:param

Kullanılabilecek araçlar:

music_play:song
chrome_open
shutdown_pc

Eğer araç gerekmiyorsa sadece şunu yaz:

CHAT

Kullanıcı mesajı:
{text}
"""

        result = self.brain.think(prompt).strip()

        if result.startswith("TOOL:"):
            return result

        return None