"""
Nova OS
Author: Tanju Aksit
Copyright (c) 2026 Tanju Aksit

This source code is licensed under the Nova OS Author Credit License.
"""

import sqlite3
from config.paths import DB_PATH
from identity.user_profile import UserProfile
from identity.people_graph import PeopleGraph


class IdentityEngine:

    def __init__(self):
        self.user = UserProfile()
        self.people = PeopleGraph()
        self.conn = sqlite3.connect(DB_PATH)

    def get_value(self, key):

        cursor = self.conn.cursor()
        cursor.execute("SELECT value FROM identity WHERE key=?", (key,))
        row = cursor.fetchone()

        return row[0] if row else None

    def set_value(self, key, value):

        cursor = self.conn.cursor()

        cursor.execute(
            "INSERT OR REPLACE INTO identity (key,value) VALUES (?,?)",
            (key, value)
        )

        self.conn.commit()

    def learn_user_interest(self, interest):
        self.user.add_interest(interest)

    def learn_goal(self, goal):
        self.user.add_goal(goal)

    def learn_person(self, name, relation="", notes=""):
        self.people.add_person(name, relation, notes)

    def get_summary(self):

        age = self.get_value("age")
        city = self.get_value("city")

        interests = "\n".join(self.user.data.get("interests", []))
        goals = "\n".join(self.user.data.get("goals", []))
        people = "\n".join(self.people.nodes.keys())

        summary = f"""
User: {self.user.data.get("name","User")}
Age: {age}
City: {city}

Interests:
{interests}

Goals:
{goals}

Known People:
{people}
"""

        return summary