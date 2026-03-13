"""
Nova OS
Author: Tanju Aksit
Copyright (c) 2026 Tanju Aksit

This source code is licensed under the Nova OS Author Credit License.
"""

class AgentRouter:

    def __init__(self, llm_router):
        self.llm_router = llm_router

    def route(self, text):

        t = (text or "").lower()

        # FAST RULES
        if "şarkı" in t or "müzik" in t:
            return "TOOL:music_play"

        if "chrome aç" in t:
            return "TOOL:chrome_open"

        if "bilgisayarı kapat" in t:
            return "TOOL:shutdown_pc"

        # FALLBACK → LLM ROUTER
        return self.llm_router.route(text)