"""
Nova OS
Author: Tanju Aksit
Copyright (c) 2026 Tanju Aksit

This source code is licensed under the Nova OS Author Credit License.
"""

import re
from identity.knowledge_graph import KnowledgeGraph
from identity.information_extractor import InformationExtractor
from config.loader import config


class MemoryController:

    def __init__(self, identity_engine):

        self.identity = identity_engine
        self.graph = KnowledgeGraph()
        self.extractor = InformationExtractor()

        self.relation_map = {
            "kız arkadaşım": "sevgilim",
            "sevgilim": "sevgilim",
            "eski sevgilim": "eski sevgilim",
            "arkadaşım": "arkadaşım",
            "tanıdığım": "tanıdığım",
            "değerlim": "değerlim",
            "dostum": "dostum",
            "kardeşim": "kardeşim"
        }

    def clean_name(self, name: str):

        name = name.strip()
        name = name.split()[0]

        return name.title()

    def process(self, text: str):

        t = text.lower()

        # -------------------------
        # DÜZELTME
        # -------------------------

        if "yanlış" in t or "öyle değil" in t:
            return {
                "type": "correction",
                "message": "Anladım. Önceki bilgiyi hatalı olarak işaretledim."
            }

        # -------------------------
        # INFORMATION EXTRACTION
        # -------------------------

        info = self.extractor.extract(text)

        if info:

            person = info.get("person")
            relation = info.get("relation")
            age = info.get("age")
            school = info.get("school")
            grade = info.get("grade")

            if relation:
                relation = self.relation_map.get(relation, relation)

            if person:
                person = self.clean_name(person)

            # relation kaydet
            if person and relation:

                self.identity.learn_person(person, relation)

                try:
                    self.graph.add_relation(
                        config.get("name", "User"),
                        relation,
                        person
                    )
                except:
                    pass

            # age attribute
            if person and age is not None:
                try:
                    self.graph.set_attribute(person, "age", age)
                except:
                    pass

            # school attribute
            if person and school:
                try:
                    self.graph.set_attribute(person, "school", school)
                except:
                    pass

            # grade attribute
            if person and grade:
                try:
                    self.graph.set_attribute(person, "grade", grade)
                except:
                    pass

            msg = []

            if person and relation:
                msg.append(f"{person} ilişkisi kaydedildi: {relation}")

            if age is not None:
                msg.append(f"yaş={age}")

            if school:
                msg.append(f"okul={school}")

            if grade:
                msg.append(f"sınıf={grade}")

            if msg:
                return {
                    "type": "extraction",
                    "message": ", ".join(msg)
                }

        # -------------------------
        # KULLANICI YAŞI
        # -------------------------

        age_pattern = r"(\d{1,3}) yaşındayım"
        match = re.search(age_pattern, t)

        if match:

            age = match.group(1)

            self.identity.set_value("age", age)

            return {
                "type": "age_update",
                "age": age,
                "message": f"Yaş bilgisi güncellendi: {age}"
            }

        return None