"""
Nova OS
Author: Tanju Aksit
Copyright (c) 2026 Tanju Aksit

This source code is licensed under the Nova OS Author Credit License.
"""

import json

class Router:
    def route(self, response_text):
        try:
            data = json.loads(response_text)
            return data
        except:
            return {"intent": "chat", "text": response_text}