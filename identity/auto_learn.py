"""
Nova OS
Author: Tanju Aksit
Copyright (c) 2026 Tanju Aksit

This source code is licensed under the Nova OS Author Credit License.
"""

import re

class AutoLearner:

    def __init__(self, identity_engine):
        self.identity = identity_engine

    def process(self, text: str):
        t = text.lower()

        if "böyle deme" in t or "yanlış" in t:
            return "Uyarı kaydedildi."

        # yaş öğrenme
        m = re.search(r"\b(\d{1,3})\s*yaş", t)
        if m:
            age = m.group(1)
            self.identity.set_value("age", age)
            return f"Yaş bilgisi kaydedildi: {age}"

        # şehir öğrenme
        m = re.search(r"(?:ben|benim)\s+(?:şehir|şehirım|şehrim)\s+(\w+)", t)
        if m:
            city = m.group(1).capitalize()
            self.identity.set_value("city", city)
            return f"Şehir bilgisi kaydedildi: {city}"

        # ilgi alanı
        m = re.search(r"(?:ben|benim)\s+(.+?)\s+ile\s+ilgileniyorum", t)
        if m:
            interest = m.group(1).strip()
            self.identity.learn_user_interest(interest)
            return f"İlgi alanı eklendi: {interest}"

        return None 