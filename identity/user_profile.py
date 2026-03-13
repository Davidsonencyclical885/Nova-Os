"""
Nova OS
Author: Tanju Aksit
Copyright (c) 2026 Tanju Aksit

This source code is licensed under the Nova OS Author Credit License.
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

PROFILE_PATH = os.path.join(
    BASE_DIR,
    "config",
    "private",
    "user_profile.json"
)


class UserProfile:

    def __init__(self):

        self.data = {
            "name": "",
            "title": "",
            "interests": [],
            "goals": [],
            "personality_notes": []
        }

        self.load()

    def load(self):

        if os.path.exists(PROFILE_PATH):

            with open(PROFILE_PATH, "r", encoding="utf-8") as f:
                self.data = json.load(f)

    def save(self):

        os.makedirs(os.path.dirname(PROFILE_PATH), exist_ok=True)

        with open(PROFILE_PATH, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)

    def add_interest(self, interest):

        if interest not in self.data["interests"]:
            self.data["interests"].append(interest)
            self.save()

    def add_goal(self, goal):

        if goal not in self.data["goals"]:
            self.data["goals"].append(goal)
            self.save()

    def add_personality_note(self, note):

        self.data["personality_notes"].append(note)
        self.save()