"""
Nova OS
Author: Tanju Aksit
Copyright (c) 2026 Tanju Aksit

This source code is licensed under the Nova OS Author Credit License.
"""

import re


class MemoryConsolidation:

    def __init__(self, identity_engine, vector_store):
        self.identity = identity_engine
        self.vector_store = vector_store

    def process(self, messages):

        learned = []

        for role, text in messages:

            t = text.lower()

            # yaş öğrenme
            age_match = re.search(r"(\d{1,3}) yaşındayım", t)

            if age_match:
                age = age_match.group(1)
                self.identity.set_value("age", age)

                learned.append(f"Yaş öğrenildi: {age}")

            # ilgi alanı öğrenme
            interest_match = re.search(r"ben (.+) yapıyorum", t)

            if interest_match:
                interest = interest_match.group(1)

                self.identity.learn_user_interest(interest)

                learned.append(f"İlgi alanı öğrenildi: {interest}")

        return learned