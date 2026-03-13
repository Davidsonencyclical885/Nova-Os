"""
Nova OS
Author: Tanju Aksit
Copyright (c) 2026 Tanju Aksit

This source code is licensed under the Nova OS Author Credit License.
"""

import json
import os
from config.paths import PEOPLE_GRAPH_PATH


class PeopleGraph:

    def __init__(self):

        self.nodes = {}

        self._load()

    def _load(self):

        if not os.path.exists(PEOPLE_GRAPH_PATH):
            return

        try:
            with open(PEOPLE_GRAPH_PATH, "r", encoding="utf-8") as f:

                content = f.read().strip()

                if not content:
                    return

                self.nodes = json.loads(content)

        except Exception:
            self.nodes = {}

    def _save(self):

        os.makedirs(os.path.dirname(PEOPLE_GRAPH_PATH), exist_ok=True)

        with open(PEOPLE_GRAPH_PATH, "w", encoding="utf-8") as f:
            json.dump(self.nodes, f, indent=2, ensure_ascii=False)

    def add_person(self, name, relation="", notes=""):

        self.nodes[name] = {
            "relation": relation,
            "notes": notes
        }

        self._save()

    def get_person(self, name):

        return self.nodes.get(name)

    def list_people(self):

        return self.nodes

    def remove_person(self, name):

        if name in self.nodes:
            del self.nodes[name]
            self._save()

    def update_relation(self, name, relation):

        if name in self.nodes:
            self.nodes[name]["relation"] = relation
            self._save()

    def update_notes(self, name, notes):

        if name in self.nodes:
            self.nodes[name]["notes"] = notes
            self._save()