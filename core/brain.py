"""
Nova OS
Author: Tanju Aksit
Copyright (c) 2026 Tanju Aksit

This source code is licensed under the Nova OS Author Credit License.
"""

import requests


class Brain:

    def __init__(self, model="nova"):

        self.model = model
        self.url = "http://localhost:11434/api/generate"

    def think(self, prompt):

        try:

            response = requests.post(
                self.url,
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False
                },
                timeout=60
            )

            data = response.json()

            return data.get("response", "Model cevap veremedi.")

        except Exception as e:

            return f"Model hatası: {e}"